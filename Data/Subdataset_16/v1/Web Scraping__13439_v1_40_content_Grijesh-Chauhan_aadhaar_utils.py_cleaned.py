import os
from urllib.parse import urlparse, parse_qs, urlencode, unquote, parse_qsl, ParseResult
from json import dumps
def fonk1(b5, b1 = True):
    b2 = urlparse(b5)
    b3 = parse_qs(b2.query, strict_parsing=False)
    if b1:
        for key in b3:
            b4 = b3[key]
            b3[key] = b4[0] if len(b4) == 1 else b4
    return b3
def fonk2(b5, params):
    b5 = unquote(b5)
    b2 = urlparse(b5)
    b6 = b2.query
    b7 = dict(parse_qsl(b6))
    b7.update(params)
    b7.update(
        {k: dumps(v) for k, v in b7.items()
         if isinstance(v, (bool, dict))}
    )
    b8 = urlencode(b7, doseq=True)
    b9 = ParseResult(
        b2.scheme, b2.netloc, b2.path,
        b2.params, b8, b2.fragment
    ).geturl()
    return b9
def fonk3(b16):
    b10 = '.'
    name, b11 = b16.rsplit('.', 1)
    b12 = [x for x in os.listdir(b10) if x.startswith(name)]
    b12 = [x.rsplit('.', 1)[0] for x in b12]
    b13 = [x.replace(name, '') for x in b12]
    b13 = [x[2:-1] for x in b13
                   if x.startswith(' (') and x.endswith(')')]
    b14 = [int(x) for x in b13
                   if set(x) <= set('0123456789')]
    a1 = 1
    if b14:
        a1 += sorted(b14)[-1]
    return '%s (%d).%s' % (name, a1, b11)
b5 = 'http:
b15 = {'answers': False, 'data': ['some', 'values']}
print(fonk2(b5, b15))
b16 = 'example.txt'
print(fonk3(b16))