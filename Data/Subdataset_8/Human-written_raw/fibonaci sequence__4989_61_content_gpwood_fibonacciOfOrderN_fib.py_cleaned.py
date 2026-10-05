class fibbonacci(object):
   def __init__(self,fibtype=2, stop=10):
      self.steps = 0
      self.ratio = 0
      self.fibtype = fibtype
      self.stop = stop
      self.previous = [1, 1]
   def fibbonacci(self):
      if self.stop  == self.steps:
        print(f"Ratio {self.fibtype}: {self.ratio}")
        return
      else:
        mysum = sum(self.previous)
        self.ratio = mysum/self.previous[-1]
        self.steps = self.steps + 1
        if len(self.previous) >= self.fibtype:
           newarray = self.previous[slice(len(self.previous)+1-self.fibtype,len(self.previous))]
           newarray.append(mysum)
           self.previous = newarray
        else:
           self.previous.append(mysum)
        self.fibbonacci()
if __name__ == "__main__":
   for i in range(55):
      myfib = fibbonacci(i,54)
      myfib.fibbonacci()