# 实验2-2： 机器人关节空间运动
# 实验成员：052210424丁雨童
# 日期：2025.3.18
# 文件名：2-2_joint.py


import swift
import roboticstoolbox as rtb
import numpy as np
import time



#定义关节空间的运动轨迹-2
'''
# 创建swift虚拟仿真器
env = swift.Swift() 
# 创建UR5机器人
robot = rtb.models.Puma560()

#定义关节空间的运动轨迹-2
#定义一个空的List对象
q_out =[]
# 对id进行从0到100的循环，构造100个关节角矢量
for id in range(100):
    q_i =[]
    # 对任意一个关节角矢量中对每个元素进行赋值
    for i in range(len(robot.q)):
        # 定义其中每个元素的数值
        if id ==0:
            q = robot.qr[i]+0.01
        else:
            q = q_out[id-1][i]+0.01
        if q >np.pi:
            q = -q
        # 将该元素添加到当前关节角矢量的队列当中
        q_i.append(q)
    # 将构造完成的关节角矢量添加到最终输出的矩阵中
    q_out.append(q_i)
# 根据输入的关节角矩阵，渲染出机器人运动的仿真动画
robot.plot(q =np.asarray(q_out), dt=0.05)

env.add(robot)

while True:
    env.step(0)
    time.sleep(0.01)

'''



#定义关节空间的运动轨迹-2-----自定义轨迹
# 一种机器人构型，使用上述方法，自定义关节角连续运动曲线，将输出控制在合理范围内，进行机器人运动仿真。

# 创建机器人
robot =rtb.models.URDF.KinovaGen3()
#定义关节空间的运动轨迹-2
#定义一个空的List对象
q_out =[]
# 对id进行从0到100的循环，构造100个关节角矢量
for id in range(50):
    q_i =[]
    # 对任意一个关节角矢量中对每个元素进行赋值
    for i in range(len(robot.q)):
        # 定义其中每个元素的数值
        if id ==0:
            q = robot.qr[i]+0.02
        else:
            q = q_out[id-1][i]+0.02
        if q >np.pi:
            q = -q
        # 将该元素添加到当前关节角矢量的队列当中
        q_i.append(q)
    # 将构造完成的关节角矢量添加到最终输出的矩阵中
    q_out.append(q_i)
# 根据输入的关节角矩阵，渲染出机器人运动的仿真动画
robot.plot(q =np.asarray(q_out), dt=0.05)






robot =rtb.models.URDF.KinovaGen3()
robot =rtb.models.URDF.vx300s()
robot =rtb.models.DH.IRB140()