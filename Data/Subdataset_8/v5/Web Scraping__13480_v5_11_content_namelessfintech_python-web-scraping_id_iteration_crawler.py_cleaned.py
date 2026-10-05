import itertools
import urllib.request
from urllib.error import URLError, HTTPError, ContentTooShortError
def download_page(url, num_retries=2, user_agent='wswp', charset='utf-8'):
    print('Downloading page:', url)
    request = urllib.request.Request(url)
    request.add_header('User-agent', user_agent)
    try:
        response = urllib.request.urlopen(request)
        content_charset = response.headers.get_content_charset() or charset
        html = response.read().decode(content_charset)
        return html
    except (URLError, HTTPError, ContentTooShortError) as e:
        print('Download error:', e.reason)
        if num_retries > 0 and hasattr(e, 'code') and 500 <= e.code < 600:
            return download_page(url, num_retries - 1)
    return None
def crawl_website(base_url, max_errors=5):
    num_errors = 0
    for page_number in itertools.count(1):
        page_url = f'{base_url}{page_number}'
        page_html = download_page(page_url)
        if page_html is None:
            num_errors += 1
            if num_errors == max_errors:
                print('Maximum consecutive errors reached. Exiting...')
                break
        else:
            num_errors = 0
crawl_website('http: