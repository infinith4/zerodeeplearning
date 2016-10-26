# coding: utf-8
class MulLayer:
    def __init__(self):
        self.x = None
        self.y = None
    
    def forward(self, x,y):
        self.x = x
        self.y = y
        out = x*y
        return out
        
    def backward(self, dout):
        dx = dout * self.y # change x to y
        dy = dout * self.x # change x to y
        
        return dx,dy    

apple = 100
num=2
tax=1.1
mul_apple_layer = MulLayer()
mul_tax_layer = MulLayer()

apple_price = mul_apple_layer.forward(apple,num)
price = mul_tax_layer.forward(apple_price,tax)

print(price) #220

#backward
dprice = 1
dapple_price, dtax = mul_tax_layer.backward(dprice)
dapple,dapple_num = mul_apple_layer.backward(dapple_price)
print(dapple,dapple_num,dtax) #2.2 110.00000000000001 200
