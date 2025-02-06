import time
import joblib
from fetch_tweets import fetch_tweets
from preprocess import clean_tweet

# Load the trained model and vectorizer
model = joblib.load("data/sentiment_model.pkl")
vectorizer = joblib.load("data/vectorizer.pkl")

def predict_sentiment(text):
    """
    Predict the sentiment of a tweet.
    """
    cleaned_text = clean_tweet(text)
    text_vector = vectorizer.transform([cleaned_text])
    prediction = model.predict(text_vector)
    return "Positive" if prediction[0] == 1 else "Negative"

def real_time_sentiment_analysis(keyword, interval=60):
    """
    Fetch and analyze tweets in real time.
    """
    while True:
        print(f"Fetching tweets for '{keyword}'...")
        tweets = fetch_tweets(keyword, count=50)
        for tweet in tweets:
            sentiment = predict_sentiment(tweet)
            print(f"Tweet: {tweet}\nSentiment: {sentiment}\n")
        print(f"Waiting for {interval} seconds...\n")
        time.sleep(interval)

if __name__ == "__main__":
    real_time_sentiment_analysis("Cowboy Carter")