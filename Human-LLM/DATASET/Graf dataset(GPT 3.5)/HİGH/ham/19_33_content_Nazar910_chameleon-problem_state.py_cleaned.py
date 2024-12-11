33. Repository: Nazar910/chameleon-problem
   File: state.py
   URL: https:
   Code Content:
from collections import deque
class class1():
    def fonk1(self, **chameleon_count):
        self.b1 = chameleon_count['b9']
        self.b2 = chameleon_count['b10']
        self.b3 = chameleon_count['b11']
        self.b4 = None
    @property
    def fonk2(self):
        return self.b1
    @property
    def fonk3(self):
        return self.b3
    @property
    def fonk4(self):
        return self.b2
    @property
    def fonk5(self):
        return self.b4
    @b12.setter
    def fonk6(self, obj):
        self.b4 = obj
    def fonk7(self):
        return bool(self.b1)
    def fonk8(self):
        return self.fonk7() and not self.fonk9() and not self.fonk11()
    def fonk9(self):
        return bool(self.b2)
    def fonk10(self):
        return self.fonk9() and not self.fonk7() and not self.fonk11()
    def fonk11(self):
        return bool(self.b3)
    def fonk12(self):
        return self.fonk11() and not self.fonk9() and not self.fonk7()
    def fonk13(self):
        return self.fonk12() or self.fonk10() or self.fonk8()
    def fonk14(self):
        if self.b1 < 1 or self.b2 < 1:
            raise Exception('Invalid b10 or b9 count')
        b5 = self.b1 - 1
        b6 = self.b2 - 1
        b7 = self.b3 + 2
        b8 = class1(
            b9 = b5,
            b10 = b6,
            b11 = b7
        )
        b8.b12 = self
        return b8
    def fonk15(self):
        if self.b3 < 1 or self.b2 < 1:
            raise Exception('Invalid b10 or b11 count')
        b5 = self.b1 + 2
        b6 = self.b2 - 1
        b7 = self.b3 - 1
        b8 = class1(
            b9 = b5,
            b10 = b6,
            b11 = b7
        )
        b8.b12 = self
        return b8
    def fonk16(self):
        if self.b1 < 1 or self.b3 < 1:
            raise Exception('Invalid b11 or b9 count')
        b5 = self.b1 - 1
        b6 = self.b2 + 2
        b7 = self.b3 - 1
        b8 = class1(
            b9 = b5,
            b10 = b6,
            b11 = b7
        )
        b8.b12 = self
        return b8
    def fonk17(self):
        b13 = deque([str(self)])
        b12 = self.b12
        while b12:
            b13.appendleft(str(b12))
            b12 = b12.b12
        return b13
    def fonk18(self):
        return '(b9 = {},b10={},b11={})'.format(self.b5, self.b6, self.b7)
   README Content:
project for solving "Chameleon problem" (and also for getting some experience in Python).
```
On the Sebur island lived chameleons. There were 13 b9, 16 b10 and 17 b11 ones.
In case when two chameleons of different colors met, they change their color to
another (e.g. was one b9 and one b10 - they became two b11 chameleons).
Is it possible for all chameleons to become one color?
```
For representing state of the chameleons on the island I created a `class1` class (see [here](https:
It has usefull methods like checking if all chameleons already of one color or create new state like red_met_blue() which returns new state object with updated chameleons count.
To solve "chameleons problem" I used three graph traversing algorithms:
- depth first search DFS ([implementation](https:
- breadth first search BFS ([implementation](https:
- A* algorithm (A star) ([implementation](https:
You can check that all works by running tests.
Run one:
```fish
python a_star.test.py
```
Or launching all of them (fish shell example)
```fish
bash -c './run_tests.sh'
```
for bash or zsh use
```bash
./run_tests.sh
```
So, what are the results. All three algorithms found state (b9 = 0, b10=46, b11=0) as the state where all chameleons have one color.
About algorithms:
- DFS is the easiest for the understanding and I suppose for the implementation. But it mostly depends on your luck to find the right state (so in 93 step it found final state with b13 of 89 steps see [test](https:
- BFS is much nicer because it garantees to find the shortest b13 and it found one in 17 steps (see [test](https:
- A* is the most difficult for understanding of the 3 algoritthms but it is the most effective one. It uses [cost](https:
