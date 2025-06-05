import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

text = "NLTK is a great library for NLP"
tokens = word_tokenize(text)
print("Tokens:", tokens)
print("POS Tags:", pos_tag(tokens))