#2-2-SE2.py
# 实验成员：052210424丁雨童


from spatialmath import *
from spatialmath.base import *
import math
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

#实现SE2的功能
T0 = SE2(0) # 构造一个单位二维变换矩阵
T1 = SE2([2, 3, math.pi /2]) # 构造一个变换矩阵，x=2,y=3, =pi/2
T2 = SE2([3, 1, -math.pi /4]) # 构造一个变换矩阵，x=3,y=1, =-pi/4
T = T1 * T2 # 将两个变换矩阵合成，构造出一个新的变换矩阵
# 图形绘制
fig1, ax1 =plt.subplots()
# 替换代码中的变量名，即可绘制不同变换矩阵， color参数为图形颜色， frame参数为坐标系名称
trplot2( np.array(T1.data)[0], color='blue',frame='A',ax=ax1)
trplot2( np.array(T2.data)[0], color='red',frame='B',ax=ax1)
trplot2( np.array(T.data)[0], color='green',frame='C',ax=ax1)
plt.grid(True) # 打开网格显示
plt.xlabel('Y')
plt.ylabel('X')
plt.show() 

#编写验证SE2的构造功能的函数
def SE2_strct(x,y,th):
    se2=np.array([[math.cos(th),-math.sin(th),x],
                 [math.sin(th),math.cos(th),y],
                 [0,0,1]])
    if np.allclose(se2,SE2(x,y,th)):  #判断构造函数是否和库中一致
        print('SE2的构造功能验证成功')
    else:
        print('SE2的构造功能验证失败')

#编写验证SE2的合成功能的函数
def SE2_compose(x1,y1,x2,y2,th1,th2):
    R1=np.array([[math.cos(th1),-math.sin(th1),x1],
                 [math.sin(th1),math.cos(th1),y1],
                 [0,0,1]])
    R2=np.array([[math.cos(th2),-math.sin(th2),x2],
                 [math.sin(th2),math.cos(th2),y2],
                 [0,0,1]])
    R=np.dot(R1,R2)
    R0=SE2(x1,y1,th1)*SE2(x2,y2,th2)
    if np.allclose(R,R0):  #判断构造的合成函数和库中的函数功能是否一致
        print('SE2的合成功能验证成功')
    else:
        print('SE2的合成功能验证失败')
    
SE2_strct(2,3,math.pi/3)
SE2_compose(1,2,3,4,math.pi/6,math.pi/4)