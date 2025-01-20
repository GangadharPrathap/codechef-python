'''
Write a program to find the remainder when an integer A is divided by an integer B.'''n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    c=a%b
    print(c)
