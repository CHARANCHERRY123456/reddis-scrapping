import argparse
from reddit_scrapper import extract_username , fetch_user_data


def main():
    parser = argparse.ArgumentParser(description="Reddit User Data Fetcher")
    parser.add_argument('--url' , required=True, help="Reddit user profile URL(e.g., https://www.reddit.com/user/kojied/)")
    args = parser.parse_args()

    try:
        username = extract_username(args.url)
        user_data = fetch_user_data(username)
        print("fetcheduser data : ", user_data)
        # llm persona generation part
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please ensure the URL is correct and try again.")
if __name__ == "__main__":
    main()