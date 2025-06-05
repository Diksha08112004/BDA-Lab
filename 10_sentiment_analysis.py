from textblob import TextBlob

text = "I love this product, it's amazing!"
blob = TextBlob(text)
print("Sentiment:", blob.sentiment)