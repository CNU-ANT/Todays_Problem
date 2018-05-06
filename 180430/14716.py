import sys
sys.setrecursionlimit(10**6)

M,N=map(int,input().split())

table=[]
isvisited=[[False]*N for i in range(M)]
count=0

def bfs(i,j):
    if isvisited[i][j] or table[i][j]==0:
        return
    isvisited[i][j]=True
    if i>0:
        bfs(i-1,j)
        if j>0:
            bfs(i-1,j-1)
        if j<N-1:
            bfs(i-1,j+1)
    if i<M-1:
        bfs(i+1,j)
        if j>0:
            bfs(i+1,j-1)
        if j<N-1:
            bfs(i+1,j+1)
    if j > 0:
        bfs(i, j - 1)
    if j<N-1:
        bfs(i,j+1)
    return

for i in range(M):
    table.append(list(map(int,input().split())))

for i in range(M):
    for j in range(N):
        if not isvisited[i][j] and table[i][j]==1:
            count+=1
            bfs(i,j)
print(count)