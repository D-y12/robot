# 实验3：直线插补
# 实验成员：052210424丁雨童
# 日期：2025.3.26
# 文件名：3-1_straight_interpolation.py

import roboticstoolbox as rtb
from spatialmath import SE3
from spatialmath.base import *
import swift
import time
import matplotlib.pyplot as plt


robot = rtb.models.UR5()
env = swift.Swift()
env.launch()
env.add(robot)
T1 = SE3(0.3, 0.3, 0.4) *SE3.OA([-1, 0, 0], [0, 0, 1])
T2 = SE3(0.3, -0.3, 0.4) *SE3.OA([-1, 0, 0], [0, 0, 1])
tg = rtb.ctraj(T1, T2, 100) # 笛卡尔空间的位姿插补
dt = 0.050
q = []
for T in tg:
    robot.q = robot.ikine_LMS(T, robot.q).q
    q.append(robot.q)
    # print(robot.q)
    env.step()
    time.sleep(dt)

# 绘制各关节位置运动曲线
import numpy as np
plt.figure()
plt.subplot(1, 2, 1)
for i in range(robot.n):
    plt.plot(np.array(q)[:, i], label=f'joint {i+1}')
plt.xlabel('trajectory point')
plt.ylabel('joint angle')
plt.legend()
plt.title('jonit angle motion curve')

# 绘制末端位姿的运动曲线
x = [] # 末端位姿的x坐标
y = []
z = []
for T in tg: 
    x.append(T.t[0]) # 将末端位姿的x坐标加入列表
    y.append(T.t[1])
    z.append(T.t[2])
plt.subplot(1, 2, 2)
plt.plot(x, label='X')
plt.plot(y, label='Y')
plt.plot(z, label='Z')
plt.xlabel('trajectory point')
plt.ylabel('end_position')
plt.legend()
plt.title('end_position motion curve')
plt.show()