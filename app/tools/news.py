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

    url = f"https://api.thenewsapi.com/v1/news/top?api_token={NEWS_API_KEY}&locale=us&limit={number_of_news}"
    headers = {}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        news_data = response.json().get("data", [])
        articles = []

        for news_item in news_data:
            uuid = news_item.get("uuid", "")
            title = news_item.get("title", "Untitled")
            description = news_item.get("description", "No description available.")
            image_url = news_item.get("image_url", None)
            output_dir = './swarmzero-data/output/images/' + uuid
            image_path = os.path.join(output_dir, 'default.jpg')
            os.makedirs(output_dir, exist_ok=True)

            try:
                img_response = requests.get(image_url)
                if img_response.status_code == 200:
                    with open(image_path, 'wb') as img_file:
                        img_file.write(img_response.content)
                    print(f"Image saved to {image_path}")
                else:
                    print(f"Failed to download image from {image_url}")
                    image_path = None

            except Exception as e:
                print(f"Error downloading image: {e}")
                image_path = None

            articles.append({
                "uuid": uuid,
                "title": title,
                "description": description,
                "default_image": image_path
            })

        return articles
    else:
        print(f"Failed to fetch news: {response.status_code}")
        return []
