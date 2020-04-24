import matplotlib.pyplot as plt
import numpy as np

def softmax(a) :
    exp_a = np.exp(a)
    sum_exp_a = np.sum(exp_a)
    return exp_a / sum_exp_a

y = np.array([4, 5.0, 6.0, 7.0, 10.0])
softmaxed = softmax(y)

print('소프트맥스 취하기 전:', y)
print('소프트맥스 취한 후', softmaxed)
print('소프트맥스 결과 합', np.sum(softmaxed))

plt.scatter([1, 2, 3, 4, 5], softmaxed)
plt.show()