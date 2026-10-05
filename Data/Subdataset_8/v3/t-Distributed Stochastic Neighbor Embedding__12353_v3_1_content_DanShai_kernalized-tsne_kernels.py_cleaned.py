
from kernels import Kernels
from Bio import SeqIO
def load_dna_sequences(fasta_file):
    sequences = []
    for record in SeqIO.parse(fasta_file, "fasta"):
        sequences.append(record.seq)
    return sequences
def main():
    fasta_file = "DNASequences.fasta"
    sequences = load_dna_sequences(fasta_file)
    kernel = Kernels(sequences)
    pca_result = kernel.process_data()
    print("PCA result:")
    print(pca_result)
if __name__ == "__main__":
    main()