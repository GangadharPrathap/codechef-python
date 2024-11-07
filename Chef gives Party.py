'''
Chef wants to give a burger party to all his N friends i.e. he wants to buy one burger for each of his friends.
The cost of each burger is X rupees while Chef has a total of K rupees.
Determine whether he has enough money to buy a burger for each of his friends or not.
'''n=int(input())
for i in range(n):
    a,s,d=map(int,input().split())
    c=a*s
    if(c<=d):
        print('YES')
    else:
        print('NO')
