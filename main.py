from twitter_api import TwitterAPI
from preprocessing import preprocess_tweet
from sentiment_analysis import SentimentAnalysis
from visualization import Visualization

def main():
    twitter_api = TwitterAPI()

    search_query = "your search query"
    tweets = twitter_api.search_tweets(search_query, count=100)
    
    preprocessed_tweets = [preprocess_tweet(tweets) for tweet in tweets]

    sentinment_analyser = SentimentAnalyzer()
    analyzed_tweets = sentiment_analyser.analyze_sentiment(preprocessed_tweet)

    visualize_sentiment(analyzed_tweets)

if __name__ == "__main__":
    main()
