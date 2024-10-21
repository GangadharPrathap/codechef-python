'''
There are three friends and a total of N candies.
There will be a fight amongst the friends if all of them do not get the same number of candies.
Chef wants to divide all the candies such that there is no fight. Find whether such distribution is possible.'''
n=int(input())
for i in range(n):
    s=int(input())
    if(s%3==0):
        print('YES')
    else:
        print('NO')
