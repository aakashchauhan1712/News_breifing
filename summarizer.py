from dotenv import load_dotenv
import os
import json  # Added to format the dictionary cleanly
from fetch_news import fetch_all_news
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

# Load env variables BEFORE initializing the LLM so it can find the key
load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7,
    google_api_key=os.getenv("GOOGLE_API_KEY") # Note: LangChain uses google_api_key or automatically reads GOOGLE_API_KEY from env
)

# Fixed: Added clear instructions on what the model should actually do
prompt = PromptTemplate(
    input_variables=["news_data"],
    template="""
You are an expert news summarizer. 

Below is a JSON object containing recent news articles categorized by topic. 
Please provide a concise, engaging bullet-point summary for each category. Highlight the most important stories.

News Data:
{news_data}

Summary:
"""
)

def main(news_data):
    # Fixed: Convert the Python dictionary into a clean, readable JSON string
    formatted_json = json.dumps(news_data, indent=2)
    
    # Format the prompt with the stringified data
    final_prompt = prompt.format(news_data=formatted_json)
    
    # Invoke the model
    response = llm.invoke(final_prompt)
    
    # langchain responses return an AIMessage object; .content extracts the raw string response
    return response.content

if __name__ == "__main__":
    print("Fetching news...")
    raw_news = fetch_all_news()
    
    print("Generating summaries via Gemini...")
    summary = main(raw_news)
    
    print("\n=== DAILY NEWS BRIEFING ===\n")
    print(summary)