from sys import getsizeof
class b5:
    def fonk1(self, gene: b2) -> None:
        self.fonk2(gene)
    def fonk2(self, gene: b2) -> None:
        self.bit_string: a1 = 1
        for b1 in gene.upper():
            self.bit_string <<= 2
            if b1 = = "A":
                self.bit_string |= 0b00
            elif b1 = = "C":
                self.bit_string |= 0b01
            elif b1 = = "G":
                self.bit_string |= 0b10
            elif b1 = = "T":
                self.bit_string |= 0b11
            else:
                raise ValueError("Invalid Nucleotide: {}".format(b1))
    def fonk3(self) -> b2:
        gene: b2 = ""
        for i in range(0, self.bit_string.bit_length() - 1, 2):
            b3: a1 = self.bit_string >> i & 0b11
            if b3 = = 0b00:
                gene += "A"
            elif b3 = = 0b01:
                gene += "C"
            elif b3 = = 0b10:
                gene += "G"
            elif b3 = = 0b11:
                gene += "T"
            else:
                raise ValueError("Invalid b3: {}".format(b3))
        return gene[::-1]
    def fonk4(self) -> b2:
        return self.fonk3()
if b4 = = "__main__":
    b6: b2 = "TAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATATAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATA"
    print("Original is {} bytes".format(getsizeof(b6)))
    compressed: b5 = b5(b6)
    print("Compressed is {} bytes".format(getsizeof(compressed.bit_string)))
    print(compressed)
    print("Original is the same as decompressed: {}".format(b6 = = compressed.fonk3()))