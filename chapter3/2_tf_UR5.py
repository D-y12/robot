# 实验2：连续坐标变换构造UR5机器人的正运动学 
# 实验成员：052210424丁雨童
# 日期：2025.3.24
# 文件名：2_tf_UR5.py


import numpy as np
import roboticstoolbox as rtb
import spatialmath as sm
# 构造一个机器人对象
robot =rtb.models.UR5()
# 设定输入转角
q = np.array([0, -0.3, 0, -2.2, 0, 2])


# UR5 从基座到末端的坐标变换
E1 = rtb.ET.tz(0.089459)
E2 = rtb.ET.Rz()
E3 = rtb.ET.Rx(np.pi/2)
E4 = rtb.ET.Rz()
E5 = rtb.ET.ty(0.425)
E6 = rtb.ET.Rz(-np.pi/2)
E7 = rtb.ET.Rz()
E8 = rtb.ET.tx(-0.392)
E9 = rtb.ET.Rz()
E10 = rtb.ET.tz(0.10915)
E11 = rtb.ET.Rx(np.pi/2)
E12 = rtb.ET.Ry(-np.pi/2)
E13 = rtb.ET.Rz()
E14 = rtb.ET.tz(0.09465)
E15 = rtb.ET.Rx(-np.pi/2)
E16 = rtb.ET.Rz()
E17 = rtb.ET.tz(0.0823)
E18 = rtb.ET.Rx(-np.pi/2)
E19 = rtb.ET.Rz(-np.pi/2)    

# 将所有的变换矩阵合成
ets = E1 * E2 * E3 * E4 * E5 * E6  *E7 * E8 * E9 * E10 * E11 * E12* E13 * E14 * E15 * E16 * E17 * E18 * E19
print(ets)



# 打印出关节数量
print(f"UR5机器人有 {ets.n} 个关节")
# 打印出基本变换矩阵的数量
print(f"UR5机器人有 {ets.m} 个基本变换矩阵")
# 打印出其中某个基本变换矩阵的内容
print(f"第二个变换矩阵为 {ets[1]}")
# 如果其中一个基本变换为转轴，则会为其分配jindex，即关节序号(joint-index)，可以通过关节序号进行数据的访问
print(f"第一个转轴的序号为 {ets[1].jindex}, 第二个转轴的序号为 {ets[2].jindex}")
# 打印出所有旋转关节的变换形式
print(f"\npanda机器人所有表示转轴的基本变换矩阵为： \n{ets.joints()}")
# 设定输入转角
#构造一个单位矩阵，作为齐次变换矩阵的初值
fk = np.eye(4)
# 对运动学模型panda的每一个变换进行遍历
for et in ets:
    # 若当前变换En为转轴，则需将自变量q代入其中进行计算，得到的矩阵再与迭代结果相乘
    if et.isjoint:
        # 若当前变换En为转轴，则需将自变量q代入其中进行计算，得到的矩阵再与迭代结果相乘
        fk = fk @ et.A(q[et.jindex])
    else:
        # 若当前变换En为常量，则直接与迭代结果相乘
        fk = fk @ et.A()
# 将正向运动学计算结果输出
print(f"\n正向运动学计算结果为：\n{fk}")


# 利用rtb库计算机器人的正向运动学
robot.q=q+np.array([np.pi, -np.pi/2, 0, -np.pi/2, 0,np.pi])
T = robot.fkine(robot.q)
print(T)

if np.allclose(fk, T):
    print("两种方法计算的结果相同")
else:
    print("两种方法计算的结果不同")



    