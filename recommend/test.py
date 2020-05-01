from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import json
import numpy as np

docs = [
  'you know I want your love',
  'I like you',
  'what should I do'
]

t = TfidfVectorizer(stop_words="english").fit(docs)
tfidfv = TfidfVectorizer(stop_words="english").fit_transform(docs)

print('[Word2Index]')
print(t.vocabulary_)
print()

print('[TF-IDF]')
print(tfidfv.toarray())
print()


print('[TF-IDF]')
print(tfidfv)
print()

print('[Cosin Similarity]')
cosine_sim = linear_kernel(tfidfv, tfidfv)

np.save('./c', cosine_sim)