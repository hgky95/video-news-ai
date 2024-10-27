import os
import requests
from dotenv import load_dotenv

load_dotenv()
NEWS_API_KEY = os.getenv("NEWS_API_KEY")


def fetch_news(number_of_news=2, categories="sport"):
    """
    Fetches news articles based on the number of news and the categories from input

    Args:
        number_of_news (int): Number of news to fetch.
        categories: categories of news such as business/tech. Each category is separated by comma. For example, "business,tech"

    Returns:
        list[dict]: A list of dictionaries containing the news article data for further processing.
    """
    url = f"https://api.thenewsapi.com/v1/news/top?api_token={NEWS_API_KEY}&locale=us&limit={number_of_news}&categories={categories}"
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
