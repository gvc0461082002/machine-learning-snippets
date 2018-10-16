from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import nltk

data = "All work and no play makes jack dull boy. All work and no play makes jack a dull boy."
stopWords = set(stopwords.words('english'))
print(stopWords)
words = word_tokenize(data)
wordsFiltered = []

for w in words:
    if w not in stopWords:
        wordsFiltered.append(w)

print(wordsFiltered)
print(len(wordsFiltered))

from collections import Counter
list1=['apple','egg','apple','banana','egg','apple']
counts = Counter(list1)
print(counts)
# Counter({'apple': 3, 'egg': 2, 'banana': 1})