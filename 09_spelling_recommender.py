from nltk.corpus import words
from difflib import get_close_matches
import nltk
nltk.download('words')

def spell_corrector(word):
    vocab = words.words()
    return get_close_matches(word, vocab, n=3)

print("Suggestions:", spell_corrector("appl"))