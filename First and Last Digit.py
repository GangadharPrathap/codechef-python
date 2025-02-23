'''
Given an integer N . Write a program to obtain the sum of the first and last digits of this number.
'''n=int(input())
for i in range(n):
    a=int(input())
    l=a%10
    f=a
    while f>=10:
        f//=10
    print(f+l)    
    
