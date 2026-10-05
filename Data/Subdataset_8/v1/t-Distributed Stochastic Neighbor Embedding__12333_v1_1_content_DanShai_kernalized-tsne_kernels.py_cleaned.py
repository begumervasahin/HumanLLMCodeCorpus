
from kernels import Kernels
from Bio import SeqIO
sequences = []
for record in SeqIO.parse("DNASequences.fasta", "fasta"):
    sequences.append(record.seq)
kernel = Kernels(sequences)
pca_result = kernel.process_data()
print("PCA result:")
print(pca_result)