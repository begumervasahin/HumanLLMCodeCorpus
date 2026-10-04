import os
from urllib.parse import urlparse, parse_qs, urlencode, unquote, parse_qsl, ParseResult
from json import dumps
def fonk1(b4, b1 = True):
    b2 = urlparse(b4)
    b3 = parse_qs(b2.query, strict_parsing=False)
    if b1:
        for key, value in b3.items():
            b3[key] = value[0] if len(value) == 1 else value
    return b3
def fonk2(b4, params):
    b4 = unquote(b4)
    b2 = urlparse(b4)
    b5 = dict(parse_qsl(b2.query))
    b5.update(params)
    for key, value in b5.items():
        if isinstance(value, (bool, dict)):
            b5[key] = dumps(value)
    b6 = urlencode(b5, doseq=True)
    b7 = ParseResult(
        b2.scheme,
        b2.netloc,
        b2.path,
        b2.params,
        b6,
        b2.fragment
    ).geturl()
    return b7
def fonk3(b17):
    b8 = '.'
    name, b9 = b17.rsplit('.', 1)
    b10 = [x for x in os.listdir(b8) if x.startswith(name)]
    b11 = [x.rsplit('.', 1)[0] for x in b10]
    b12 = [x.replace(name, '') for x in b11]
    b12 = [x[2:-1] for x in b12 if x.startswith(' (') and x.endswith(')')]
    b13 = [int(x) for x in b12 if x.isdigit()]
    b14 = max(b13, default=0) + 1
    return f'{name} ({b14}).{b9}'
if b15 = = "__main__":
    b4 = 'http:
    b16 = {'answers': False, 'data': ['some', 'values']}
    print(fonk2(b4, b16))
    b17 = 'example.txt'
    print(fonk3(b17))