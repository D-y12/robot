# 实验2-2： 机器人关节空间运动
# 实验成员：052210424丁雨童
# 日期：2025.3.18
# 文件名：2-1_joint.py

import swift
import roboticstoolbox as rtb
import numpy as np
import time



# 创建UR5机器人
robot = rtb.models.Puma560()
# 构造100个6维随机数矢量，即100x6的随机数矩阵，将其作为机器人关节角的输入
q_out =np.random.rand(100, 6)
# 将q_out中每一行作为当前时刻关节角的数值，按照dt=0.1s的间隔，输入给机器人，并渲染出仿真动画
# 注：使用该种方法仿真，无需调用swift()启动函数，直接构造robot对象即可
robot.plot(q=np.asarray(q_out), dt=0.1)






