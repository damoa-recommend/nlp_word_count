doc1 = "apple banana everyone like likey watch card holder"
doc2 = "apple banana coupon passport love you"

tokenized_doc1 = doc1.split()
tokenized_doc2 = doc2.split()

set_doc1 = set(tokenized_doc1)
set_doc2 = set(tokenized_doc2)

union = set_doc1.union(set_doc2)
print('합집합: ', union)

intersection = set_doc1.intersection(set_doc2)
print('교집합: ', intersection)

print('jaccardd : ', len(intersection)/len(union))