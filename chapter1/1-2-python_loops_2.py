#1-2-python_loops_2.py
#列举由 1,2,3,4 所能组成的所有互不相同且无重复数字的三位数，并输出

for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i != j and i != k and j != k:
                print(i,j,k)