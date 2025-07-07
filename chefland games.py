n=int(input())
for i in range(n):
    a,b,c,d=map(int,input().split())
    if a==1 or b==1 or c==1 or d==1:
        print('OUT')
    else:
        print('IN')
