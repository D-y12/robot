#1-3-pythpn_func_2.py
#写一个 Python 函数，输入一个 list 和一个数 n，判断该 n 是否在 list 当中

import numpy as np
def check(n,list):
    print(f"列表是:{list}")
    if n in list:
        print(f"{n} 在 list 中")
    else:
        print(f"{n} 不在 list 中")




if __name__=="__main__":
    list=np.arange(2,10)
    n=int(input("请输入一个数：")) 
    check(n,list)