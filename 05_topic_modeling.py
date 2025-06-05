from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

docs = ["I love machine learning", "Deep learning and AI are future", "Python is great for data science"]
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(docs)

lda = LatentDirichletAllocation(n_components=2)
lda.fit(X)

for topic_idx, topic in enumerate(lda.components_):
    print(f"Topic #{topic_idx}:")
    print([vectorizer.get_feature_names_out()[i] for i in topic.argsort()[-3:]])