max=0
for i in range(4):
    a,b=map(int,input().split())
    now=max-a+b
    max=max if max>now else now
print(max)