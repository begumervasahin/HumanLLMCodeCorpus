import sys
import argparse
from collections import defaultdict
class Tree:
    def __init__(self, label, span, word=None, subs=None):
        assert (word is None) ^ (subs is None), \
            f"Invalid tree initialization with label: {label}, word: {word}, subs: {subs}"
        self.label = label
        self.span = span
        self.word = word
        self.subs = subs
        self._str = None
        self._hash = None
    def is_terminal(self):
        return self.word is not None
    def dostr(self):
        if self.is_terminal():
            return f"({self.label} {self.word})"
        else:
            return f"({self.label} {' '.join(map(str, self.subs))})"
    def __str__(self):
        if self._str is None:
            self._str = self.dostr()
        return self._str
    __repr__ = __str__
    def __hash__(self):
        if self._hash is None:
            self._hash = hash(str(self))
        return self._hash
    def __eq__(self, other):
        return str(self) == str(other)
    def span_width(self):
        return self.span[1] - self.span[0]
    __len__ = span_width
    def arity(self):
        return len(self.subs)
    def labelspan(self):
        return f"{self.label} [{self.span[0]}-{self.span[1]}]"
    def spanlabel(self):
        return f"[{self.span[0]}-{self.span[1]}]: {self.label}"
    @staticmethod
    def _parse(line, pos=0, wrdidx=0, trunc=True):
        assert line[pos] == '(', f"Tree must start with '(': {line} at position {pos}"
        space = line.find(" ", pos)
        label = line[pos + 1: space]
        if trunc and label != "-NONE-":
            for delimiter in "-=|":
                label = label.split(delimiter)[0]
        newpos = space + 1
        newidx = wrdidx
        if line[newpos] == '(':
            subtrees = []
            while line[newpos] != ')':
                if line[newpos] == " ":
                    newpos += 1
                (newpos, newidx), empty, sub = Tree._parse(line, newpos, newidx, trunc)
                if not empty:
                    subtrees.append(sub)
            return (newpos + 1, newidx), subtrees == [], Tree(label, (wrdidx, newidx), subs=subtrees)
        else:
            finalpos = line.find(")", newpos)
            word = line[newpos: finalpos]
            return (finalpos + 1, wrdidx + 1), False, Tree(label, (wrdidx, wrdidx + 1), word=word)
    @staticmethod
    def parse(line, trunc=False):
        _, is_empty, tree = Tree._parse(line, 0, 0, trunc)
        assert not is_empty, "The entire tree is empty! " + line
        if tree.label != "TOP":
            tree = Tree(label="TOP", span=tree.span, subs=[tree])
        return tree
    def all_label_spans(self):
        if self.is_terminal():
            return []
        label_spans = [(self.label, self.span)]
        for sub in self.subs:
            label_spans.extend(sub.all_label_spans())
        return label_spans
    def label_span_counts(self):
        counts = defaultdict(int)
        for label_span in self.all_label_spans():
            counts[label_span] += 1
        return counts
    def pretty_print(self, level=0):
        if not self.is_terminal():
            print(f"{'| ' * level}{self.labelspan()}")
            for sub in self.subs:
                sub.pretty_print(level + 1)
        else:
            print(f"{'| ' * level}{self.labelspan()} {self.word}")
    def height(self):
        if self.is_terminal():
            return 1
        return max(sub.height() for sub in self.subs) + 1
    def binarize(self):
        if self.subs:
            if len(self.subs) > 2:
                new_label = f"{self.label}'" if self.label[-1] != "'" else self.label
                self.subs = [self.subs[0], Tree(label=new_label, span=self.span, subs=self.subs[1:])]
            for sub in self.subs:
                sub.binarize()
    def deBinarize(self):
        if self.subs:
            while self.subs[-1].label.endswith("'"):
                rhs_node = self.subs.pop()
                self.subs.extend(rhs_node.subs)
            for sub in self.subs:
                sub.deBinarize()
    def get_productions(self):
        productions = []
        if self.subs:
            if len(self.subs) == 2:
                productions.append((self.label, f"{self.subs[0].label} {self.subs[1].label}"))
            elif len(self.subs) == 1:
                productions.append((self.label, self.subs[0].label))
            for sub in self.subs:
                productions.extend(sub.get_productions())
        elif self.word:
            productions.append((self.label, self.word))
        return productions
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some trees.')
    parser.add_argument('--max_len', type=int, default=400, help='Maximum sentence length')
    parser.add_argument('--pp', action='store_true', help='Pretty print the tree')
    parser.add_argument('--height', action='store_true', help='Output the height of each tree')
    parser.add_argument('--clean', action='store_true', help='Clean up functional tags and empty nodes')
    args = parser.parse_args()
    for line in sys.stdin:
        tree = Tree.parse(line.strip(), trunc=args.clean)
        tree.binarize()
        if len(tree) <= args.max_len:
            if args.pp:
                tree.pretty_print()
                print(tree)
            elif args.height:
                print(f"{len(tree)}\t{tree.height()}")
            else:
                print(tree)
        tree.deBinarize()
        if len(tree) <= args.max_len:
            if args.pp:
                tree.pretty_print()
                print(tree)
            elif args.height:
                print(f"{len(tree)}\t{tree.height()}")
            else:
                print(tree)