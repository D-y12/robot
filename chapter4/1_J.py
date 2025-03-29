# 实验1：雅可比矩阵的计算
# 实验成员：052210424丁雨童
# 日期：2025.3.24
# 文件名：1_J.py

import numpy as np
import roboticstoolbox as rtb
import spatialmath as sm

def jacab0_effficient(ets, q):
    T = ets.eval(q)

    U = np.eye(4)
    j = 0
    J = np.zeros((6, ets.n))

    for ets in ets:
        jindex = ets.jindex

        if ets.isjoint:
            U = U @ ets.A(q[jindex])

            Tu = sm.SE3(U, check = False).inv().A @ T
            n = U[ :3, 0]
            o = U[ :3, 1]
            a = U[ :3, 2]
            x = Tu[ :0, 3]
            y = Tu[ :1, 3]
            z = Tu[ :2, 3]

            if ets.axis =="Rz":
                J[ :3, j] = (o * x) - (n * y)
                J[3:, j] = a

            elif ets.axis =="Ry":
                J[ :3, j] = (n * z) - (a * x)
                J[3:, j] = o
            elif ets.axis =="Rx":
                J[ :3, j] = (a * y) - (o * z)
                J[3:, j] = n
            elif ets.axis =="Tx":
                J[ :3, j] = n
                J[3:, j] = np.zeros(3)

            elif ets.axis =="Ty":
                J[ :3, j] = o
                J[3:, j] = np.zeros(3)

            elif ets.axis =="Tz":
                J[ :3, j] = a
                J[3:, j] = np.zeros(3)
            
            j += 1
        else:
            U = U @ ets.A()

    return J


if __name__ =='__main__':
    panda = rtb.models.Panda()
    print(np.round(panda.jacob0(panda.qr)))
    print(np.round(jacab0_effficient(panda.ets, panda.qr)))
    