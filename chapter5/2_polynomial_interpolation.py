# 实验2：三次/五次多项式插补
# 实验成员：052210424丁雨童
# 日期：2025.3.26
# 文件名：2_polynomial_interpolation.py


from spatialmath import SE3
import roboticstoolbox as rtb
import swift
import matplotlib.pyplot as plt
import time
from spatialmath.base import *
import numpy as np
from roboticstoolbox.tools.trajectory import *

robot = rtb.models.Panda()
# 定义一个末端位姿
T = SE3(rpy2tr(0, 180, 0, unit="deg")) * SE3(transl(0.5, 0.3, -0.1))
# 求其运动学逆解
sol = robot.ikine_LMS(T)

# 使用默认的关节空间轨迹规划
qtraj = rtb.jtraj(robot.qz, sol.q, 100)
# print(qtraj.q)
# 使用梯形速度曲线轨迹规划
qtraj_t = rtb.mtraj(trapezoidal, robot.qz, sol.q, 100)
# 将规划够的第一个关节的角度变化曲线输出，与梯形速度曲线轨迹规划的结果进行对比
plt.subplot(2, 2, 1)
plt.plot(qtraj.q[:, 0], label='jtraj')
plt.plot(qtraj_t.q[:, 0], label='trapzoidal')
plt.xlabel('trajectory point')
plt.ylabel('joint angle')
plt.legend()
plt.title('joint1 angle motion curve')


# 三次多项式插补
def cubic(q0, qf, qd0, qdf, T, N):
    """
    计算五次多项式插值
    :param q0: 起始位置
    :param qd0: 起始速度
    :param qf: 终止位置
    :param qdf: 终止速度
    :param T: 总时间
    :param N: 插值点数
    :return: 插值后各轨迹点的关节角度数组列表
    """
    t = np.linspace(0, T, N)
    a0 = q0
    a1 = qd0
    a2 = (3 * (qf - q0) - (2 * qd0 + qdf) * T) / (T ** 2)
    a3 = (2 * (q0 - qf) + (qd0 + qdf) * T) / (T ** 3)
    q = []
    for t in t:
        q.append(a0 + a1 * t + a2 * t ** 2 + a3 * t ** 3)
    return np.array(q)

qtraj_3 = cubic(robot.q , sol.q, 0, 0, T = 10, N = 100)
plt.subplot(2, 2, 2)
for i in range(robot.n):
        plt.plot(qtraj_3[:, i], label=f'joint{i+1}')
plt.xlabel('trajectory point')
plt.ylabel('joint angle')
plt.legend()
plt.title('cubic')


# 五次多项式插补

def quintic(q0, qd0, qdd0, qf, qdf, qddf, T, N):
    """
    计算五次多项式插值
    :param q0: 起始位置
    :param qd0: 起始速度
    :param qdd0: 起始加速度
    :param qf: 终止位置
    :param qdf: 终止速度
    :param qddf: 终止加速度
    :param T: 总时间
    :param N: 插值点数
    :return: 插值后各轨迹点的关节角度矩阵
    """
    # 计算多项式系数
    a0 = q0
    a1 = qd0
    a2 = qdd0 / 2
    a3 = (20 * qf - 20 * q0 - (8 * qdf + 12 * qd0) * T - (3 * qdd0 - qddf) * T**2) / (2 * T**3)
    a4 = (30 * q0 - 30 * qf + (14 * qdf + 16 * qd0) * T + (3 * qdd0 - 2 * qddf) * T**2) / (2 * T**4)
    a5 = (12 * qf - 12 * q0 - (6 * qdf + 6 * qd0) * T - (qdd0 - qddf) * T**2) / (2 * T**5)

    
    t = np.linspace(0, T, N)
    q = []
    # 计算插值后的位置
    for t in t:
        qt = a0 + a1 * t + a2 * t**2 + a3 * t**3 + a4 * t**4 + a5 * t**5
        q.append(qt)
    return np.array(q)


qtraj_5 = quintic(robot.q ,0,0, sol.q, 0, 0, T = 10, N = 100)
plt.subplot(2, 2, 3)
for i in range(robot.n):
        plt.plot(qtraj_5[:, i], label=f'joint{i+1}')
plt.xlabel('trajectory point')
plt.ylabel('joint angle')
plt.legend()
plt.title('quintic')

# 启动swift仿真器
env = swift.Swift()
env.launch()
# 将机器人添加到仿真环境中
env.add(robot)
# 逐个轨迹点更新机器人位置
for q in qtraj_5:
    # print(q)
    robot.q = q
    env.step(0)
    time.sleep(0.01)

# 实现过路径点的三次多项式插值

def cubic_waypoint(p0, pv, pf, T, N):
    '''
     过路径点的三次多项式插值, 两规划时间相等, 即T1 = T2 = T
    :param p0: 起始位置
    :param pv: 中间位置
    :param pf: 终止位置
    :param T: 总时间
    :param N: 插值点数
    :return: 插值后各轨迹点的位置矩阵
    '''
    tf = np.linspace(0, 2*T, N)
    # 第一段曲线多项式系数
    a10 = p0
    a11 = 0
    a12 = (12*pv - 3*pf - 9*p0) / (4*T**2)
    a13 = (-8*pv + 3*pf + 5*p0) / (4*T**3)
    # 第二段曲线多项式系数
    a20 = pv
    a21 = (3*pf - 3*p0) / (4*T)
    a22 = (-12*pv + 6*pf + 6*p0) / (4*T**2)
    a23 = (8*pv - 5*pf - 3*p0) / (4*T**3)
    q = []
    for t in tf:
        if t < tf[N//2]:
            q.append(a10 + a11*t + a12*t**2 + a13*t**3)
        else:
            # 修正时间
            t-=tf[N//2]
            q.append(a20 + a21*t + a22*t**2 + a23*t**3)
    return np.array(q)

pf = np.array([0.3, -0.7, 0.7, -0.9, 0.7, 0.8, -0.2])
qtraj_waypoint = cubic_waypoint(robot.q, pf, sol.q, T = 10, N = 100)
# print(qtraj_waypoint)
# print(qtraj_waypoint[49], qtraj_waypoint[50])
plt.subplot(2, 2, 4)
for i in range(robot.n):
        plt.plot(qtraj_waypoint[:, i], label=f'joint {i+1}')
plt.xlabel('trajectory point')
plt.ylabel('joint angle')
plt.legend()
plt.title('cubic_waypoint')
# 调整子图间距
plt.subplots_adjust(wspace=0.5, hspace=0.5)
plt.show()


