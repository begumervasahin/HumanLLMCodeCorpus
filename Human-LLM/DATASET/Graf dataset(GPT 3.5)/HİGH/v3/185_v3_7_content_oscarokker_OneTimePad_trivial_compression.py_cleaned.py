from sys import getsizeof
class b3:
    def fonk1(self, gene: b1) -> None:
        self.fonk2(gene)
    def fonk2(self, gene: b1) -> None:
        self.bit_string: a1 = 1
        for nucleotide in gene.upper():
            self.bit_string <<= 2
            if nucleotide in "ACGT":
                self.bit_string |= {"A": 0b00, "C": 0b01, "G": 0b10, "T": 0b11}[nucleotide]
            else:
                raise ValueError(f"Invalid Nucleotide: {nucleotide}")
    def fonk3(self) -> b1:
        gene: b1 = ""
        for i in range(self.bit_string.bit_length() - 1, 0, -2):
            bits: a1 = self.bit_string >> i & 0b11
            gene += {0b00: "A", 0b01: "C", 0b10: "G", 0b11: "T"}[bits]
        return gene[::-1]
    def fonk4(self) -> b1:
        return self.fonk3()
if b2 = = "__main__":
    b4: b1 = "TAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATATAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATA"
    print("Original size: {} bytes".format(getsizeof(b4)))
    compressed: b3 = b3(b4)
    print("Compressed size: {} bytes".format(getsizeof(compressed.bit_string)))
    print(compressed)
    print("Original is the same as decompressed: {}".format(b4 = = compressed.fonk3()))