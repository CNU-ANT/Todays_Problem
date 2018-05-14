N,S,M=map(int,input().split())
volume=list(map(int,input().split()))
dp=[[False for col in range(M+1)] for row in range(N+1)]
dp[0][S]=True
for i in range(1,N+1):
    flag=False
    for j in range(M+1):
        if dp[i-1][j]:
            ngap=j-volume[i-1]
            if ngap>=0:
                flag=True
                dp[i][ngap]=True
            pgap=j+volume[i-1]
            if pgap<=M:
                flag=True
                dp[i][pgap]=True
    if not flag:
        break
max=-1
for i in range(M,-1,-1):
    if dp[N][i]:
        max=i
        break
print(max)