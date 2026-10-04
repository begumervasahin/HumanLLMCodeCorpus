class class1:
    def fonk1(self, b4, b5, b6, b7, b8, b9):
        self.b1 = []
        self.b2 = set()
        self.b3 = set()
        self.b4 = b4
        self.b5 = b5
        self.b6 = b6
        self.b7 = b7
        self.b8 = b8
        self.b9 = b9
        self.a1 = 0
    def fonk2(self):
        while self.b1:
            self.a1 = max(self.a1, len(self.b1) + len(self.b2))
            b10 = min(self.b1, key=lambda x: x[1] + x[3])
            self.b1.remove(b10)
            path, g_cost, b5, b11 = b10
            b12 = path[-1]
            if self.fonk7(b12):
                return b5, path, g_cost, b11
            if b12 not in self.b2:
                self.b2.add(b12)
                for action in self.fonk5(b12):
                    b13 = self.fonk6(b12, action)
                    if b13 not in self.b2:
                        b14 = g_cost + self.fonk8(b12, b13)
                        b15 = self.fonk9(b13)
                        b16 = path + [b13]
                        b17 = b5 + [action]
                        self.b1.append([b16, b14, b17, b15])
                        if b13 not in self.b3:
                            self.b3.add(b13)
        return None
    def fonk3(self):
        b18 = self.fonk4()
        self.b1 = [[[b18], 0, [], self.fonk9(b18)]]
        self.b2 = set()
        self.b3 = set()
        b6 = self.fonk2()
        if not b6:
            print("There is no path.")
        else:
            b5, path, g_cost, b11 = b6
            print("Path found:")
            print("Actions:", b5)
            print("Number of b3 nodes:", len(self.b3))
            print("Number of nodes in the closed list:", len(self.b2))
            print("Maximum memory used:", self.a1)
            print("Path cost:", g_cost)
if b19 = = "__main__":
    def fonk4():
        return "initial"
    def fonk5(b20):
        return ["action1", "action2"]
    def fonk6(b20, action):
        return f"{b20}_{action}"
    def fonk7(b20):
        return b20 = = "goal"
    def fonk8(state1, state2):
        return 1
    def fonk9(b20):
        return 0
    b21 = class1(b4, b5, b6, b7, b8, b9)
    b21.fonk3()