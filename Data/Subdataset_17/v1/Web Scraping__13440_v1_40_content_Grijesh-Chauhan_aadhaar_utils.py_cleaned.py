import os
from urllib.parse import urlparse, parse_qs, urlencode, unquote, parse_qsl, ParseResult
from json import dumps
def parse_query_params(url, flat=True):
    parsed_url = urlparse(url)
    parsed_params = parse_qs(parsed_url.query, strict_parsing=False)
    if flat:
        for key in parsed_params:
            value = parsed_params[key]
            parsed_params[key] = value[0] if len(value) == 1 else value
    return parsed_params
def add_url_params(url, params):
    url = unquote(url)
    parsed_url = urlparse(url)
    get_args = parsed_url.query
    parsed_get_args = dict(parse_qsl(get_args))
    parsed_get_args.update(params)
    parsed_get_args.update(
        {k: dumps(v) for k, v in parsed_get_args.items()
         if isinstance(v, (bool, dict))}
    )
    encoded_get_args = urlencode(parsed_get_args, doseq=True)
    new_url = ParseResult(
        parsed_url.scheme, parsed_url.netloc, parsed_url.path,
        parsed_url.params, encoded_get_args, parsed_url.fragment
    ).geturl()
    return new_url
def filename_fix_existing(filename):
    dirname = '.'
    name, ext = filename.rsplit('.', 1)
    names = [x for x in os.listdir(dirname) if x.startswith(name)]
    names = [x.rsplit('.', 1)[0] for x in names]
    suffixes = [x.replace(name, '') for x in names]
    suffixes = [x[2:-1] for x in suffixes
                   if x.startswith(' (') and x.endswith(')')]
    indexes  = [int(x) for x in suffixes
                   if set(x) <= set('0123456789')]
    idx = 1
    if indexes:
        idx += sorted(indexes)[-1]
    return '%s (%d).%s' % (name, idx, ext)
url = 'http:
new_params = {'answers': False, 'data': ['some', 'values']}
print(add_url_params(url, new_params))
filename = 'example.txt'
print(filename_fix_existing(filename))