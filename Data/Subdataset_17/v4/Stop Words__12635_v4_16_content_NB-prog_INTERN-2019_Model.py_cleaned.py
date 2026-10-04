import torch
import torch.nn as nn
import numpy as np
class SkipGram(nn.Module):
    def __init__(self, vocab_size=20001, embedding_dims=50, neg_samples=20, word_freq=None, padding_idx=0):
        super(SkipGram, self).__init__()
        self.vocab_size = vocab_size
        self.embedding_dims = embedding_dims
        self.neg_samples = neg_samples
        self.input_embedding = nn.Embedding(self.vocab_size, self.embedding_dims, padding_idx=padding_idx)
        self.output_embedding = nn.Embedding(self.vocab_size, self.embedding_dims, padding_idx=padding_idx)
        self._init_embedding_weights()
        self.neg_sampling_dis = self.gen_neg_sampling_dis(word_freq)
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    def _init_embedding_weights(self):
        init_range = 0.5 / self.embedding_dims
        self.input_embedding.weight.data.uniform_(-init_range, init_range)
        self.output_embedding.weight.data.uniform_(-init_range, init_range)
    @staticmethod
    def gen_neg_sampling_dis(word_freq):
        if word_freq is None:
            raise ValueError("word_freq must be provided for negative sampling distribution.")
        neg_sampling_dis = np.power(word_freq, 0.75)
        neg_sampling_dis = neg_sampling_dis / neg_sampling_dis.sum()
        return neg_sampling_dis
    def forward(self, target, contexts):
        batch_size, context_size = target.size(0), contexts.size(1)
        neg_words = self._generate_neg_samples(batch_size, context_size)
        target_vectors = self.input_embedding(target).unsqueeze(2)
        contexts_vectors = self.output_embedding(contexts)
        neg_vectors = self.output_embedding(neg_words)
        pos_loss = torch.bmm(contexts_vectors, target_vectors).squeeze().sigmoid().log()
        neg_loss = torch.bmm(-neg_vectors, target_vectors).sigmoid().log().view(-1, context_size, self.neg_samples).sum(2)
        loss = -(pos_loss + neg_loss).mean()
        return loss
    def _generate_neg_samples(self, batch_size, context_size):
        neg_words = np.random.choice(self.vocab_size, size=(batch_size, context_size * self.neg_samples), replace=True, p=self.neg_sampling_dis)
        return torch.tensor(neg_words, dtype=torch.long, device=self.device)