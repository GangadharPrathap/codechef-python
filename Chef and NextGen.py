# cook your dish here
n=int(input())
for i in range(n):
    m,n,b,v=map(int,input().split())
    if(m*n<=b*v):
        print("Yes")
    else:
        print("No")
