'''
Chef has to travel to another place. For this, he can avail any one of two cab services.
The first cab service charges X rupees.
The second cab service charges Y rupees.
Chef wants to spend the minimum amount of money. Which cab service should Chef take?
'''n=int(input())
for  i in range(n):
    a,b=map(int,input().split())
    if(a<b):
        print('FIRST')
    elif(a>b):
        print('SECOND')
    else:
        print('ANY')
