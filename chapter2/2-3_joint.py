# 实验2-2： 机器人关节空间运动
# 实验成员：052210424丁雨童
# 日期：2025.3.18
# 文件名：2-3_joint.py


import swift
import roboticstoolbox as rtb
import numpy as np
import time

'''
# 创建swift虚拟仿真器
env = swift.Swift() 
env.launch()
# 创建UR5机器人并添加到虚拟环境中
robot = rtb.models.YuMi()
env.add(robot)
#定义关节空间的运动轨迹-2
#该方法需要启动swift仿真器，并将机器人添加到虚拟环境中
while True:
    # 遍历机器人每个关节角
    for i in range(len(robot.q)):
        q = robot.q[i]+0.01
        # 如果关节角大于pi，则取负值
        if q >np.pi:
            q = -q
        # 定义每个关节角数值大小，并赋值给robot.q
        robot.q[i] =q
    # 输出当前关节角矢量（可选）
    print(robot.q)
    # 更新机器人模型
    env.step(0)
    # 等待0.01s，即仿真周期
    time.sleep(0.01)
'''


#选择一种机器人构型，使用上述方法，自定义关节角连续运动曲线，将输出控制在合理范围内，进行机器人运动仿真。
# 创建swift虚拟仿真器
env = swift.Swift() 
env.launch()
# 创建Panda机器人并添加到虚拟环境中
robot = rtb.models.Panda()
env.add(robot)
#定义关节空间的运动轨迹-2
#该方法需要启动swift仿真器，并将机器人添加到虚拟环境中
while True:
    # 遍历机器人每个关节角
    for i in range(len(robot.q)):
        q = robot.q[i]+0.01
        # 如果关节角大于pi/2，则取负值
        if q >np.pi/2:
            q = -q
        # 定义每个关节角数值大小，并赋值给robot.q
        robot.q[i] =q
    # 输出当前关节角矢量（可选）
    print(robot.q)
    # 更新机器人模型
    env.step(0)
    # 等待0.01s，即仿真周期
    time.sleep(0.01)




robot =rtb.models.Panda()
robot =rtb.models.UR3()
robot =rtb.models.UR5()
robot =rtb.models.UR10()
robot =rtb.models.Puma560()
robot =rtb.models.YuMi()