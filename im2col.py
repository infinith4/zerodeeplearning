import os, sys
sys.path.append(os.curdir)
from common.util import im2col
import numpy as np

x1 = np.random.rand(1,3,7,7)
col1 = im2col(x1,5,5,stride=1,pad=0)
print(col1.shape) #(9, 75)

x2 = np.random.rand(10,3,7,7)
col2 = im2col(x2,5,5,stride=1,pad=0)
print(col2.shape) #(90, 75)

