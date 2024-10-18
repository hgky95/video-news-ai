import os
import requests
from dotenv import load_dotenv
from app.tools import text_to_speech

load_dotenv()
NEWS_API_KEY = os.getenv("NEWS_API_KEY")


def fetch_news(number_of_news=2):
    """
    Fetches news articles and prepares them for use by agents in a multi-agent system.

    Args:
        number_of_news (int): Number of news articles to fetch.

    Returns:
        list[dict]: A list of dictionaries containing the news article data for further processing.
    """
    # Fetch the news data (replace with actual API)
    url = "https://f3e74836-6f41-4a24-be68-d0de23251b88.mock.pstmn.io/news"  # Mock URL
    headers = {}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        news_data = response.json().get("data", [])
        articles = []

        for news_item in news_data:
            uuid = news_item.get("uuid", "")
            title = news_item.get("title", "Untitled")
            description = news_item.get("description", "No description available.")

            articles.append({
                "uuid": uuid,
                "title": title,
                "description": description
            })

        return articles
    else:
        print(f"Failed to fetch news: {response.status_code}")
        return []
