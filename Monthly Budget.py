'''
Akshat has X rupees to spend in the current month. His daily expenditure is Y rupees,
i.e., he spends Y rupees each day.Given that the current month has 30 days, find out if Akshat has enough money to meet his daily expenditures for this month.
'''n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    if a>=30*b:
        print('YES')
    else:
        print('NO')
