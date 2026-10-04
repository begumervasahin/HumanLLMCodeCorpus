"""
Created on Mon Feb  5 13:50:13 2018
@author:
"Given a string of English text and a paragraph width,
design an algorithm to break the texts into lines not
exceeding the paragraph width, and not too jagged."
"""
from itertools import product, combinations
class Lines:
    def __init__(self, raw="", width=80):
        self.raw = raw
        self.width = width
        self.borders = []
        self.linebreaks = []
        self.bf = set()
        self.tz = set()
    def find_borders(self):
        for i in range(len(self.raw)):
            if not self.raw[i].isspace():
                if i == 0 or self.raw[i - 1].isspace():
                    self.borders.append(i)
                if self.borders and i - self.borders[-1] > self.width:
                    print(f"\"{self.raw[self.borders[-1]:i + 1]}\" is longer than the allowed line width {self.width}.")
                    print("Please consider adjusting the line width.")
                    self.borders = []
        self.borders.append(len(self.raw))
    def break_text_into_lines(self):
        self.find_borders()
        lines = ['']
        d = 0
        offset = 0
        for b in self.borders:
            if b - offset < self.width:
                lines[-1] += self.raw[d:b]
            else:
                lines.append(self.raw[d:b])
                offset = d
            d = b
        print([len(l) for l in lines])
        return lines
    def find_next_linebreak(self, p, reversed=False):
        if not reversed:
            if p == len(self.borders) - 1: return None
            i, j = p, len(self.borders) - 1
            sign = 1
        else:
            if p == 0: return None
            i, j = 0, p
            sign = -1
        while i < j:
            m = (i + j)
            if self.borders[m - 1] <= self.borders[p] + sign * self.width <= self.borders[m]:
                p = m - 1 * (not reversed)
                break
            elif self.borders[m] > self.borders[p] + sign * self.width:
                j = m
            else:
                i = m
        return p
    def find_linebreaks(self):
        front_push, back_push = [], []
        p = 0
        while p is not None and p <= len(self.borders):
            front_push.append((p, self.borders[p]))
            p = self.find_next_linebreak(p)
        p = len(self.borders) - 1
        while p is not None and p >= 0:
            back_push.append((p, self.borders[p]))
            p = self.find_next_linebreak(p, reversed=True)
        min_cost = float('inf')
        possible_ranges = [range(back[0], front[0] + 1) for back, front in zip(back_push[::-1], front_push)]
        for scenario in product(*possible_ranges):
            cost = 0
            for k in range(1, len(scenario)):
                diff = self.borders[scenario[k]] - self.borders[scenario[k - 1]]
                if diff > self.width:
                    cost = float('inf')
                    break
                else:
                    cost += (self.width - diff) ** 2
            if cost < min_cost:
                min_cost = cost
                self.linebreaks = [self.borders[k] for k in scenario]
        for b in range(1, len(self.linebreaks)):
            print(self.raw[self.linebreaks[b - 1]:self.linebreaks[b]])
    def find_linebreaks_brute_force(self):
        borders = self.borders[1:-1]
        n = len(self.raw)
        min_cost = float('inf')
        for scenario in combinations(borders, n):
            cost = 0
            scenario = [0] + list(scenario) + [len(self.raw)]
            for k in range(1, len(scenario)):
                diff = scenario[k] - scenario[k - 1]
                if diff > self.width:
                    cost = float('inf')
                    break
                else:
                    cost += (self.width - diff) ** 2
            if cost < min_cost:
                min_cost = cost
                self.linebreaks = scenario
        for b in range(1, len(self.linebreaks)):
            print(self.raw[self.linebreaks[b - 1]:self.linebreaks[b]])
    def find_linebreaks_improved(self):
        pass
raw = "Try this: Given a string of English text and a paragraph width, design an algorithm to break the texts into lines not exceeding the paragraph width, and not too jagged."
lines = Lines(raw, 80)
lines.find_borders()
print(lines.borders)
lines.find_linebreaks_brute_force()
lines.find_linebreaks()