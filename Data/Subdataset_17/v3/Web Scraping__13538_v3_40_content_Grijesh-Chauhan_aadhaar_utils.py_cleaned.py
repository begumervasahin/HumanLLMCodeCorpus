import os
from urllib.parse import urlparse, parse_qs, urlencode, unquote, parse_qsl, ParseResult
from json import dumps
def parse_query_params(url, flat=True):
    parsed_url = urlparse(url)
    parsed_params = parse_qs(parsed_url.query, strict_parsing=False)
    if flat:
        for key, value in parsed_params.items():
            if len(value) == 1:
                parsed_params[key] = value[0]
    return parsed_params
def add_url_params(url, params):
    url = unquote(url)
    parsed_url = urlparse(url)
    existing_params = dict(parse_qsl(parsed_url.query))
    existing_params.update(params)
    for key, value in existing_params.items():
        if isinstance(value, (bool, dict)):
            existing_params[key] = dumps(value)
    encoded_params = urlencode(existing_params, doseq=True)
    new_url = ParseResult(
        scheme=parsed_url.scheme,
        netloc=parsed_url.netloc,
        path=parsed_url.path,
        params=parsed_url.params,
        query=encoded_params,
        fragment=parsed_url.fragment
    ).geturl()
    return new_url
def filename_fix_existing(filename):
    dirname = '.'
    name, ext = filename.rsplit('.', 1)
    existing_files = [f for f in os.listdir(dirname) if f.startswith(name)]
    suffixes = [f.replace(name, '').strip(' .()') for f in existing_files]
    indexes = [int(suffix) for suffix in suffixes if suffix.isdigit()]
    idx = max(indexes, default=0) + 1
    return f'{name} ({idx}).{ext}'
if __name__ == "__main__":
    url = 'http:
    new_params = {'answers': False, 'data': ['some', 'values']}
    print(add_url_params(url, new_params))
    filename = 'example.txt'
    print(filename_fix_existing(filename))