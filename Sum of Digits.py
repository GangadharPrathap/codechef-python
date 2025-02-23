'''
You're given an integer N. Write a program to calculate the sum of all the digits of N.
'''n=int(input())
for i in range(n):
    a=int(input())
    s=0
    while a!=0:
        s=s+a%10
        a=a//10
    print(s)    
