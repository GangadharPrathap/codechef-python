'''
Alice, Bob, and Charlie are contributing to buy a Netflix subscription. However, Netfix allows only two users to share a subscription.
Given that Alice, Bob, and Charlie have A,B, and C rupees respectively and a Netflix subscription costs X rupees, find whether any two of them can contribute to buy a subscription.
'''n=int(input())
for i in range(n):
    a,b,c,d=map(int,input().split())
    if (a+b)>=d or (a+c)>=d or (b+c)>=d:
        print('YES')
    else:
        print('NO')
