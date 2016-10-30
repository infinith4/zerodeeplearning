import sys,os
sys.path.append(os.curdir)
import numpy as np
from dataset.mnist import load_mnist
from twolayernet import TwoLayerNet

(x_train,t_train),(x_test,t_test) = load_mnist(normalize=True)
network = TwoLayerNet(input_size=784,hidden_size=50,output_size=10)
x_batch = x_train[:3]
t_batch = t_train[:3]

grad_numerical = network.numerical_gradient(x_batch,t_batch)
grad_backprop = network.gradient(x_batch,t_batch)

for key in grad_numerical.keys():
    diff = np.average(np.abs(grad_backprop[key]-grad_numerical[key]))
    print(key + ":" + str(diff))
# W2:8.40451683671e-13
# b2:1.20126125713e-10
# b1:1.03517937278e-12
# W1:2.2455573235e-13

# b2:1.20570220474e-10
# W2:1.00584997791e-12
# b1:9.83043057763e-13
# W1:2.68616411544e-13
