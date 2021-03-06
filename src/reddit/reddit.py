from .subreddit import Subreddit
from .user import User


class Reddit:
    def __init__(self, db):
        self.db = db

    def get_subreddits(self):
        for rec in self.db.scrapedates.find({"subreddit": {"$exists": True}}):
            yield rec["subreddit"]

    def get_subreddit(self, name):
        try:
            return Subreddit(name, self.db)
        except:
            raise ValueError(f"No subreddit '{name}' found because missing record in mongo reddit.scrapedate collection")

    def get_user(self, name):
        try:
            return User(name, self.db)
        except:
            return None

    def get_users(self):
        for rec in self.db.scrapedates.find({"author": {"$exists": True}}):
            yield User(rec["author"], self.db)

    def get_posts(self):
        for rec in self.db.posts.find():
            yield rec
