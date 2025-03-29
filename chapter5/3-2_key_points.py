# 实验3：直线插补-多关键点.
# 实验成员：052210424丁雨童
# 日期：2025.3.26
# 文件名：3-2_key_points.py

import roboticstoolbox as rtb
from spatialmath import SE3
from spatialmath.base import *
import swift
import time
import matplotlib.pyplot as plt
import numpy as np

# 初始化机器人和仿真环境
robot = rtb.models.UR5()
env = swift.Swift()
env.launch()
env.add(robot)

# 定义多个关键点
key_points = [
    SE3(0.3, 0.3, 0.4) * SE3.OA([-1, 0, 0], [0, 0, 1]),
    SE3(0.2, 0.4, 0.5) * SE3.OA([-1, 0, 0], [0, 0, 1]),
    SE3(0.3, -0.3, 0.4) * SE3.OA([-1, 0, 0], [0, 0, 1])
]

# 进行位姿插补
N = 100  # 每个关键点之间的插补点数
traj = []
for i in range(len(key_points) - 1):
    tg = rtb.ctraj(key_points[i], key_points[i + 1], N)
    traj.extend(tg)

dt = 0.050
q = []
for T in traj:
    robot.q = robot.ikine_LMS(T, robot.q).q
    q.append(robot.q)
    # print(robot.q)
    env.step()
    time.sleep(dt)

# 绘制各关节位置运动曲线
plt.figure()
plt.subplot(1, 2, 1)
for i in range(robot.n):
    plt.plot(np.array(q)[:, i], label=f'joint {i+1}')
plt.xlabel('trajectory point')
plt.ylabel('joint angle')
plt.legend()
plt.title('joint angle motion curve')

# 绘制末端位姿的运动曲线
x = []
y = []
z = []
for T in tg:
    x.append(T.t[0])
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
