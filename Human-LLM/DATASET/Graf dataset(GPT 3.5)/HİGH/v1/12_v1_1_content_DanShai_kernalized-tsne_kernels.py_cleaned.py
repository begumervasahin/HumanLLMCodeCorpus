
from kernels import Kernels
from Bio import SeqIO
b1 = []
for record in SeqIO.parse("DNASequences.fasta", "fasta"):
    b1.append(record.seq)
b2 = Kernels(b1)
b3 = b2.process_data()
print("PCA result:")
print(b3)