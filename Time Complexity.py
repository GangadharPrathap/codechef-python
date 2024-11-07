'''
A sorting algorithm A is said to have more time complexity than a sorting algorithm B if it uses more number of comparisons for sorting the same array than algorithm B.
Given that algorithm A uses X comparisons to sort an array and algorithm B uses Y comparisons to sort the same array, find whether algorithm A has more time complexity
'''
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    if(a>b):
        print('YES')
    else:
        print('NO')
