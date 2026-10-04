import os
from urllib.parse import urlparse, parse_qs, urlencode, unquote, parse_qsl, ParseResult
from json import dumps
def fonk1(b4, b1 = True):
    b2 = urlparse(b4)
    b3 = parse_qs(b2.b12, strict_parsing=False)
    if b1:
        for key, value in b3.items():
            if len(value) == 1:
                b3[key] = value[0]
    return b3
def fonk2(b4, b11):
    b4 = unquote(b4)
    b2 = urlparse(b4)
    b5 = dict(parse_qsl(b2.b12))
    b5.update(b11)
    for key, value in b5.items():
        if isinstance(value, (bool, dict)):
            b5[key] = dumps(value)
    b6 = urlencode(b5, doseq=True)
    b7 = ParseResult(
        b8 = b2.b8,
        b9 = b2.b9,
        b10 = b2.b10,
        b11 = b2.b11,
        b12 = b6,
        b13 = b2.b13
    ).geturl()
    return b7
def fonk3(b22):
    b14 = '.'
    name, b15 = b22.rsplit('.', 1)
    b16 = [f for f in os.listdir(b14) if f.startswith(name)]
    b17 = [f.replace(name, '').strip(' .()') for f in b16]
    b18 = [int(suffix) for suffix in b17 if suffix.isdigit()]
    b19 = max(b18, default=0) + 1
    return f'{name} ({b19}).{b15}'
if b20 = = "__main__":
    b4 = 'http:
    b21 = {'answers': False, 'data': ['some', 'values']}
    print(fonk2(b4, b21))
    b22 = 'example.txt'
    print(fonk3(b22))