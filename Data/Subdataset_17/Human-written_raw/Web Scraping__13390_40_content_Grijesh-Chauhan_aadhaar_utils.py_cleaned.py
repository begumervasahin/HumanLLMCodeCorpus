import urlparse
import os
from urlparse import urlparse, parse_qs
from json import dumps
try:
    from urllib import urlencode, unquote
    from urlparse import urlparse, parse_qsl, ParseResult
except ImportError:
    from urllib.parse import (
        urlencode, unquote, urlparse, parse_qsl, ParseResult
    )
def parse_query_paras(url, flat=True):
    parsed_url = urlparse(url)
    parsed_paras = parse_qs(parsed_url.query, strict_parsing=False)
    if flat:
        for key in parsed_paras:
            value = parsed_paras[key]
            parsed_paras[key] = value[0] if len(value) == 1 else value
    return parsed_paras
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
    dirname = u'.'
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