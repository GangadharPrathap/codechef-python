n=int(input())
for i in range(n):
    a,b,c=map(int,input().split())
    if (a==0 and b==0) or (c==0 and b==0) or (a==0 and c==0) or (a==0 and b==0 and c==0):
        print('Water filling time')
    else:
        print('Not now')
