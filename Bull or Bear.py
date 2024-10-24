'''
Chef is on his way to become the new big bull of the stock market but is a bit weak at calculating whether he made a profit or a loss on his deal.
Given that Chef bought the stock at value X and sold it at value Y. Help him calculate whether he made a profit, loss, or was it a neutral deal.
'''
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    if(a==b):
        print('NEUTRAL')
    elif(a<b):
        print('PROFIT')
    else:
        print('LOSS')
