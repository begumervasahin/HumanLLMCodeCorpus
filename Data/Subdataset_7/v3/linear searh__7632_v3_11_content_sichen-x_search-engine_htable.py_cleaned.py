class class1:
    def fonk1(self, nbuckets):
        self.b1 = [[] for _ in range(nbuckets)]
    def fonk2(self, key):
        if isinstance(key, int):
            return key
        elif isinstance(key, str):
            a1 = 0
            for char in key:
                a1 = a1 * 31 + ord(char)
            return a1
        else:
            return None
    def fonk3(self, key, value):
        if self.b1 is None or not self.b1:
            return
        b2 = self.fonk2(key) % len(self.b1)
        b3 = self.b1[b2]
        for i, (b4, v) in enumerate(b3):
            if b4 = = key:
                b3[i] = (key, value)
                return
        b3.append((key, value))
    def fonk4(self, key):
        if self.b1 is None or not self.b1:
            return None
        b2 = self.fonk2(key) % len(self.b1)
        b3 = self.b1[b2]
        for b4, v in b3:
            if b4 = = key:
                return v
        return None
    def fonk5(self):
        if not self.b1:
            return "{}"
        b5 = [f"{b4}:{v}" for b3 in self.b1 for b4, v in b3]
        return "{" + ", ".join(b5) + "}"
    def fonk6(self):
        return str(self)
    def fonk7(self):
        if not self.b1:
            return ""
        b6 = ""
        for i, b3 in enumerate(self.b1):
            b5 = [f"{b4}:{v}" for b4, v in b3]
            b6 += f"{str(i).zfill(4)}->" + ", ".join(b5) + "\n"
        return b6
b7 = class1(5)
b7.fonk3("apple", 10)
b7.fonk3("banana", 20)
b7.fonk3("apple", 5)
print("class1:", b7)
print("Buckets:", b7.fonk7())
print("Get 'apple':", b7.fonk4("apple"))
print("Get 'banana':", b7.fonk4("banana"))
print("Get 'orange':", b7.fonk4("orange"))