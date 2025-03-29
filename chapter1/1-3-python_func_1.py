#1-3-python_func_1.py
"""
写一个 Python 函数，输入参数为 n，计算并返回 n+nn+nnn 的值
（如输入 1，输出1+11+111 的值，即 123）。
"""
def add(n):
    a=n*10+n
    b=a*10+n
    print(f"{n}+{a}+{b}={n+a+b}")

if __name__=="__main__":
    add(int(input("请输入一个整数：")))



