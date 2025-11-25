import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
from scipy.stats import pearsonr


def preprocess_news(news_df):
    news_df["date"] = pd.to_datetime(news_df["date"], utc=True, errors='coerce').dt.date
    news_df = news_df.dropna(subset=["date"])
    news_df["sentiment"] = news_df["headline"].apply(lambda x: TextBlob(str(x)).sentiment.polarity)
    daily_sentiment = news_df.groupby("date")["sentiment"].mean().reset_index()
    daily_sentiment.columns = ["date", "avg_sentiment"]
    return daily_sentiment

def preprocess_stock(stock_df):
    stock_df["date"] = pd.to_datetime(stock_df["Date"], format="%m/%d/%Y", errors='coerce').dt.date
    stock_df = stock_df.dropna(subset=["date"])
    stock_df.sort_values("date", inplace=True)
    stock_df["return"] = stock_df["Close"].pct_change()
    return stock_df[["date", "Close", "return"]]


def merge_and_correlate(stock_df, sentiment_df, company_name="Company"):
    """
    Merge sentiment and stock data, calculate correlation, and plot.
    """
    merged = pd.merge(stock_df, sentiment_df, on="date", how="inner").dropna()

    if len(merged) < 2:
        print(f"⚠️ Not enough overlapping data between sentiment and stock for {company_name}.")
        print("Sentiment date range:", sentiment_df["date"].min(), "-", sentiment_df["date"].max())
        print("Stock date range:", stock_df["date"].min(), "-", stock_df["date"].max())
        print("Overlap size:", pd.merge(stock_df, sentiment_df, on="date", how="inner").shape[0])
        return None, merged

    correlation, p_value = pearsonr(merged["avg_sentiment"], merged["return"])

    print(f"\n📊 Correlation for {company_name}: {correlation:.4f} (p={p_value:.4f})")

    plt.figure(figsize=(10, 4))
    plt.scatter(merged["avg_sentiment"], merged["return"], alpha=0.6)
    plt.title(f"Sentiment vs Stock Return: {company_name}")
    plt.xlabel("Average Daily Sentiment")
    plt.ylabel("Daily Return")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    return correlation, merged