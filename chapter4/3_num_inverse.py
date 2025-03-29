# 实验3：数值法逆运动学
# 实验成员：052210424丁雨童
# 日期：2025.3.25
# 文件名：3_num_inverse.py


import numpy as np
import roboticstoolbox as rtb
from swift import Swift
import time
import sys, os
sys.path.append(os.getcwd())
from appendix import numercial_IK

class NR(numercial_IK):
    def __init__(self, pinv=False, **kwargs):
        super().__init__(**kwargs)
        self.pinv = pinv
        self.name = f"NR (pinv= {pinv})"

    def step(self, ets: rtb.ETS, Tep: np.ndarray, q: np.ndarray):
        Te = ets.eval(q)
        e, E =self.error(Te, Tep)
        J = ets.jacob0(q)
        if self.pinv:
            q += np.linalg.pinv(J) @ e
        else:
            q += np.linalg.inv(J) @ e
        return E, q   
    
if __name__ =='__main__':
    # 启动虚拟仿真环境
    env =Swift()
    env.launch(realtime=True)
    # 构造机器人对象
    panda =rtb.models.Panda()
    ets =panda.ets()
    # 取消关节角限位
    for link in panda.links:
        if link.isjoint:
            link.qlim =[-np.inf, np.inf]
    # 将机器人对象添加虚拟环境中
    env.add(panda)
    ilimit =30 # 设置单次搜索最大迭代次数
    slimit =100 # 设置最大搜索次数
    q0 = ets.random_q(slimit) # 设置若干组数值随机的q的初值
    problems =10 # 设置测试数据集数量
    q_Tep =ets.random_q(problems) # 根据测试数据集数量生成若干组随机的输入量q
    # 根据若干组随机的输入量q，生成对应的末端位姿
    Tep =np.zeros((problems, 4, 4))
    for i in range(problems):
        Tep[i] = ets.eval(q_Tep[i])

        # 定义一个基于Newton-Raphson (NR) 方法的求解器
    solver =NR(pinv=True, ilimit=30, slimit=100, problems=problems)
    # 对测试集中每个数据进行遍历、计算
    for pose in Tep:
    # 使用求解器求解逆运动学
        q, success, iterations, searches, residual =solver.solve(ets, pose, q0)
        print(f"Successful: {success}, iterations: {iterations}, searches: {searches},residual: {residual}")
    # 更新关节角数据，并在仿真环境中渲染机器人模型
    panda.q =q
    env.step(0)
    time.sleep(2)