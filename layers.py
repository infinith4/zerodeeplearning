import numpy as np
import sys,os
sys.path.append(os.curdir)
from common.functions import *

class Relu:
    def __init__(self):
        self.mask = None
    def forward(self,x):
        self.mask = (x <= 0)
        out = x.copy()
        out[self.mask] = 0
        return out
    def backward(self, dout):
        dout[self.mask]=0
        dx = dout
        return dx
class Affine:
    def __init__(self,W,b):
        self.W = W
        self.b = b
        self.x = None
        self.dw = None
        self.db = None
    def forward(self,x):
        self.x = x
        out = np.dot(x,self.W) + self.b
        return out
    def backward(self,dout):
        dx = np.dot(dout,self.W.T)
        self.dw = np.dot(self.x.T,dout)
        self.db = np.sum(dout,axis=0)
        return dx
class SoftmaxWithLoss:
    def __init__(self):
        self.loss = None
        self.y = None
        self.t = None
    def forward(self,x,t):
        self.t = t
        self.y = softmax(x)
        self.loss = cross_entropy_errror(self.y,self.t)
        return self.loss
    def backward(self,dout=1):
        batch_size=self.t.shape[0]
        dx=(self.x-self.t)/batch_size
        return dx

x = np.array([[1.0,-0.5],[-2.0,3.0]])
print(x)

mask = (x <= 0)
print(mask)
