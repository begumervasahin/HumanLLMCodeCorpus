class class1:
    def fonk1(self, nbuckets):
        self.b1 = [[] for _ in range(nbuckets)]
    def fonk2(self, key):
        if isinstance(key, int):
            return key
        if isinstance(key, str):
            return sum(31 ** i * ord(char) for i, char in enumerate(key))
        raise TypeError("Unsupported key type")
    def fonk3(self, key, value):
        b2 = self.fonk2(key) % len(self.b1)
        b3 = self.b1[b2]
        for i, (b4, v) in enumerate(b3):
            if b4 = = key:
                b3[i] = (key, value)
                return
        b3.append((key, value))
    def fonk4(self, key):
        b2 = self.fonk2(key) % len(self.b1)
        b3 = self.b1[b2]
        for b4, v in b3:
            if b4 = = key:
                return v
        return None
    def fonk5(self):
        b5 = (f"{b4}:{v}" for b3 in self.b1 for b4, v in b3)
        return "{" + ", ".join(b5) + "}"
    def fonk6(self):
        return self.fonk5()
    def fonk7(self):
        b6 = []
        for i, b3 in enumerate(self.b1):
            b5 = ", ".join(f"{b4}:{v}" for b4, v in b3)
            b6.append(f"{str(i).zfill(4)}-> {b5}")
        return "\n".join(b6)
if b7 = = "__main__":
    b8 = class1(5)
    b8.fonk3("apple", 10)
    b8.fonk3("banana", 20)
    b8.fonk3("apple", 5)
    print("class1:", b8)
    print("Buckets:", b8.fonk7())
    print("Get 'apple':", b8.fonk4("apple"))
    print("Get 'banana':", b8.fonk4("banana"))
    print("Get 'orange':", b8.fonk4("orange"))