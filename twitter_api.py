import tweepy

class TwitterAPI:
    def __init__(self):
        consumer_key = "your consumer key"
        consumer_secret = "your consumer secret"
        access_token = "your access token"
        access_token_secret = "your access token secret"

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def search_tweets(self, query, count=100):
        tweets = []
        try:
            search_results = self.api.search(q=query, count=count)
            tweets = [tweet.text for tweet in search_results]
        except tweepy.TweepError as e:
            print(f"Error Occured: {e}")
        return tweets
