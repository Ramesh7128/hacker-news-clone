from textblob import TextBlob

def calculate_sentiment(title):
    """
    Calculate Sentiment score for a given text
    
    Args:
        text: string,(title Hackernews)
    returns:
        sentiment score float.
    """
    title_sentiment = TextBlob(title)
    return title_sentiment.sentiment.polarity
