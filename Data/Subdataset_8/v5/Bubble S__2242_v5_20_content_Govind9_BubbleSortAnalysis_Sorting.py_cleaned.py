class SortingAnalyzer:
    def __init__(self):
        self.Qmoves = []
        self.Bmoves = []
        self.BBmoves = []
    def analyze(self):
        Q_total = sum(self.Qmoves)
        B_total = sum(self.Bmoves)
        BB_total = sum(self.BBmoves)
        print("Qsort\tBubble\tBetterBubble")
        for q, b, bb in zip(self.Qmoves, self.Bmoves, self.BBmoves):
            print(f"{q}\t{b}\t{bb}")
        print(f"{Q_total}\t{B_total}\t{BB_total}")
    def permute(self, x):
        arr = []
        if len(x) == len(self.s):
            p = "".join(self.s[int(i)] for i in x)
            for i in p:
                arr.append(int(i))
            self.sort(arr)
        for i in range(len(self.s)):
            if str(i) not in x:
                self.permute(x + str(i))
    def sort(self, arr):
        self.Bmoves.append(self.Bubble(arr))
        self.Qmoves.append(self.Qsort(arr))
        self.BBmoves.append(self.BetterBubble(arr))
        self.analyze()
    @staticmethod
    def Bubble(arr):
        moves = 0
        for j in range(len(arr)):
            moves += 3
            for i in range(len(arr) - 1 - j):
                moves += 2
                if arr[i] > arr[i + 1]:
                    moves += 2
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
        return moves
    @staticmethod
    def Qsort(arr):
        moves = 0
        for j in range(len(arr)):
            moves += 3
            swap = 0
            for i in range(len(arr) - 1 - j):
                moves += 2
                if arr[i] > arr[i + 1]:
                    moves += 2
                    swap += 1
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
            if swap < 2:
                break
        return moves
    @staticmethod
    def BetterBubble(arr):
        moves = 0
        for j in range(len(arr)):
            moves += 3
            flag = False
            for i in range(len(arr) - 1 - j):
                moves += 2
                if arr[i] > arr[i + 1]:
                    moves += 2
                    flag = True
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
            if not flag:
                break
        return moves
    def run_analysis(self):
        self.s = '123456'
        self.permute("")
if __name__ == "__main__":
    analyzer = SortingAnalyzer()
    analyzer.run_analysis()