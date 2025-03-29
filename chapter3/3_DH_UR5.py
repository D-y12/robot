# 实验3：DH参数法计算UR5机器人的正运动学 
# 实验成员：052210424丁雨童
# 日期：2025.3.24
# 文件名：3_DH_UR5.py


import numpy as np
import roboticstoolbox as rtb
from spatialmath import SE3

# TODO: 根据机器人构型尺寸，完善如下DH参数列表
a = [0, -0.425, -0.39225, 0, 0, 0]
d = [0.089159, 0, 0, 0.10915, 0.09465, 0.0823]
alpha =[np.pi/2, 0, 0, np.pi/2, -np.pi/2, 0]
# 根据DH参数，生成坐标变换矩阵链
links =[]
for j in range(6):
    link =rtb.RevoluteDH(d=d[j], a=a[j], alpha=alpha[j])
    links.append(link)
 # 将矩阵连乘，并代入关节角数值，计算运动学正解
T = SE3(np.eye(4))
q1 = np.array([180, 0, 0, 0, 90, 0]) *np.pi/180
for q, l in zip(q1, links):
     T = T * l.A(q)
print(T)

# 创建UR5机器人对象
robot = rtb.models.DH.UR5()
# 利用rtb库计算机器人的正向运动学

T1 = robot.fkine(q1)
print(T1)


