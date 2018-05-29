N=int(input())

def move(n,start,waypoint,end):
    if n==1:
        print(start,end)
    else:
        move(n-1,start,end,waypoint)
        print(start,end)
        move(n-1,waypoint,start,end)


print(2**N-1)
move(N,1,2,3)
