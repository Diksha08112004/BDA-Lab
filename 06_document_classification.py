from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

docs = ["spam offer free win", "hello friend", "free coupons available"]
labels = ["spam", "ham", "spam"]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(docs)

clf = MultinomialNB()
clf.fit(X, labels)

test = ["free offer for you"]
X_test = vectorizer.transform(test)
print("Prediction:", clf.predict(X_test))
