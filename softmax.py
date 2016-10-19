import numpy as np

def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a -c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y

a = np.array([1010,1000,990])
print(np.exp(a) / np.sum(np.exp(a)))
print(softmax(a))

# softmax.py:11: RuntimeWarning: overflow encountered in exp
#   print(np.exp(a) / np.sum(np.exp(a)))
# softmax.py:11: RuntimeWarning: invalid value encountered in true_divide
#   print(np.exp(a) / np.sum(np.exp(a)))
# [ nan  nan  nan]
# [  9.99954600e-01   4.53978686e-05   2.06106005e-09]