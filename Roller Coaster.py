'''Chef's son wants to go on a roller coaster ride. The height of Chef's son is X inches while the minimum height required to go on the ride is H inches. Determine whether he can go on the ride or not.'''
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    if(a>=b):
        print('YES')
    else:
        print('NO')
