#1-3-python_func_3.py
#写一个 Python 函数，输入两个正整数，求这两个数的最大公约数和最小公倍数

def func(a,b):
    gcb=0
    if a<b:  
        i=2
        while i<=a:
            if a%i==0 and b%i==0:
                gcb=i
            i+=1
        if gcb!=0:
            print(f"{a}和{b}的最大公约数是{gcb}")
            print(f"{a}和{b}的最小公倍数是{a*b//gcb}")
        else :
            print("互质")
    else:
        i=2
        while i<=b:
            if a%i==0 and b%i==0:
                gcb = i
            i+=1
        if gcb!=0:
            print(f"{a}和{b}的最大公约数是{gcb}")
            print(f"{a}和{b}的最小公倍数是{a*b//gcb}")
        else :
            print("互质")
if __name__=="__main__":
    a=int(input("请输入第一个正整数："))
    b=int(input("请输入第二个正整数："))
    func(a,b)
    