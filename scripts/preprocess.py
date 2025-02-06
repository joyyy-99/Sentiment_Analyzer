import re
import string
from nltk.corpus import stopwords
import nltk


nltk.download('stopwords')

def clean_tweet(tweet):
    """
    Clean a tweet by removing URLs, mentions, hashtags, punctuation, and stopwords.
    """
    
    tweet = re.sub(r"http\S+|www\S+|https\S+", "", tweet, flags=re.MULTILINE)
    
    tweet = re.sub(r"@\w+|#\w+", "", tweet)
    
    tweet = tweet.translate(str.maketrans("", "", string.punctuation))
    
    tweet = tweet.lower()
    
    stop_words = set(stopwords.words("english"))
    tweet = " ".join([word for word in tweet.split() if word not in stop_words])
    return tweet

if __name__ == "__main__":
    # Test the cleaning function
    tweet = "Cowboy Carter is a MASTERPIECE! 🔥 Beyoncé really delivered with this one. Best album of the year! #CowboyCarter #Beyoncé https://open.spotify.com/album/6BzxX6zkDsYKFJ04ziU5xQ"
    print(f"Original: {tweet}")
    print(f"Cleaned: {clean_tweet(tweet)}")