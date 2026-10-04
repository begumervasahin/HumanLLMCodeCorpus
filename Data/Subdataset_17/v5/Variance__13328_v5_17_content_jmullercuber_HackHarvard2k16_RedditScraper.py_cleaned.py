import json
import http.client
import string
from Scraper import Scraper
class RedditScraper(Scraper):
    BASE_URL = 'www.reddit.com'
    def __init__(self):
        self.depth = 0
    def get_documents(self, subreddit, qty):
        subreddit_data = self._fetch_subreddit_data(subreddit)
        documents = []
        for i in range(qty):
            permalink = subreddit_data['data']['children'][i]['data']['permalink']
            documents.extend(self.get_comments_for_post(permalink))
        return documents
    def get_comments_for_post(self, permalink):
        post_data = self._fetch_post_data(permalink)
        top_level_comments = post_data[1]['data']['children']
        all_comments = []
        for comment in top_level_comments:
            if 'body' in comment['data']:
                self.depth = 0
                all_comments.extend(self._recurse_comments(comment))
        return all_comments
    def _recurse_comments(self, comment):
        comment_bodies = []
        body = ''.join(filter(lambda x: x in string.printable, comment['data']['body']))
        comment_bodies.append(body)
        if comment['data']['replies'] and self.depth < 1:
            for reply in comment['data']['replies']['data']['children']:
                if reply['kind'] != 'more':
                    self.depth += 1
                    comment_bodies.extend(self._recurse_comments(reply))
        return comment_bodies
    def _fetch_subreddit_data(self, subreddit):
        conn = http.client.HTTPSConnection(self.BASE_URL)
        conn.request("GET", f"/r/{subreddit}/hot/.json")
        response = conn.getresponse()
        subreddit_data = json.loads(response.read())
        conn.close()
        return subreddit_data
    def _fetch_post_data(self, permalink):
        conn = http.client.HTTPSConnection(self.BASE_URL)
        conn.request("GET", f"{permalink}.json?limit=500")
        response = conn.getresponse()
        post_data = json.loads(response.read())
        conn.close()
        return post_data