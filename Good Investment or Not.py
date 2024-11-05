'''
Chef has invested his money at an interest rate of X percent per annum while the current inflation rate is Y percent per annum.
An investment is called good if and only if the interest rate of the investment is at least twice of the inflation rate.
Determine whether the investment made by Chef is good or not
'''n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    if(a>=2*b):
        print('YES')
    else:
        print('NO')
