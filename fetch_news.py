from dotenv import load_dotenv
import os
import requests

load_dotenv()

api_key = os.getenv("NEWS_API_KEY")
BASE_URL = "https://newsapi.org/v2/everything"

topic = ["technology", "sports", "politics", "entertainment", "health", "science", "business"]

def fetch_news(topic: str):
    params = {
        "q": topic,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": 5,
        "apiKey": api_key
    }
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    data = response.json()
    return data["articles"]

def clean_articles(raw_articles):
    # Fixed: Returns a LIST of all cleaned articles instead of just the last one
    return [
        {
            "title": article.get("title", "No Title"),
            "description": article.get("description", "No Description"),
            "url": article.get("url", ""),
            "publishedAt": article.get("publishedAt", "")
        }
        for article in raw_articles
    ]

def fetch_all_news():
    all_news = {}
    for t in topic:
        raw_articles = fetch_news(t)
        cleaned_articles = clean_articles(raw_articles)
        all_news[t] = cleaned_articles  # Maps topic -> list of 5 cleaned articles
    return all_news

if __name__ == "__main__":
    all_news = fetch_all_news()
    
    # Fixed: Count total articles across all categories
    total_articles = sum(len(articles) for articles in all_news.values())
    print(f"Fetched {total_articles} articles total\n")
    
    # Fixed: Loop through the dictionary items (topic_name, list_of_articles)
    for category, articles in all_news.items():
        print(f"--- Category: {category.upper()} ---")
        for article in articles:
            print(f"- {article['title']}")
            print(f" Description: {article['description']}")
        print() # Adds a blank line between categories