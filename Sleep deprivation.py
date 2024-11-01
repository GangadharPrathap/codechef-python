'''
A person is said to be sleep deprived if he slept strictly less than 7 hours in a day.
Chef was only able to sleep X hours yesterday. Determine if he is sleep deprived or not.'''
n=int(input())
for i in range(n):
    a=int(input())
    if(a<7):
        print('YES')
    else:
        print('NO')
