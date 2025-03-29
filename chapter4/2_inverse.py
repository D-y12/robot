# 实验2：逆运动学
# 实验成员：052210424丁雨童
# 日期：2025.3.25
# 文件名：2_inverse.py

from spatialmath import SE3
import roboticstoolbox as rtb
import swift
import time

'''
robot = rtb.models.Panda() # 机器人模型
# print(robot)
#T = robot.fkine(robot.qr) # 正运动学
#print(T)

# 逆运动学求解
# 构造一个目标位姿
T = SE3(0.7, 0.2, 0.1) * SE3.OA([0, 1, 0],[0, 0, -1]) # 末端目标位姿位姿
print(T)
sol = robot.ikine_LM(T) # 逆运动学求解
print(sol)
print(sol.q)
print(robot.fkine(sol.q)) # 检验逆运动学求解是否正确

'''


#UR5
# 启动swift虚拟仿真器
env = swift.Swift() 
env.launch()

# 创建机器人
robot = rtb.models.UR5()
# 构造一个目标位姿
T = SE3(0.7, 0.2, 0.1) * SE3.OA([0, 1, 0],[0, 0, -1]) # 末端目标位姿位姿
print(T)
sol = robot.ikine_LM(T) # 逆运动学求解
print(sol)
print(sol.q)
print(robot.fkine(sol.q)) # 检验逆运动学求解是否正确
robot.q=sol.q # 将机器人的关节角设置为求解得到的关节角
env.add(robot)
while True:
    env.step(0) #更新仿真环境
    time.sleep(0.01) #暂停0.01秒'