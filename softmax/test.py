# numpy 이해

from numpy import dot
from numpy.linalg import norm

data1 = (1, 2)
data2 = (3, 4)

print(dot(data1, data2))
print(norm(data1))
print(norm(data2))