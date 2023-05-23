import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def preprocess_tweet(tweet):
    cleaned_tweet = re.sub(r"http\S+|@\S+|#[A-Za-z0-9]+", "", tweet)

    tokens = word_tokenize(cleaned_tweet)

    stop_words = set(stopwords.words("english"))
    filtered_tokens = [token.lower() for token in tokens if token.lower() not in stop_words]

    return filtered_tokens