import os
import praw
from dotenv import load_dotenv

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT"),
)

user = reddit.redditor("spez")

for comment in user.comments.new(limit=5):
    print(f"{comment.subreddit} - {comment.body[:80]}...\n")
