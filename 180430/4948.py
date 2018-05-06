while True:
    n = int(input())
    if n==0:
        break
    prime = [True] * (2 * n + 1)
    prime[0] = False
    prime[1] = False
    count = 0
    for i in range(2,2*n+1):
        if prime[i]:
            if i>n:
                count+=1
            for j in range(2*i,2*n+1,i):
                prime[j]=False
    print(count)