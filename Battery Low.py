'''
Chef's phone shows a Battery Low notification if the battery level is 15% or less.
Given that the battery level of Chef's phone is X%, determine whether it would show a Battery low notification.'''
n=int(input())
for i in range(n):
    a=int(input())
    if(a<=15):
        print('YES')
    else:
        print('NO')
