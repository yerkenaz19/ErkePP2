def down(n):
    for i in range(0,n+1):
        yield n-i
    
n=int(input())
for num in down(n):
    print(num)