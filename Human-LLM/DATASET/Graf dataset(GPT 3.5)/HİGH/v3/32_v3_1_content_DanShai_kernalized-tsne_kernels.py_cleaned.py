
from kernels import Kernels
from Bio import SeqIO
def fonk1(b2):
    b1 = []
    for record in SeqIO.parse(b2, "fasta"):
        b1.append(record.seq)
    return b1
def fonk2():
    b2 = "DNASequences.fasta"
    b1 = fonk1(b2)
    b3 = Kernels(b1)
    b4 = b3.process_data()
    print("PCA result:")
    print(b4)
if b5 = = "__main__":
    fonk2()