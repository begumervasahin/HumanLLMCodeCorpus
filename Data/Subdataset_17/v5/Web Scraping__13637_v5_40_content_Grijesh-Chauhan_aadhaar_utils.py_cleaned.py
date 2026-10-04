import os
from json import dumps
try:
    from urllib import urlencode, unquote
    from urlparse import urlparse, parse_qs, parse_qsl, ParseResult
except ImportError:
    from urllib.parse import (
        urlencode, unquote, urlparse, parse_qs, parse_qsl, ParseResult
    )
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
    for k, v in existing_params.items():
        if isinstance(v, (bool, dict)):
            existing_params[k] = dumps(v)
    encoded_params = urlencode(existing_params, doseq=True)
    new_url = ParseResult(
        parsed_url.scheme, parsed_url.netloc, parsed_url.path,
        parsed_url.params, encoded_params, parsed_url.fragment
    ).geturl()
    return new_url
def filename_fix_existing(filename):
    dirname = '.'
    name, ext = filename.rsplit('.', 1)
    existing_names = [x.rsplit('.', 1)[0] for x in os.listdir(dirname) if x.startswith(name)]
    suffixes = [x[len(name):][2:-1] for x in existing_names if x.startswith(f'{name} (') and x.endswith(')')]
    indexes = [int(x) for x in suffixes if x.isdigit()]
    idx = 1 + max(indexes) if indexes else 1
    return f'{name} ({idx}).{ext}'