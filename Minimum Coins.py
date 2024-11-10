'''
There are only 2 type of denominations in Chefland:Coins worth 1 rupee each
Notes worth 10 rupees eachChef wants to pay his friend exactly X rupees. What is the minimum number of coins Chef needs to pay exactly X rupees?
'''n=int(input())
for i in range(n):
    a=int(input())
    if(a>9):
        c=a%10
        print(c)
    else:
        print(a)
