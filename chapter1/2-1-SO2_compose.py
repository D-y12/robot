#2-1-SO2_compose.py
# 实验成员：052210424丁雨童
#编写一个 Python 函数，实现 SO2 的合成功能，并使用 spatialmath 库中的函数进行验证。

from spatialmath import *
from spatialmath.base import *
import math
import numpy as np


#构造合成函数
def compose(th1,th2):
    SO1=np.array([[math.cos(th1),-math.sin(th1)]
                  ,[math.sin(th1),math.cos(th1)]])
    SO2=np.array([[math.cos(th2),-math.sin(th2)]
                  ,[math.sin(th2),math.cos(th2)]])
    return(np.dot(SO1,SO2))

th1=math.pi/6
th2=math.pi/4
R1=compose(th1,th2)
R=SO2(th1)*SO2(th2)

if np.allclose(R,R1):
    print('合成功能验证成功')
else:
    print('合成功能验证失败')