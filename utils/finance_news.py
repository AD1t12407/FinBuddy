import requests
import datetime
import sqlite3
import streamlit as st

# Function to display financial information



def display_financial_news():
    st.subheader("Financial News")
    st.write("Here are some recent financial news articles:")
    news_articles = get_news()
    if news_articles:
        for article in news_articles:
            st.write(f"- [{article['title']}]({article['url']})")
    else:
        st.write("Unable to fetch financial news at the moment.")
# Set up financial news API key
news_api_key = "9c364d44f202437fa167782d1d075057"

# Function to get financial news
def get_news():
    try:
        today = datetime.date.today()
        response = requests.get(
            f"https://newsapi.org/v2/everything?q=finance&from={today}&sortBy=publishedAt&apiKey={news_api_key}"
        )
        data = response.json()
        articles = data.get('articles', [])
        return articles
    except Exception as e:
        return []
    

def financial_news():
    get_news()
    display_financial_news()


