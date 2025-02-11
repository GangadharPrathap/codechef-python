'''
Ezio can manipulate at most X number of guards with the apple of eden.Given that there are Y number of guards, predict if he can safely manipulate all of them.'''
# cook your dish here
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    if(a>=b):
        print('YES')
    else:
        print('NO')
