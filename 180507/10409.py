n,T=map(int,input().split())
count=0
for i in list(map(int,input().split())):
    T-=i
    if T<0:
        break
    count+=1
print(count)

