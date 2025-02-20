'''
There are 
N
N bikes and 
M
M cars on the road.

Each bike has 
2
2 tyres.
Each car has 
4
4 tyres.
Find the total number of tyres on the road.
'''# cook your dish here
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    print(a*2+4*b)
