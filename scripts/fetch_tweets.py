import tweepy

# Replace with your Bearer Token
BEARER_TOKEN = "YOUR_BEARER_TOKEN"


client = tweepy.Client(bearer_token=BEARER_TOKEN)

def fetch_tweets(keyword, count=10):
    """
    Fetch tweets containing a keyword using the v2 API.
    """
    try:
        
        response = client.search_recent_tweets(
            query=keyword,  
            max_results=count,  
            tweet_fields=["text"],  
            expansions=["author_id"],  
            user_fields=["username"],  
        )

        
        if response.data:
            tweets = [tweet.text for tweet in response.data]
        else:
            tweets = []

    except tweepy.TweepyException as e:
        print(f"Error fetching tweets: {e}")
        tweets = []

    return tweets

if __name__ == "__main__":
    keyword = "Cowboy Carter"
    tweets = fetch_tweets(keyword, count=50)
    for tweet in tweets:
        print(tweet)