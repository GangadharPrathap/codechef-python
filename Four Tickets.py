'''
Four friends want to attend a concert. Each ticket costs X rupees.
They have decided to go to the concert if and only if the total cost of the tickets does not exceed 1000 rupees.
Determine whether they will be going to the concert or not.
'''
n=int(input())
for i in range(n):
    a=int(input())
    if(a*4<=1000):
        print('YES')
    else:
        print('NO')
