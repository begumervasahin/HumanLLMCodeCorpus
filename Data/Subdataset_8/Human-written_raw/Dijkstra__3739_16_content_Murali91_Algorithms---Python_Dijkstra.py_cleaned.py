import collections
class dijkstra:
    def __init__(self,*args):
        self.nodes = list(args)
        self.result=dict.fromkeys(self.nodes,99999)
        self.edges=collections.defaultdict(str)
    def path(self,src,dest,dist):
        if src not in self.edges:
            self.edges[src]={}
        self.edges[src][dist]=dest
    def traverse(self,index,item):
        low =99999
        for key,value in item.iteritems():
            low=min(low,key)
            if self.result[value]== 99999 or self.result[value]> key+self.result[index]:
                self.result[value] = key+self.result[index]
        self.source = item[low]
    def calculate(self,source):
        self.source = source
        if self.source in self.edges:
            self.result[self.source] = 0
            i=0
            while i<=len(self.edges):
                for key,value in self.edges.iteritems():
                    if key == self.source or self.result[key]!=99999:
                        self.traverse(key,value)
                i+=1
        print self.result