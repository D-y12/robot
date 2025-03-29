# 2-1-2.py
# 实验成员：052210424丁雨童
#写一个 Python 函数，实现 SO2 的构造功能，并使用 spatialmath 库中的函数进行验证。


from spatialmath import *
from spatialmath.base import *
import math
import numpy as np

#构建二维旋转矩阵的函数
def SO2_hand(th):
    return(np.array([[math.cos(th),-math.sin(th)]
                  ,[math.sin(th),math.cos(th)]]))

R=SO2_hand(math.pi/4)  
R2=SO2(math.pi/4)  #调用spatialmath库生成生成旋转矩阵

 #判断两个矩阵在数值上是否足够接近
if np.allclose(R, R2):
    print('功能验证成功')  




