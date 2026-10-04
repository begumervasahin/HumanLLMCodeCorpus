from prf import *
from pairs import *
from lists import *
from dicts import *
a1 = 0
a2 = 1
a3 = 2
b1 = LIST(
    0,
    LIST(2, 3),
    LIST(
        pair(pair(0, 1), LIST(1, 1, a3)),
        pair(pair(0, 2), LIST(0, 2, a3)),
        pair(pair(1, 1), LIST(0, 1, a3)),
        pair(pair(1, 2), LIST(1, 2, a3)),
        pair(pair(0, 0), LIST(2, 0, a1)),
        pair(pair(1, 0), LIST(3, 0, a1)),
    ),
)
b2 = C(list3, C(Getter(0), Proj(2, 0)), Zero(2), Proj(2, 1))
def fonk1(b25):
    state, b4, b3 = UNLIST(b25)
    b4 = UNLIST(b4)
    b3 = UNLIST(b3)
    b5 = f'[{state}] {" ".join(reversed(list(map(str, b4))))} > {" ".join(map(str, b3))}'
    print(b5)
b6 = C(pair, Getter(0), C(head, Getter(2)))
b7 = C(lookup, C(Getter(2), Proj(2, 0)), C(b6, Proj(2, 1)))
b8 = C(list3, Getter(0), C(tail, Getter(1)), C(cons, C(head, Getter(1)), Getter(2)))
b9 = C(list3, Getter(0), C(cons, C(head, Getter(2)), Getter(1)), C(tail, Getter(2)))
b10 = C(cond,
                 C(eq, Proj(2, 1), Constant(a2, 2)),
                 C(b8, Proj(2, 0)),
                 C(cond,
                   C(eq, Proj(2, 1), Constant(a3, 2)),
                   C(b9, Proj(2, 0)),
                   Proj(2, 0)
                   )
                 )
b11 = C(list3,
                  C(Getter(0), Proj(2, 0)),
                  C(Getter(1), Proj(2, 0)),
                  C(cons, Proj(2, 1), C(tail, C(Getter(2), Proj(2, 0))))
                  )
b12 = C(list3,
                      Proj(2, 1),
                      C(Getter(1), Proj(2, 0)),
                      C(Getter(2), Proj(2, 0))
                      )
b13 = C(b10,
                         C(b11,
                           C(b12,
                             Proj(2, 0),
                             C(Getter(0), Proj(2, 1))
                             ),
                           C(Getter(1), Proj(2, 1))
                           ),
                         C(Getter(2), Proj(2, 1))
                         )
b14 = C(b13, Proj(2, 1), b7)
b15 = C(contains, C(Getter(1), Proj(2, 0)), Proj(2, 1))
b16 = C(b15, Proj(2, 0), C(Getter(0), Proj(2, 1)))
b17 = C(cond, b16, Proj(2, 1), b14)
b18 = PR(Proj(2, 1), C(b17, Proj(4, 2), Proj(4, 0)))
b19 = C(b18, Proj(3, 2), Proj(3, 0), Proj(3, 1))
b20 = Minimize(C(not_, C(b16, Proj(3, 1), C(b19, Proj(3, 1), Proj(3, 2), Proj(3, 0)))))
b21 = C(b19, Proj(2, 0), Proj(2, 1), b20)
b22 = C(b21, Proj(2, 0), b2)
if b23 = = '__main__':
    b24 = LIST(1, 1, 2, 2, 1)
    b25 = b2(b1, b24)
    fonk1(b25)
    while not b16(b1, b25):
        b25 = b17(b1, b25)
        fonk1(b25)
    fonk1(b22(b1, b24))