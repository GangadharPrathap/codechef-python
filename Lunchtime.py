'''
Chef has his lunch only between 1 pm and 4 pm (both inclusive).
Given that the current time is X pm, find out whether it is lunchtime for Chef.
'''n=int(input())
for i in range(n):
    a=int(input())
    if(1<=a<=4):
        print('YES')
    else:
        print('NO')
