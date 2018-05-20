N=int(input())

array=[[0 for col in range(10)] for row in range(N)]

for i in range(1,10):
    array[0][i]=1

for i in range(1,N):
    array[i][0]=array[i-1][1]
    for j in range(1,9):
        array[i][j]=(array[i-1][j-1]+array[i-1][j+1])%1000000000
    array[i][9]=array[i-1][8]

sum=0
for i in range(10):
    sum=(sum+array[N-1][i])%1000000000
print(sum)
