#2-1-SO2.py
# 实验成员：052210424丁雨童
#spatialmath库功能验证

from spatialmath import *
from spatialmath.base import *
import math
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

#旋转功能
R0=SO2(0) 
R1=SO2(math.pi/2)  
R2=SO2(45,unit='deg')
#合成功能
R=R1*R2
print(R)

