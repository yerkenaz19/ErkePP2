import math

def cube(n):
    for i in range(1,n+1):
        yield math.pow(i,3)


n=int(input())
for num in cube(n):
    print(num)