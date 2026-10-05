import sys
from collections import defaultdict
class Tree:
    def __init__(self, label, span, word=None, subs=None):
        assert (word is None) ^ (subs is None), "Invalid tree structure"
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
    def _parse_tree(line, pos=0, word_index=0, trunc=True):
        assert line[pos] == '(', "Tree must start with a '('"
        empty = False
        space_index = line.find(" ", pos)
        label = line[pos + 1: space_index]
        if trunc:
            if label[0] != "-":
                dash_pos = label.find("-")
                if dash_pos >= 0:
                    label = label[:dash_pos]
                dash_pos = label.find("=")
                if dash_pos >= 0:
                    label = label[:dash_pos]
                dash_pos = label.find("|")
                if dash_pos >= 0:
                    label = label[:dash_pos]
            else:
                if label == "-NONE-":
                    empty = True
        new_pos = space_index + 1
        new_word_index = word_index
        if line[new_pos] == '(':
            subtrees = []
            while line[new_pos] != ')':
                if line[new_pos] == " ":
                    new_pos += 1
                (new_pos, new_word_index), emp, sub = Tree._parse_tree(line, new_pos, new_word_index, trunc)
                if not emp:
                    subtrees.append(sub)
            return (new_pos + 1, new_word_index), subtrees == [], Tree(label, (word_index, new_word_index), subs=subtrees)
        else:
            final_pos = line.find(")", new_pos)
            word = line[new_pos: final_pos]
            return (final_pos + 1, word_index + 1 if not empty else word_index), empty, Tree(label, (word_index, word_index + 1), word=word)
    @staticmethod
    def parse(line, trunc=False):
        _, is_empty, tree = Tree._parse_tree(line, 0, 0, trunc)
        assert not is_empty, "The whole tree is empty! " + line
        if tree.label != "TOP":
            tree = Tree(label="TOP", span=tree.span, subs=[tree])
        return tree
