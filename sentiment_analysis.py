from textblob import TextBlob

class SentimentAnalyzer:
    def analyze_sentiment(self, tweets):
        analyzed_tweets = []
        for tweet in tweets:
            analysis = TextBlob(tweet)
            polarity = analysis.sentiment.polarity
            subjectivity = analysis.sentiment.subjectivity

            if polarity > 0:
                sentiment = "Positive"
            elif polarity < 0:
                sentiment = "Negative"
            else:
                sentiment = "Neutral"
            
            analyzed_tweets.append({
                "tweet": tweet,
                sentiment: sentiment,
                "polarity": polarity,
                subjectivity: subjectivity
            })
        return analyzed_tweets