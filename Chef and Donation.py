'''

In a certain month, Chef earned X rupees while Chefina earned Y rupees such that Y>X.
Since they want to end up with exactly the same amount, they decide to donate the difference between their income to a charity.
'''
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    print(b-a)
    
