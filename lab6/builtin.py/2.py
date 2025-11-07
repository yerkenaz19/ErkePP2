# text=input()
# cnt1=0
# cnt2=0
# for i in text:
#     if i.isupper():
#         cnt1+=1
#     elif i.islower():
#         cnt2+=1
        
# print(cnt1)
# print(cnt2)

a=list(map(int,input().split()))
min=a[0]
max=a[0]

for i in a:
    if i > max:
        max=i
        
    if i < min:
        min=i
print(max)
print(min)