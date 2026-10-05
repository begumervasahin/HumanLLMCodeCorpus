class b5:
    def fonk1(self, gene: b2) -> None:
        self.fonk2(gene)
    def fonk2(self, gene: b2) -> None:
        self.bit_string: a1 = 1
        for nucleotide in gene.upper():
            self.bit_string <<= 2
            self.bit_string |= self.fonk3(nucleotide)
    def fonk3(self, nucleotide: b2) -> a1:
        b1 = {'A': 0b00, 'C': 0b01, 'G': 0b10, 'T': 0b11}
        if nucleotide not in b1:
            raise ValueError("Invalid Nucleotide: {}".format(nucleotide))
        return b1[nucleotide]
    def fonk4(self) -> b2:
        gene: b2 = ""
        for i in range(0, self.bit_string.bit_length() - 1, 2):
            bits: a1 = self.bit_string >> i & 0b11
            gene += self.fonk5(bits)
        return gene[::-1]
    def fonk5(self, bits: a1) -> b2:
        b3 = {0b00: 'A', 0b01: 'C', 0b10: 'G', 0b11: 'T'}
        if bits not in b3:
            raise ValueError("Invalid bits: {}".format(bits))
        return b3[bits]
    def fonk6(self) -> b2:
        return self.fonk4()
if b4 = = "__main__":
    b6: b2 = "TAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATATAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATA"
    print("Original is {} bytes".format(len(b6.encode())))
    compressed: b5 = b5(b6)
    print("Compressed is {} bytes".format(compressed.bit_string.bit_length()
    print(compressed)
    print("Original is the same as decompressed: {}".format(b6 = = compressed.fonk4()))