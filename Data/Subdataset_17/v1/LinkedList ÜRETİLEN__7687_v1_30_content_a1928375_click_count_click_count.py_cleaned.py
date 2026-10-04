def record_user_click(index, keyword, url):
    urls = lookup(index, keyword)
    if urls:
        for entry in urls:
            if entry[0] == url:
                entry[1] = entry[1] + 1
def lookup(index, keyword):
    for entry in index:
        if entry[0] == keyword:
            return entry[1]
    return None
def add_to_index(index, keyword, url):
    for entry in index:
        if entry[0] == keyword:
            for urls in entry[1]:
                if urls[0] == url:
                    return
            entry[1].append([url, 0])
            return
    index.append([keyword, [[url, 0]]])
def get_page(url):
    try:
        if url == "http:
            return '''<html> <body> This is a test page for learning to crawl!
<p> It is a good idea to
<a href="http:
learn to crawl</a> before you try to
<a href="http:
<a href="http:
        elif url == "http:
            return '''<html> <body> I have not learned to crawl yet, but I am
quite good at  <a href="http:
</body> </html>'''
        elif url == "http:
            return '''<html> <body> I can't get enough
<a href="http:
        elif url == "http:
            return '<html><body>The magic words are Squeamish Ossifrage!</body></html>'
    except:
        return ""
    return ""
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
print(lookup(index, 'good'))
record_user_click(index, 'good', 'http:
print(lookup(index, 'good'))
record_user_click(index, 'good', 'http:
print(lookup(index, 'good'))