import sys
sys.setrecursionlimit(10**6)

def DFS(data,x,y):
    count=0
    if data[x][y]==1:
        data[x][y]=0
        count=1
        if x>0:
            count +=DFS(data, x - 1, y)
        if y>0:
            count +=DFS(data, x , y - 1)
        if y<N-1:
            count +=DFS(data, x , y + 1)
        if x<N-1:
            count +=DFS(data, x + 1, y)
    return count

N=int(input())
data=[]
for i in range(N):
    data.append(list(map(int,input())))
arr=[]
for i in range(N):
    for j in range(N):
        count=DFS(data,i,j)
        if count>0:
            arr.append(count)
arr.sort()
print(len(arr))
for i in arr:
    print(i)