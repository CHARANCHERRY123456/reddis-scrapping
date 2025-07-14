import argparse
import os

from reddit_scrapper import extract_username, fetch_user_data
from persona_generator import chunk_text, generate_persona


def main():
    parser = argparse.ArgumentParser(description="Reddit User Persona Generator")
    parser.add_argument(
        '--url',
        required=True,
        help="Reddit user profile URL (e.g., https://www.reddit.com/user/kojied/)"
    )
    args = parser.parse_args()

    try:
        username = extract_username(args.url)
        print(f"[+] Extracted username: u/{username}")

        user_data = fetch_user_data(username)
        print(f"[+] Fetched {len(user_data['posts'])} posts and {len(user_data['comments'])} comments")

        chunks = chunk_text(user_data)
        print(f"[+] Split into {len(chunks)} chunks for LLM")

        persona_text = generate_persona(chunks)

        output_dir = "output"
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, f"{username}.txt")

        with open(output_path, "w", encoding="utf-8") as file:
            file.write(persona_text)

        print(f"[✅] Persona saved to {output_path}")

    except Exception as e:
        print(f"[❌] An error occurred: {e}")
        print("Please ensure the URL and environment setup are correct.")


if __name__ == "__main__":
    main()
