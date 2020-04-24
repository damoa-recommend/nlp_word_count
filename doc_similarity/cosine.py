from numpy import dot
from numpy.linalg import norm
import numpy as np

def cos_sim(A, B):
       return dot(A, B)/(norm(A)*norm(B))


doc1 = [1, 0]
doc2 = [0, 6]
doc3 = [1, 2]

nu_doc1 = np.array(doc1)
nu_doc2 = np.array(doc2)
nu_doc3 = np.array(doc3)

one_three = cos_sim(nu_doc1, nu_doc3)
two_three = cos_sim(nu_doc2, nu_doc3)
three_three = cos_sim(nu_doc3, nu_doc3)

print('document1 document3 cosine:', one_three)
print('document2 document3 cosine:', two_three)
print('document3 document3 cosine:', three_three)
