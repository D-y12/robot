# 实验3： 生成“机器人浪”
# 实验成员：052210424丁雨童
# 日期：2025.3.18
# 文件名：3_wave.py



import numpy as np
from spatialmath import SE3
import roboticstoolbox as rtb
from swift import Swift
import time

# 启动 Swift 仿真环境
env = Swift()
env.launch()

# 加载 Puma560 机器人的模型
puma0 = rtb.models.Puma560()
# 用于存储后续创建的多个 Puma560 机器人
pumas = []
# 要创建的机器人数量
num_robots = 15
# 计算机器人围绕圆周分布时的总旋转角度
rotation = 2 * np.pi * ((num_robots - 1) / num_robots)

# 循环创建指定数量的机器人，并将它们添加到仿真环境中
for theta in np.linspace(0, rotation, num_robots):
    # 计算每个机器人的基础位姿，通过旋转和平移得到
    base = SE3.Rz(theta) * SE3(2, 0, 0)
    # 以 puma0 为基础，拷贝构造出一个新的 puma 机器人实例
    puma = rtb.ERobot(puma0)
    # 设置新机器人的基础位姿
    puma.base = base
    # 将新机器人的关节角度初始化为零位姿
    puma.q = puma0.qz
    # 将新机器人添加到仿真环境中
    env.add(puma)
    # 将新机器人实例添加到 pumas 列表中
    pumas.append(puma)

# 生成用于创建高斯波的时间序列，用于控制机器人的运动
tt = np.linspace(0, num_robots, num_robots * 10)
# 定义高斯函数，用于生成高斯波的形状
def gaussian(x, mu, sig):
    # 根据高斯分布公式计算函数值
    return np.exp(-np.power(x - mu, 2) / (2 * np.power(sig, 2)))
# 计算高斯波的数值
g = gaussian(tt, 5, 1)
# 初始化计步器
t = 0
while True:
    # 遍历每个机器人
    for i, puma in enumerate(pumas):
        # 计算当前时间步下该机器人对应的高斯波索引
        k = (t + i * 10) % len(tt)
        # 设置机器人的关节角度，使机器人按照高斯波规律运动
        puma.q = np.r_[0, g[k], -g[k], 0, 0, 0]
        env.step(0.05)
    t += 1
    time.sleep(0.001)