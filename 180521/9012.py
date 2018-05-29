T=int(input())
for i in range(T):
    str=input()
    list=[]
    result=True
    for j in str:
        if j == '(':
            list.append('(')
        elif j == ')':
            if len(list)==0:
                result=False
                break
            else:
                list.pop()
    if len(list)!=0:
        result=False
    print('YES' if result else 'NO')