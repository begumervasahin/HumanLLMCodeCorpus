import sys
from collections import defaultdict
import argparse
class Tree:
    def __init__(self, label, span, word=None, subs=None):
        assert (word is None) ^ (subs is None), f"Invalid tree: {label}, {word}, {subs}"
        self.label = label
        self.span = span
        self.word = word
        self.subs = subs
        self._str = None
        self._hash = None
    def is_terminal(self):
        return self.word is not None
    def __str__(self):
        if True or self._str is None:
            self._str = self._to_string()
        return self._str
    __repr__ = __str__
    def __hash__(self):
        if self._hash is None:
            self._hash = hash(str(self))
        return self._hash
    def _to_string(self):
        if self.is_terminal():
            return f"({self.label} {self.word})"
        else:
            return f"({self.label} {' '.join(map(str, self.subs))})"
    def span_width(self):
        return self.span[1] - self.span[0]
    def arity(self):
        return len(self.subs)
    def labelspan(self):
        return f"{self.label} [{self.span[0]}-{self.span[1]}]"
    def spanlabel(self):
        return f"[{self.span[0]}-{self.span[1]}]: {self.label}"
    @staticmethod
    def _parse(line, pos=0, word_index=0, trunc=True):
        assert line[pos] == '(', f"Tree must start with a '(': {line}, {pos}, {line[pos]}"
        empty = False
        space = line.find(" ", pos)
        label = line[pos + 1: space]
        if trunc:
            if label[0] != "-":
                for symbol in ["-", "=", "|"]:
                    dash_pos = label.find(symbol)
                    if dash_pos >= 0:
                        label = label[:dash_pos]
                        break
            else:
                if label == "-NONE-":
                    empty = True
        new_pos = space + 1
        new_index = word_index
        if line[new_pos] == '(':
            subtrees = []
            while line[new_pos] != ')':
                if line[new_pos] == " ":
                    new_pos += 1
                (new_pos, new_index), empty_node, subtree = Tree._parse(line, new_pos, new_index, trunc)
                if not empty_node:
                    subtrees.append(subtree)
            return (new_pos + 1, new_index), subtrees == [], Tree(label, (word_index, new_index), subs=subtrees)
        else:
            final_pos = line.find(")", new_pos)
            word = line[new_pos: final_pos]
            return (final_pos + 1, word_index + 1 if not empty else word_index), empty, Tree(label, (word_index, word_index + 1), word=word)
    @staticmethod
    def parse(line, trunc=False):
        _, is_empty, tree = Tree._parse(line, 0, 0, trunc)
        assert not is_empty, f"The whole tree is empty! {line}"
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
        label_span_count = defaultdict(int)
        for label_span in self.all_label_spans():
            label_span_count[label_span] += 1
        return label_span_count
    def pp(self, level=0):
        if not self.is_terminal():
            print(f"{'| ' * level}{self.labelspan()}")
            for sub in self.subs:
                sub.pp(level + 1)
        else:
            print(f"{'| ' * level}{self.labelspan()} {self.word}")
    def height(self, level=0):
        if self.is_terminal():
            return 1
        return max(sub.height() for sub in self.subs) + 1
    def binarize(self):
        if self.subs is not None and len(self.subs) > 2:
            new_label = self.label + "'" if self.label[-1] != "'" else self.label
            second_subtree = Tree(label=new_label, span=self.span, subs=self.subs[1:])
            self.subs = [self.subs[0], second_subtree]
            for child in self.subs:
                child.binarize()
    def de_binarize(self):
        if self.subs is not None:
            while self.subs[-1].label[-1] == "'":
                rhs_node = self.subs[-1]
                self.subs.pop()
                self.subs.extend(rhs_node.subs)
        if self.subs is not None:
            for child in self.subs:
                child.de_binarize()
    def get_productions(self):
        productions = []
        if self.subs is not None:
            if len(self.subs) == 2:
                child1, child2 = self.subs
                productions.append((self.label, f"{child1.label} {child2.label}"))
            elif len(self.subs) == 1:
                productions.append((self.label, self.subs[0].label))
            for child in self.subs:
                productions.extend(child.get_productions())
        elif self.word is not None:
            productions.append((self.label, self.word))
        return productions
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parse and manipulate Penn Treebank-style trees.")
    parser.add_argument("--max_len", type=int, default=400, help="maximum sentence length")
    parser.add_argument("--pp", action="store_true", help="pretty print")
    parser.add_argument("--height", action="store_true", help="output the height of each tree")
    parser.add_argument("--clean", action="store_true", help="clean up functional tags and empty nodes")
    args = parser.parse_args()
    for line in sys.stdin:
        tree = Tree.parse(line.strip(), trunc=args.clean)
        tree.binarize()
        if len(tree) <= args.max_len:
            if args.pp:
                tree.pp()
                print(tree)
            elif args.height:
                print(f"{len(tree)}\t{tree.height()}")
            else:
                print(tree)
        tree.de_binarize()
        if len(tree) <= args.max_len:
            if args.pp:
                tree.pp()
                print(tree)
            elif args.height:
                print(f"{len(tree)}\t{tree.height()}")
            else:
                print(tree)