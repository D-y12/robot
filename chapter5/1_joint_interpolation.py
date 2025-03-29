# 实验1：关节角速度插补
# 实验成员：052210424丁雨童
# 日期：2025.3.25
# 文件名：1_joint_interpolation.py

from spatialmath import SE3
import roboticstoolbox as rtb
import swift
import matplotlib.pyplot as plt
import time
from spatialmath.base import *


robot =rtb.models.Panda()
# 定义一个末端位姿
T = SE3(rpy2tr(0, 180, 0, unit="deg")) *SE3(transl(0.5, 0.3, -0.1))
# 求其运动学逆解
sol =robot.ikine_LMS(T)
# 规划机器人从零位到给定位置的轨迹点，数量为100个
qtraj =rtb.jtraj(robot.qz, sol.q, 100)
print(qtraj.q)


# 使用pyplot将各关节运动曲线画出来
plt.figure()
for i in range(robot.n):
    plt.plot(qtraj.q[:, i], label=f'joint {i+1}')
plt.xlabel('trajectory point')
plt.ylabel('joint angle')
plt.legend()
plt.title('jonit angle motion curve')
plt.show()

# 将生成的轨迹点输出到swift仿真器中
# 启动swift仿真器
env = swift.Swift()
env.launch()
# 将机器人添加到仿真环境中
env.add(robot)
# 逐个轨迹点更新机器人位置
for q in qtraj.q:
    # print(q)
    robot.q = q
    env.step(0)
    time.sleep(0.01)



# 使用pyplot将末端位姿的运动曲线画出来
x = [] # 末端位姿的x坐标
y = []
z = []
for q in qtraj.q: 
    T = robot.fkine(q) # 求解末端位姿
    # print(T.t)
    # print(T)
    x.append(T.t[0]) # 将末端位姿的x坐标加入列表
    y.append(T.t[1])
    z.append(T.t[2])
plt.figure()  
plt.plot(x, label='X')
plt.plot(y, label='Y')
plt.plot(z, label='Z')
plt.xlabel('trajectory point')
plt.ylabel('end_position')
plt.legend()
plt.title('end_position motion curve')
plt.show()
