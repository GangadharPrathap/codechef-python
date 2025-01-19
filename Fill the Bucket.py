'''
Chef has a bucket having a capacity of K liters. It is already filled with X liters of water.
Find the maximum amount of extra water in liters that Chef can fill in the bucket without overflowing.'''
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    print(a-b)
