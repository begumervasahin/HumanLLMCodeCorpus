import torch.nn as nn
import torch
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from torch.utils.data import DataLoader, Dataset
from visdom import Visdom
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, mean_absolute_error
torch.manual_seed(1234)
np.random.seed(1234)
LR = 0.001
EPOCHS = 5
BATCH_SIZE = 256
WINDOW_LENGTH = 24
HIDDEN_SIZE = 64
PREDICTION_LENGTH = 24
TS_FEATURE = 1
RNN_INPUT_FEATURES = 8
TRAIN_PROP = 0.8
SLID_STEP = 1
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
def generate_samples(dataset, in_seq_len, out_seq_len, slid_step=1):
    samples = []
    step = slid_step
    valid_len = dataset.shape[0] - in_seq_len - out_seq_len + 1
    for i in range(0, valid_len, step):
        time_step = dataset[i:i + in_seq_len, 0]
        enc_seqs = dataset[i:i + in_seq_len, 1]
        dec_output_seqs = dataset[i + in_seq_len:i + in_seq_len + out_seq_len, 1]
        samples.append([time_step, enc_seqs, dec_output_seqs])
    return np.array(samples)
class TimeSeriesDataset(Dataset):
    def __init__(self, values):
        self.raw_data = values
        self.length = self.raw_data.shape[0]
    def __len__(self):
        return self.length
    def __getitem__(self, index):
        idx = index % self.length
        data = self.raw_data[idx]
        time_step = data[0].astype(np.float32)
        enc_seqs = data[1].astype(np.float32)
        dec_output_seqs = data[2].astype(np.float32)
        return time_step, enc_seqs, dec_output_seqs
class MLPAttention(nn.Module):
    def __init__(self, q_size, k_size, attn_size, bias=True, dropout=0.):
        super(MLPAttention, self).__init__()
        self.Wq = nn.Linear(q_size, attn_size, bias=bias)
        self.Wk = nn.Linear(k_size, attn_size, bias=bias)
        self.dropout = nn.Dropout(dropout)
    def forward(self, q, k, v):
        q = self.Wq(q)
        k = self.Wk(k)
        scores = torch.matmul(q, k.transpose(-2, -1))
        weight = self.dropout(torch.softmax(scores, dim=-1))
        atten_value = torch.bmm(weight, v)
        return atten_value, weight
class Seq2SeqPrediction(nn.Module):
    def __init__(self, ts_features, rnn_input_features, hidden_size, out_seq_len, use_pe=False, use_atten=False):
        super(Seq2SeqPrediction, self).__init__()
        self.input_size = ts_features
        self.hidden_size = hidden_size
        self.out_seq_len = out_seq_len
        self.rnn_input_size = rnn_input_features
        self.use_pe = use_pe
        self.use_attention = use_atten
        self.embed = nn.Linear(self.input_size, self.rnn_input_size)
        self.encoder = nn.LSTMCell(self.rnn_input_size, self.hidden_size)
        self.out_linear = nn.Linear(self.hidden_size, 1)
        if self.use_attention:
            self.attention = MLPAttention(hidden_size, hidden_size, hidden_size)
            self.decoder = nn.LSTMCell(self.hidden_size + self.hidden_size, self.hidden_size)
        else:
            self.decoder = nn.LSTMCell(self.hidden_size, self.hidden_size)
        if self.use_pe:
            self.time_embed = nn.Linear(self.input_size, self.rnn_input_size)
    def forward(self, enc_inputs, timestep=None):
        enc_inputs = self.embed(enc_inputs.unsqueeze(-1))
        if self.use_pe:
            enc_inputs = enc_inputs + self.time_embed(timestep.unsqueeze(-1))
        batch = enc_inputs.shape[0]
        in_hx, in_cx = torch.zeros(batch, self.hidden_size).to(device), torch.zeros(batch, self.hidden_size).to(device)
        out_seqs = []
        in_hxs = []
        for in_step in range(enc_inputs.shape[1]):
            in_hx, in_cx = self.encoder(enc_inputs[:, in_step, :], (in_hx, in_cx))
            if self.use_attention:
                in_hxs.append(in_hx)
        out_hx = in_hx
        out_cx = in_cx
        if self.use_attention:
            in_hxs = torch.stack(in_hxs, dim=1)
        for _ in range(self.out_seq_len):
            if self.use_attention:
                context, _ = self.attention(out_hx.unsqueeze(1), in_hxs, in_hxs)
                dec_input_i = torch.cat((out_hx, context.squeeze(1)), dim=-1)
            else:
                dec_input_i = out_hx
            out_hx, out_cx = self.decoder(dec_input_i, (out_hx, out_cx))
            out_seqs.append(out_hx)
        outs = self.out_linear(torch.stack(out_seqs, dim=1)).squeeze()
        return outs
def train_model(model, train_loader, val_loader, optimizer, criterion, viz):
    best_model = None
    min_loss = float('inf')
    for epoch in range(EPOCHS):
        model.train()
        train_loss = []
        for t_time, b_enc, b_dec_out in train_loader:
            t_time, b_enc, b_dec_out = t_time.to(device), b_enc.to(device), b_dec_out.to(device)
            out_seq = model(b_enc)
            loss = criterion(b_dec_out, out_seq)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            train_loss.append(loss.item())
        model.eval()
        with torch.no_grad():
            val_loss = []
            for e_time, b_enc, b_dec_out in val_loader:
                e_time, b_enc, b_dec_out = e_time.to(device), b_enc.to(device), b_dec_out.to(device)
                out_seq = model(b_enc)
                t_loss = criterion(b_dec_out, out_seq)
                val_loss.append(t_loss.item())
            epoch_loss = sum(val_loss) / len(val_loss)
            if epoch_loss < min_loss:
                min_loss = epoch_loss
                best_model = model.state_dict()
            if epoch % 20 == 0:
                viz.line([[sum(train_loss) / len(train_loss)], [epoch_loss]],
                         [epoch], win="train_loss", update="append")
                print(f"Epoch {epoch:02}, Train Loss: {sum(train_loss) / len(train_loss):.5f}, Val Loss: {epoch_loss:.5f}")
    print(f"Min val loss: {min_loss:.5f}")
    return best_model, min_loss
def evaluate_model(model, test_data, scaler):
    model.eval()
    test_len = test_data.shape[0]
    reals = []
    preds = []
    for i in range(0, test_len, WINDOW_LENGTH):
        if i + WINDOW_LENGTH + PREDICTION_LENGTH - 1 < test_len:
            interval_time, interval_seq = test_data[i:i + WINDOW_LENGTH, 0], test_data[i:i + WINDOW_LENGTH, 1]
            interval_time = torch.from_numpy(interval_time).float().unsqueeze_(0).to(device)
            interval_seq = torch.from_numpy(interval_seq).float().unsqueeze_(0).to(device)
            interval_preds = model(interval_seq).cpu().numpy().reshape(-1, 1)
            interval_reals = test_data[i + WINDOW_LENGTH:i + WINDOW_LENGTH + PREDICTION_LENGTH, 1]
            interval_time = test_data[i + WINDOW_LENGTH:i + WINDOW_LENGTH + PREDICTION_LENGTH, 0]
            interval_preds = np.hstack((interval_time.reshape(-1, 1), interval_preds))
            interval_reals = np.hstack((interval_time.reshape(-1, 1), interval_reals.reshape(-1, 1)))
            interval_preds = scaler.inverse_transform(interval_preds)
            interval_reals = scaler.inverse_transform(interval_reals)
            preds.extend(interval_preds[:, 1])
            reals.extend(interval_reals[:, 1])
    model.plot_prediction_result(preds, reals)
    metrics = model.calculate_metrics(reals, preds)
    print(f"Test RMSE: {metrics[0]:.5f}, MAE: {metrics[1]:.5f}, MAPE: {metrics[2]:.5f}, SMAPE: {metrics[3]:.5f}")
if __name__ == '__main__':
    viz = Visdom()
    viz.line([[0., 0.]], [0.], win="train_loss", opts=dict(title="Train Loss, Validation Loss", legend=["Train Loss", "Validation Loss"]))
    train_file_path = "pollution.csv"
    training = pd.read_csv(train_file_path).values
    if training.ndim == 1:
        training = training.reshape(-1, 1)
    scaler = MinMaxScaler()
    training = scaler.fit_transform(training)
    train_samples = int(training.shape[0] * TRAIN_PROP)
    test_data = training[train_samples:]
    train_data = generate_samples(training[:train_samples], WINDOW_LENGTH, PREDICTION_LENGTH)
    trainer, validation = train_test_split(train_data, train_size=TRAIN_PROP)
    train_loader = DataLoader(dataset=TimeSeriesDataset(trainer), batch_size=BATCH_SIZE)
    val_loader = DataLoader(dataset=TimeSeriesDataset(validation), batch_size=BATCH_SIZE)
    model = Seq2SeqPrediction(TS_FEATURE, RNN_INPUT_FEATURES, HIDDEN_SIZE, PREDICTION_LENGTH,
                             use_pe=False, use_atten=False).to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=LR)
    criterion = nn.MSELoss()
    best_model, min_val_loss = train_model(model, train_loader, val_loader, optimizer, criterion, viz)
    torch.save(best_model, f"./model_stat_val_loss_{min_val_loss:.5f}.pth")
    with torch.no_grad():
        model.load_state_dict(best_model)
        evaluate_model(model, test_data, scaler)