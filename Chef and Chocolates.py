'''
Chef wants to gift C chocolates to Botswal on his birthday. However, he has only X chocolates with him.
The cost of 1 chocolate is Y rupees.Find the minimum money in rupees Chef needs to spend so that he can gift C chocolates to Botswal.'''n=int(input())
for i in range(n):
    a,b,c=map(int,input().split())
    print((a-b)*c)
