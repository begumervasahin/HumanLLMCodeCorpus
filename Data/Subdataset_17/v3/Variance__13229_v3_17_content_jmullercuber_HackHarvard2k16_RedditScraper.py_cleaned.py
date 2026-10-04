import json
import http.client as httplib
import string
class Scraper:
    def get_documents(self, subreddit, qty):
        raise NotImplementedError("This method should be overridden.")
    def get_comments_for_post(self, link):
        raise NotImplementedError("This method should be overridden.")
    def recurse_comments(self, comment):
        raise NotImplementedError("This method should be overridden.")
class RedditScraper(Scraper):
    def __init__(self):
        self.max_depth = 1
        self.current_depth = 0
    def get_documents(self, subreddit, qty):
        conn = httplib.HTTPSConnection('www.reddit.com')
        conn.request("GET", f"/r/{subreddit}/hot/.json")
        response = conn.getresponse()
        subreddit_data = json.loads(response.read())
        documents = []
        for i in range(min(qty, len(subreddit_data['data']['children']))):
            permalink = subreddit_data['data']['children'][i]['data']['permalink']
            documents.extend(self.get_comments_for_post(permalink))
        conn.close()
        return documents
    def get_comments_for_post(self, link):
        conn = httplib.HTTPSConnection('www.reddit.com')
        conn.request("GET", f"{link}.json?limit=500")
        response = conn.getresponse()
        post_data = json.loads(response.read())
        top_level_comments = post_data[1]['data']['children']
        all_comments = []
        for comment in top_level_comments:
            if 'body' in comment['data']:
                self.current_depth = 0
                all_comments.extend(self.recurse_comments(comment))
        conn.close()
        return all_comments
    def recurse_comments(self, comment):
        comment_bodies = []
        body = ''.join(filter(lambda x: x in string.printable, comment['data']['body']))
        comment_bodies.append(body)
        if comment['data'].get('replies') and self.current_depth < self.max_depth:
            for reply in comment['data']['replies']['data']['children']:
                if reply['kind'] != 'more':
                    self.current_depth += 1
                    comment_bodies.extend(self.recurse_comments(reply))
                    self.current_depth -= 1
        return comment_bodies
if __name__ == "__main__":
    scraper = RedditScraper()
    subreddit = "python"
    qty = 5
    documents = scraper.get_documents(subreddit, qty)
    for doc in documents:
        print(doc)