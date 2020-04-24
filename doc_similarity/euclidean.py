import matplotlib.pyplot as plt
import numpy as np

def euclidean(x,y):   
    return np.sqrt(np.sum((x-y)**2))

doc1 = [1, 0]
doc2 = [0, 6]
doc3 = [1, 2]

nu_doc1 = np.array(doc1)
nu_doc2 = np.array(doc2)
nu_doc3 = np.array(doc3)

one_three = euclidean(nu_doc1, nu_doc3)
two_three = euclidean(nu_doc2, nu_doc3)

print('document1 document3 거리비교:', one_three)
print('document2 document3 거리비교:', two_three)

a = plt.scatter([doc1[0], doc2[0], doc3[0]], [doc1[1], doc2[1], doc3[1]])
plt.xlabel('phone')
plt.ylabel('book')
plt.show()