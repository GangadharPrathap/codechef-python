'''
Chef is looking to buy a TV and has shortlisted two models. The first one costs A rupees, while the second one costs B rupees.
Since there is a huge sale coming up on Chefzon, Chef can get a flat discount of C rupees on the first TV, and a flat discount of D rupees on the second one.Help Chef determine which of the two TVs would be cheaper to buy during the sale.
'''n=int(input())
for i in range(n):
    a,b,c,d=map(int,input().split())
    if (a-c)<(b-d):
        print('First')
    elif(a-c)>(b-d):
        print('Second')
    else:
        print('Any')
