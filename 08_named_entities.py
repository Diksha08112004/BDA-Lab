import nltk
from nltk import ne_chunk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

nltk.download('maxent_ne_chunker')
nltk.download('words')

text = "Barack Obama was the 44th President of the United States"
tokens = word_tokenize(text)
tags = pos_tag(tokens)
tree = ne_chunk(tags)
tree.draw()