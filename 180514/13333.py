k=int(input())
q=list(map(int,input().split()))
q.sort(reverse=True)
result=0
for i in range(k):
    if q[i]>=i+1:
        if i < k-1 and q[i+1]<=i+1:
            result=i+1
            break
        elif i==k-1:
            result=k
print(result)