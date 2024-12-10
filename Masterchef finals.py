'''

Chef has been working hard to compete in MasterChef.
He is ranked X out of all contestants. However, only 10 contestants would be selected for the finals.
Check whether Chef made it to the top 10 or not?
'''
n=int(input())
for i in range(n):
    a=int(input())
    if(a>10):
        print('NO')
    else:
        print('YES')
