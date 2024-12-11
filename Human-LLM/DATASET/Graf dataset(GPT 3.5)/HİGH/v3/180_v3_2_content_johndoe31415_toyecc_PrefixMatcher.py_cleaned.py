class class1:
    def fonk1(self, options):
        self.b1 = options
    def fonk2(self, value):
        b2 = self.fonk3(value)
        if len(b2) == 0:
            raise ValueError(f"'{value}' did not match any options.")
        elif len(b2) > 1:
            raise ValueError(f"'{value}' is ambiguous. Please clarify further. Available options: {', '.join(sorted(b2))}")
        return b2[0]
    def fonk3(self, value):
        return [option for option in self.b1 if option.startswith(value)]
if b3 = = "__main__":
    b4 = class1(["import", "install", "foo"])
    print("Matches for 'i':", b4.fonk3("i"))
    print("Unique match for 'i':", b4.fonk2("i"))