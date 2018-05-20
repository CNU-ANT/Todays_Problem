n = int(input())
Table = [0 for i in range(1001)]
Table[0] = 1
Table[1] = 1

for i in range(2, n + 1):
    Table[i] = (Table[i - 1] + Table[i - 2])%10007
print(Table[n]%10007)
