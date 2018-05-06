Max = 1000
Data = [] * Max
Table = [] * Max


def getMin(x, y):
    return x if x < y else y


N = int(input())

for i in range(N):
    Data.insert(i, [int(k) for k in input().split()])

Table.insert(0, Data[0])

for i in range(1, N):
    Table.insert(i, [getMin(Table[i - 1][1], Table[i - 1][2]) + Data[i][0],
                     getMin(Table[i - 1][0], Table[i - 1][2]) + Data[i][1],
                     getMin(Table[i - 1][0], Table[i - 1][1]) + Data[i][2]])

print(getMin(Table[N - 1][0], getMin(Table[N - 1][1], Table[N - 1][2])))