'''
Chef categorises an instagram account as spam, if, the following count of the account is more than 10 times the count of followers.
Given the following and follower count of an account as X and Y respectively, find whether it is a spam account.'''
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    if(a>10*b):
        print("YES")
    else:
        print('NO')
