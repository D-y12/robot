# 实验2-2： 机器人关节空间运动
# 实验成员：052210424丁雨童
# 日期：2025.3.18
# 文件名：2.py

import swift
import roboticstoolbox as rtb
import numpy as np
import time

# 启动swift虚拟仿真器
env = swift.Swift() 
env.launch()

# 创建UR5机器人
robot = rtb.models.UR5()
#初始化机器人关节角，其中robot.qr是机器人初始关节角构成的6x1矢量
#robot.q =robot.qr
#给关节角赋值的另一种方式
# robot.q = np.array([0, -np.pi/2, np.pi/2, 0, 0, 0])
robot.q= np.array([-np.pi, -np.pi/2, 0, -np.pi/2, 0,0])
print(robot.q)

env.add(robot)

while True:
    env.step(0)
    time.sleep(0.01)



