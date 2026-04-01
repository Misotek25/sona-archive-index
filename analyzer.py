# analyzer.py

import nltk
from collections import Counter
from textblob import TextBlob

nltk.download('punkt')

def analyze_word_frequency(text):
    """Analyze word frequency in the given text."""
    words = nltk.word_tokenize(text)
    word_freq = Counter(words)
    return word_freq.most_common()

def analyze_sentiment(text):
    """Analyze sentiment of the given text."""
    blob = TextBlob(text)
    return blob.sentiment

def extract_key_insights(text):
    """Extract key insights from the given SONA text data."""
    insights = {}
    insights['word_frequency'] = analyze_word_frequency(text)
    insights['sentiment'] = analyze_sentiment(text)
    return insights

# Example usage:
if __name__ == "__main__":
    sample_text = "Your SONA text goes here."
    insights = extract_key_insights(sample_text)
    print(insights)