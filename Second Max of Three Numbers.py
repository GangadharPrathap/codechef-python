'''
Write a program that accepts sets of three numbers, and prints the second-maximum number among the three.
'''# cook your dish here
n=int(input())
for i in range(n):
    a,b,c=map(int,input().split())
    if(a>b and a<c) or (a>c and a<b):
        print(a)
    elif(b>a and b<c) or (b>c and b<a):
        print(b)
    else:
        print(c)
