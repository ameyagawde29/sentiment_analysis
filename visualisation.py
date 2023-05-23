import matplotlib.pyplot as plt

def visualise_sentiment(analyzed_tweets):
    sentiment_count = {"Positive": 0, "Negative": 0, "Neutral": 0}
    for tweet in analyzed_tweets:
        sentiment_count[tweet["sentiment"]] += 1

    labels = sentiment_count.keys()
    counts = sentiment_count.values()

    plt.bar(labels, counts)
    plt.xlabel("Sentiment")
    plt.ylabel("Count")
    plt.title("Sentiment Analysis of Tweets")
    plt.show()