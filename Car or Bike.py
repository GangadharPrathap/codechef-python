# cook your dish here
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    if(a<b):
        print("BIKE")
    if(a>b):
        print("CAR")
    if(a==b):
        print("SAME")
