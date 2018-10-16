from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()
data_corpus = ["John likes to watch movies. Mary likes movies too.",
"John also likes to watch football games."]
X = vectorizer.fit_transform(data_corpus)
print(X.toarray())
print(vectorizer.get_feature_names())

import collections,re
texts = ['John likes to watch movies. Mary likes too.','John also likes to watch football games.']
bagsofwords = [ collections.Counter(re.findall(r'\w+', txt)) for txt in texts]
# r'...' for raw string \w+ for string, ]w for single letter
sumbags = sum(bagsofwords, collections.Counter())
print(bagsofwords)
print(sumbags)