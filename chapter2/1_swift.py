# 实验2-1： 在swift模拟器中仿真机器人运动
# 实验成员：052210424丁雨童
# 日期：2025.3.18
# 文件名：1_swift.py

import swift
import roboticstoolbox as rtb
import numpy as np
import time


# 启动swift虚拟仿真器
env = swift.Swift() 
env.launch()

# 创建机器人
robot = rtb.models.UR5()
# robot.q =robot.qr
env.add(robot)

# 改变机器人模型关节角的回调函数
def set_joint(j,value):
    robot.q[j] = np.deg2rad(float(value))
    print(robot.fkine(robot.q))

# 循环遍历机器人的每个关节，并使用滑块控件控制关节角的大小
j = 0
for link in robot.links:
    if link.isjoint:
        env.add(
            swift.Slider(
                lambda x, j=j: set_joint(j, x),
                min=np.round(np.rad2deg(link.qlim[0]), 2),
                max=np.round(np.rad2deg(link.qlim[1]), 2),
                step=1,
                value=np.round(np.rad2deg(robot.q[j]), 2),
                desc="Panda Joint " +str(j),
                unit="&#176;",
            )
        )   
        j += 1

while True:
    env.step(0) #更新仿真环境
    time.sleep(0.01) #暂停0.01秒

#可选用不同的robot模型
robot =rtb.models.UR3()
robot =rtb.models.UR5()
robot =rtb.models.UR10()
robot =rtb.models.Puma560()
robot =rtb.models.YuMi()
