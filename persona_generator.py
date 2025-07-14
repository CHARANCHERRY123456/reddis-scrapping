import os
import google.generativeai as genai
from dotenv import load_dotenv
from typing import List, Dict

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model_name = os.getenv("GEMINI_MODEL", "gemini-2.0-flash")
MODEL = genai.GenerativeModel(model_name=model_name)


def prepare_prompt(chunks: List[str]) -> str:
    base = """
You are an expert LLM assistant. Given the Reddit user's raw content (posts and comments),
analyze and extract a **complete user persona**.

Structure your response like this:

- Name (if guessable):
- Age range:
- Occupation (if any hints):
- Status (e.g. Single, Married):
- Location (if available):
- Tier (e.g. Explorer, Follower):
- Archetype (e.g. Creator, Activist):

**Traits**
- Practical / Spontaneous / Active / Adaptable (use what fits)
- Hobbies and interests:
- Writing style / Tone:
- Personality (Introvert/Extrovert, etc):

**Motivations** (inferred):
- Convenience, Wellness, Speed, Preferences, Comfort, Dietary Needs

**Frustrations** (if any):
- e.g., Reddit complaints, tech issues, dislikes

**Behaviour & Habits**:
- Posting times, Subreddits, Topics they engage with

**Cite** each trait with a post/comment ID or exact text.

---

Text Chunks:
"""
    return base + "\n\n".join(chunks)


def chunk_text(data: Dict, chunk_size=8) -> List[str]:
    """Break user's comments/posts into chunks."""
    all_texts = []

    for post in data["posts"]:
        if post["body"].strip():
            all_texts.append(f"[Post {post['id']} from r/{post['subreddit']}]: {post['title']} — {post['body']}")

    for comment in data["comments"]:
        if comment["body"].strip():
            all_texts.append(f"[Comment {comment['id']} from r/{comment['subreddit']}]: {comment['body']}")

    chunks = [all_texts[i:i+chunk_size] for i in range(0, len(all_texts), chunk_size)]
    return ["\n\n".join(chunk) for chunk in chunks]


def generate_persona(chunks: List[str]) -> str:
    """Call Gemini API and return the full persona text."""
    responses = []
    for i, chunk in enumerate(chunks):
        prompt = prepare_prompt([chunk])
        response = MODEL.generate_content(prompt)
        if response.text:
            responses.append(response.text.strip())
    return "\n\n---\n\n".join(responses)
