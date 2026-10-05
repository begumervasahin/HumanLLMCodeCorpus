def record_user_click(index, keyword, url):
    urls = lookup_keyword(index, keyword)
    if urls:
        for entry in urls:
            if entry[0] == url:
                entry[1] += 1
def lookup_keyword(index, keyword):
    for entry in index:
        if entry[0] == keyword:
            return entry[1]
    return None
def add_to_index(index, keyword, url):
    for entry in index:
        if entry[0] == keyword:
            for url_entry in entry[1]:
                if url_entry[0] == url:
                    return
            entry[1].append([url, 0])
            return
    index.append([keyword, [[url, 0]]])
def get_page(url):
    return ''
def union(a, b):
    for e in b:
        if e not in a:
            a.append(e)
def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote
def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links
def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    index = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index, page, content)
            union(tocrawl, get_all_links(content))
            crawled.append(page)
    return index
def add_page_to_index(index, url, content):
    words = content.split()
    for word in words:
        add_to_index(index, word, url)
index = crawl_web('http:
print(lookup_keyword(index, 'good'))
record_user_click(index, 'good', 'http:
print(lookup_keyword(index, 'good'))
record_user_click(index, 'good', 'http:
print(lookup_keyword(index, 'good'))