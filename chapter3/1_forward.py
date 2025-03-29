# 实验1： 正运动学
# 实验成员：052210424丁雨童
# 日期：2025.3.24
# 文件名：1_forward.py

import numpy as np
import roboticstoolbox as rtb
import spatialmath as sm


# 创建一个 Puma560 机器人的实例
puma = rtb.models.Puma560()
# 调用成员函数 fkine，计算机器人的正向运动学
# 查定义知，qr是机器人的ready姿态，qz是机器人的零姿态
# self.qr = np.array([0, pi / 2, -pi / 2, 0, 0, 0])
# self.qz = np.zeros(6)
T = puma.fkine(puma.qr)
print(puma.qr)
print(f"rtb库正运动学计算结果{T}")

