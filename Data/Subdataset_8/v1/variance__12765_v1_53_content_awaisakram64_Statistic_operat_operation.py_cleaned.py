class Functions:
    def Median(self, data):
        ln = len(data)
        data = sorted(data)
        if ln % 2 == 0:
            return (data[ln
        else:
            return data[ln
    def Mode(self, data):
        dic = {}
        for i in set(data):
            dic[i] = data.count(i)
        x = max(dic.values())
        if x <= 1:
            return [0]
        else:
            return [key for key, val in dic.items() if val == x]
    def Mean(self, data):
        return sum(data) / len(data)
    def Variance(self, data):
        mean = self.Mean(data)
        return sum([(i - mean) ** 2 for i in data]) / len(data)
    def StaDev(self, data):
        return (self.Variance(data)) ** 0.5
def main():
    func = Functions()
    with open("data.txt", 'r') as file:
        data = [float(line.strip()) for line in file]
    print('Median is %.2f' % (func.Median(data)))
    print('Mean is %.2f' % (func.Mean(data)))
    print('Mode is ' + (', '.join(map(str, [i for i in func.Mode(data)]))))
    print('Variance is %.2f' % (func.Variance(data)))
    print('Standard Dev is %.2f' % (func.StaDev(data)))
if __name__ == "__main__":
    main()