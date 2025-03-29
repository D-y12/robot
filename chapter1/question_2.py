#question_2.py
#在a坐标系下坐标为(1,2),在b坐标系下坐标为(4,-2),用python表示

from spatialmath import *
from spatialmath.base import *
import math
import numpy as np


a=np.array([1,2])  #在{a}坐标系下的坐标
print(a)
R=SE2(6,-3,math.pi/2)  #在{b}坐标系下的坐标
b=R*a
print(b.reshape(1,-1))