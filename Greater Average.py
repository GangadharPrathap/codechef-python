'''
You are given 3 numbers A,B, and C.Determine whether the average of A and B is strictly greater than C or not?
'''n=int(input())
for i in range(n):
    a,b,c=map(int,input().split())
    if ((a+b)/2)>c:
        print('YES')
    else:
        print('NO')
