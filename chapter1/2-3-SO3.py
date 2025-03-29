#2-3-SO3.py
# 实验成员：052210424丁雨童


from spatialmath import *
from spatialmath.base import *
import math
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


#实现三维旋转函数的功能
R0 = SO3(np.identity(3)) # 由3阶单位矩阵构造一个表示单位旋转矩阵
R1 = SO3.Rx(30, 'deg') # 构造一个绕x轴旋转30°的三维旋转矩阵
R2 = SO3.Ry(45, 'deg') # 构造一个绕y轴旋转0.1弧度的三维旋转矩阵
R3 = SO3.Rz(45, 'deg') # 构造一个绕z轴旋转45°的三维旋转矩阵
R = R1 * R2 * R3 # 将多个旋转矩阵进行合成
R.print() # 两种打印输出旋转矩阵的方式
R_rpy =SO3(rpy2r(30, 45,45 , unit="deg")) # 以RPY角的形式构造旋转矩阵
R_eul =SO3(eul2r(30, 45, 45, unit="deg")) # 以欧拉角的形式构造旋转矩阵
print(R_rpy)
print(R_eul)

#编写实现SO3构造函数功能的函数
def rx(thx):
    return(np.array([[1,0,0],
                 [0,math.cos(thx),-math.sin(thx)],
                 [0,math.sin(thx),math.cos(thx)]]))
def ry(thy):
    return(np.array([[math.cos(thy),0,math.sin(thy)],
                 [0,1,0],
                 [-math.sin(thy),0,math.cos(thy)]]))
def rz(thz):
    return(np.array([[math.cos(thz),-math.sin(thz),0],
                 [math.sin(thz),math.cos(thz),0],
                 [0,0,1]]))
def so3_struct(thx,thy,thz):
    R1 = SO3.Rx(thx) 
    R2 = SO3.Ry(thy) 
    R3 = SO3.Rz(thz) 
    x=rx(thx)
    y=ry(thy)
    z=rz(thz)
    R=np.dot(x,np.dot(y,z))
    if np.allclose(R1*R2*R3,R):
        print('SO3功能得到验证')



#用现有工具函数证明rpy2r与eul2r两个函数的旋转运动合成顺序。
def so3_rpy_euler(thx,thy,thz,a):
    if a=='rpy':
        Rx=rx(thx)
        Ry=ry(thy)
        Rz=rz(thz)
        R=np.dot(Rz,np.dot(Ry,Rx))
        print(R)
    if a=='euler':
        Rx=rz(thx)
        Ry=rx(thy)
        Rz=ry(thz)
        R=np.dot(Rx,np.dot(Ry,Rz))   
        print(R)

so3_struct(math.pi/6,math.pi/4,math.pi/3)
print("若选择RPY角计算则输入'rpy',若选择欧拉角计算则输入'euler',注：欧拉角采用zyx的计算方式")
a=input()
so3_rpy_euler(math.pi/6,math.pi/4,math.pi/4,a)