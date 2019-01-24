
import numpy as np

import os
import sys

cwd=os.getcwd()
print (cwd)
t =np.zeros((3,2),np.uint8)
t[0,1]=20
print (t)
t[0:2]=[10,30]
print(t)