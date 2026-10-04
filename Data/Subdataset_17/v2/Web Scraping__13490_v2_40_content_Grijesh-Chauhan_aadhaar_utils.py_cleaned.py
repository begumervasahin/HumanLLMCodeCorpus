import os
from urllib.parse import urlparse, parse_qs, urlencode, unquote, parse_qsl, ParseResult
from json import dumps
def parse_query_params(url, flat=True):
    parsed_url = urlparse(url)
    parsed_params = parse_qs(parsed_url.query, strict_parsing=False)
    if flat:
        for key, value in parsed_params.items():
            parsed_params[key] = value[0] if len(value) == 1 else value
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
        parsed_url.scheme,
        parsed_url.netloc,
        parsed_url.path,
        parsed_url.params,
        encoded_params,
        parsed_url.fragment
    ).geturl()
    return new_url
def filename_fix_existing(filename):
    dirname = '.'
    name, ext = filename.rsplit('.', 1)
    existing_files = [x for x in os.listdir(dirname) if x.startswith(name)]
    existing_names = [x.rsplit('.', 1)[0] for x in existing_files]
    suffixes = [x.replace(name, '') for x in existing_names]
    suffixes = [x[2:-1] for x in suffixes if x.startswith(' (') and x.endswith(')')]
    indexes = [int(x) for x in suffixes if x.isdigit()]
    idx = max(indexes, default=0) + 1
    return f'{name} ({idx}).{ext}'
if __name__ == "__main__":
    url = 'http:
    new_params = {'answers': False, 'data': ['some', 'values']}
    print(add_url_params(url, new_params))
    filename = 'example.txt'
    print(filename_fix_existing(filename))