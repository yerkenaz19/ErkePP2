def unique(nums):
    uniq=[]
    for elem in nums:
        if elem not in uniq:
            uniq.append(elem)
    print(uniq)
nums=list(map(int,input().split()))
unique(nums)