def filter_prime(nums):
    for i in nums:
        c=0
        for j in range(1, i):
            if i % j==0:
                c+=1
        if(c==1):
            pnums.append(i)
    print(pnums)
        
nums=list(map(int,input().split()))
pnums=[]
filter_prime(nums)