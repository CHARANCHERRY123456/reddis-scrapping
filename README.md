
# ✅ Project Title: Reddit User Persona Generator

Generate a structured user persona from any Reddit profile using scraped posts/comments and LLM-powered analysis (via Gemini API). This tool extracts behavior, interests, personality traits, motivations, and frustrations — complete with cited Reddit content.

---

## 🚀 Features

* ✅ Scrapes posts & comments from public Reddit profiles using `praw`
* ✅ Generates a structured persona with age, occupation, personality, interests, etc.
* ✅ Uses Google Gemini LLM (`gemini-2.0-flash`) to create natural language summaries
* ✅ Cites the original content used for inference
* ✅ Output saved as `.txt` (can be extended to `.md`)
* ✅ Clean modular structure, PEP-8 styled, scalable

---

## 🛠️ Full Installation Guide (For Fresh Laptops)

### 1. 📦 Install Python (if not installed)

* **Windows**:
  Download and install Python 3.10+ from [python.org](https://www.python.org/downloads/windows/).
  During install, check ✅ "Add Python to PATH".

* **Ubuntu/Debian**

  ```bash
  sudo apt update
  sudo apt install python3 python3-pip
  ```

* **macOS**

  ```bash
  brew install python
  ```

---

### 2. 🧬 Clone This Repo

```bash
git clone https://github.com/<your-username>/reddit-persona-generator.git
cd reddit-persona-generator
```

---

### 3. 🌱 Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate.bat       # Windows
```

---

### 4. 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 5. 🔑 Setup API Keys (Gemini + Reddit)

1. Create `.env` file:

```bash
cp .env.example .env
```

2. Get a **Google Gemini API Key**

   * Go to: [https://makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)
   * Add to `.env`:

```
GEMINI_API_KEY=your_key_here
GEMINI_MODEL=gemini-2.0-flash
```

3. Get Reddit API credentials from [https://www.reddit.com/prefs/apps](https://www.reddit.com/prefs/apps)

   * Add these to `.env`:

```
REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_secret
REDDIT_USER_AGENT=script by <your name>
```

---

## ▶️ How to Run

```bash
python main.py --url https://www.reddit.com/user/kojied/
```

* Output will be saved at `output/kojied.txt`

---

## 📁 Folder Structure

```
reddit-persona-generator/
│
├── main.py                    # Entry point
├── reddit_scraper.py         # Reddit data fetcher using PRAW
├── persona_generator.py      # Chunking + LLM persona creation
├── requirements.txt
├── .env.example              # Sample .env
├── output/                   # Output text files
└── README.md
```

---

## 📄 Sample Output Snippet

```txt
- Age: Late 20s - Early 30s
- Occupation: iOS Developer
- Location: New York City
- Traits: Enthusiastic, proactive, conversational
- Motivations: Prefers convenience, values innovation
- Subreddits: r/VisionPro, r/nba, r/newyorkcity
- Frustrations: Annoyed by intern bar crowd, tech limitations
- Personality: Extroverted, tech-savvy, forward-thinking
- Citations: [Post 1lykkqf], [Comment 1alf7av]
```

---

## ✅ Requirements

* Python 3.10+
* Reddit API (via PRAW)
* Gemini API key (`gemini-2.0-flash` or `gemini-1.5-pro`)
* Internet access

---

## 💡 Customization

* 💬 Add Markdown output in `persona_generator.py`
* 📊 Add subreddit frequency stats (Phase 4+)
* 🧠 Switch Gemini model in `.env` (`GEMINI_MODEL`)
* 📥 Save full JSON snapshots of Reddit profile (optional enhancement)

---

## 🤝 License

This repository is submitted as part of a take-home assignment for BeyondChats Internship. Do not use without permission.

---

## 🙋‍♂️ Questions?

Raise an issue or message me directly on [Internshala] or [LinkedIn](https://www.linkedin.com/in/your-name).
