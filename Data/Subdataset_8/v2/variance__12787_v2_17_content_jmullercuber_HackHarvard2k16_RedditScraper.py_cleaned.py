import json
import http.client
import string
class RedditScraper:
    def __init__(self):
        self.depth = 0
    def get_documents(self, subreddit, quantity):
        connection = http.client.HTTPSConnection('www.reddit.com')
        connection.request("GET", f"/r/{subreddit}/hot/.json")
        response = connection.getresponse()
        subreddit_data = response.read()
        subreddit_data = json.loads(subreddit_data)
        documents = []
        for i in range(quantity):
            post_permalink = subreddit_data['data']['children'][i]['data']['permalink']
            post_comments = self.get_comments_for_post(post_permalink)
            documents.extend(post_comments)
        connection.close()
        return documents
    def get_comments_for_post(self, post_link):
        connection = http.client.HTTPSConnection('www.reddit.com')
        connection.request("GET", f"{post_link}/.json?limit=500")
        response = connection.getresponse()
        post_data = response.read()
        post_data = json.loads(post_data)
        top_level_comments = post_data[1]['data']['children']
        all_comments = []
        for comment in top_level_comments:
            if 'body' in comment['data']:
                self.depth = 0
                comment_bodies = self.recurse_comments(comment)
                all_comments.extend(comment_bodies)
        connection.close()
        return all_comments
    def recurse_comments(self, comment):
        comment_bodies = []
        body = ''.join(filter(lambda x: x in string.printable, comment['data']['body']))
        comment_bodies.append(body)
        if 'replies' in comment['data'] and comment['data']['replies'] != '' and self.depth < 1:
            for reply in comment['data']['replies']['data']['children']:
                if 'kind' in reply and reply['kind'] != 'more':
                    self.depth += 1
                    reply_comments = self.recurse_comments(reply)
                    comment_bodies.extend(reply_comments)
        return comment_bodies
if __name__ == "__main__":
    reddit_scraper = RedditScraper()
    subreddit = 'Python'
    quantity = 3
    documents = reddit_scraper.get_documents(subreddit, quantity)
    for document in documents:
        print(document)