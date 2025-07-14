import os
import re
import praw
from dotenv import load_dotenv

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT"),
)

def extract_username(url: str) -> str:
    """Extract Reddit username from profile URL."""
    match = re.search(r"reddit\.com/user/([A-Za-z0-9_-]+)/?", url)
    if not match:
        raise ValueError("Invalid Reddit user URL")
    return match.group(1)

def fetch_user_data(username: str, limit: int = 50) -> dict:
    """Fetch posts and comments by a Reddit user."""
    user = reddit.redditor(username)

    try:
        comments = [{
            "type": "comment",
            "id": comment.id,
            "subreddit": str(comment.subreddit),
            "body": comment.body,
            "score": comment.score,
            "url": f"https://www.reddit.com{comment.permalink}"
        } for comment in user.comments.new(limit=limit)]

        posts = [{
            "type": "post",
            "id": post.id,
            "subreddit": str(post.subreddit),
            "title": post.title,
            "body": post.selftext or "",
            "score": post.score,
            "url": f"https://www.reddit.com{post.permalink}"
        } for post in user.submissions.new(limit=limit)]

        return {
            "username": username,
            "comments": comments,
            "posts": posts
        }
    except Exception as e:
        raise RuntimeError(f"Failed to fetch data for u/{username}: {e}")
