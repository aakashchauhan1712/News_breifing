import os
from dotenv import load_dotenv
from fetch_news import fetch_all_news
from summarizer import main as generate_summary  # assuming your previous script is named summarizer.py
from email_sender import send_news_email

load_dotenv()

if __name__ == "__main__":
    # 1. Fetch raw articles from NewsAPI
    print("Step 1: Fetching news from API...")
    raw_news = fetch_all_news()
    
    # 2. Send the dictionary to Gemini for summarizing
    print("Step 2: Generating AI summaries...")
    ai_summary = generate_summary(raw_news)
    
    # 3. Email the results to the user
    print("Step 3: Preparing email dispatch...")
    user_email = "receiver_address@example.com"  # Change this to your test recipient address
    
    send_news_email(recipient_email=user_email, email_content=ai_summary)