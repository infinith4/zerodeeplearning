import numpy as np

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
        self.x None
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

x = np.array([[1.0,-0.5],[-2.0,3.0]])
print(x)

mask = (x <= 0)
print(mask)
