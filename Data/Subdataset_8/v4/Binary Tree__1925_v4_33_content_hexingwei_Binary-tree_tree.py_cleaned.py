import sys
from collections import defaultdict
class Tree:
    def __init__(self, label, span, wrd=None, subs=None):
        assert (wrd is None) ^ (subs is None), \
               "Invalid tree structure"
        self.label = label
        self.span = span
        self.word = wrd
        self.subs = subs
        self._str = None
        self._hash = None
    def is_terminal(self):
        return self.word is not None
    def __str__(self):
        if True or self._str is None:
            self._str = self._to_string()
        return self._str
    def __repr__(self):
        return self.__str__()
    def _to_string(self):
        if self.is_terminal():
            return f"({self.label} {self.word})"
        else:
            return f"({self.label} {' '.join(map(str, self.subs))})"
    def __hash__(self):
        if self._hash is None:
            self._hash = hash(str(self))
        return self._hash
    def __eq__(self, other):
        return str(self) == str(other)
    def span_width(self):
        return self.span[1] - self.span[0]
    def arity(self):
        return len(self.subs)
    def labelspan(self):
        return f"{self.label} [{self.span[0]}-{self.span[1]}]"
    def spanlabel(self):
        return f"[{self.span[0]}-{self.span[1]}]: {self.label}"
    @staticmethod
    def _parse(line, pos=0, wrdidx=0, trunc=True):
        assert line[pos] == '(', "Tree must start with a '('"
        empty = False
        space = line.find(" ", pos)
        label = line[pos + 1 : space]
        if trunc:
            if label[0] != "-":
                dashpos = label.find("-")
                if dashpos >= 0:
                    label = label[:dashpos]
                dashpos = label.find("=")
                if dashpos >= 0:
                    label = label[:dashpos]
                dashpos = label.find("|")
                if dashpos >= 0:
                    label = label[:dashpos]
            else:
                if label == "-NONE-":
                    empty = True
        newpos = space + 1
        newidx = wrdidx
        if line[newpos] == '(':
            subtrees = []
            while line[newpos] != ')':
                if line[newpos] == " ":
                    newpos += 1
                (newpos, newidx), emp, sub = Tree._parse(line, newpos, newidx, trunc)
                if not emp:
                    subtrees.append(sub)
            return (newpos + 1, newidx), subtrees == [], Tree(label, (wrdidx, newidx), subs=subtrees)
        else:
            finalpos = line.find(")", newpos)
            word = line[newpos : finalpos]
            return (finalpos + 1, wrdidx + 1 if not empty else wrdidx), empty, Tree(label, (wrdidx, wrdidx+1), wrd=word)
    @staticmethod
    def parse(line, trunc=False):
        _, is_empty, tree = Tree._parse(line, 0, 0, trunc)
        assert not is_empty, "The whole tree is empty! " + line
        if tree.label != "TOP":
            tree = Tree(label="TOP", span=tree.span, subs=[tree])
        return tree
    def all_label_spans(self):
        if self.is_terminal():
            return []
        a = [(self.label, self.span)]
        for sub in self.subs:
            a.extend(sub.all_label_spans())
        return a
    def label_span_counts(self):
        d = defaultdict(int)
        for a in self.all_label_spans():
            d[a] += 1
        return d
    def pp(self, level=0):
        if not self.is_terminal():
            print("| " * level, self.labelspan())
            for sub in self.subs:
                sub.pp(level+1)
        else:
            print("| " * level, self.labelspan(), self.word)
    def height(self, level=0):
        if self.is_terminal():
            return 1
        return max([sub.height() for sub in self.subs]) + 1
    def binarize(self):
        if self.subs is not None:
            if len(self.subs) > 2:
                newLabel = self.label
                if newLabel[-1] != "'":
                    newLabel += "'"
                t2 = Tree(label=newLabel, span=self.span, subs=self.subs[1:])
                self.subs = [self.subs[0], t2]
            for child in self.subs:
                child.binarize()
    def deBinarize(self):
        if self.subs is not None:
            while self.subs[-1].label[-1] == "'":
                rhsNode = self.subs[-1]
                rhsLabel = rhsNode.label
                if rhsLabel[-1] == "'":
                    self.subs.pop()
                    self.subs.extend(rhsNode.subs)
        if self.subs is not None:
            for child in self.subs:
                child.deBinarize()
    def getProductions(self):
        prods = []
        if self.subs is not None:
            if len(self.subs) == 2:
                child1 = self.subs[0]
                child2 = self.subs[1]
                prod = (self.label, f"{child1.label} {child2.label}")
                prods.append(prod)
            elif len(self.subs) == 1:
                prod = (self.label, self.subs[0].label)
                prods.append(prod)
            for child in self.subs:
                childProds = child.getProductions()
                prods.extend(childProds)
        elif self.word is not None:
            prod = (self.label, self.word)
            prods.append(prod)
        return prods
if __name__ == "__main__":
    max_len = 400
    pp = True
    height = False
    clean = False
    for i, line in enumerate(sys.stdin):
        t = Tree.parse(line.strip(), trunc=clean)
        t.binarize()
        if len(t) <= max_len:
            if pp:
                t.pp()
                print(t)
            elif height:
                print(f"{len(t)}\t{t.height()}")
            else:
                print(t)
        t.deBinarize()
        if len(t) <= max_len:
            if pp:
                t.pp()
                print(t)
            elif height:
                print(f"{len(t)}\t{t.height()}")
            else:
                print(t)