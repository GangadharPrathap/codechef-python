'''
Chef is hungry and wants to reach home.
Chef can travel up to 5 kilometres on 1 litre of fuel on his motorcycle.
Currently, his motorcycle is filled with X litres of fuel and his home is Y kilometres away.
Determine whether Chef can reach his home on his motorcycle or not.
'''
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    if(a*5>=b):
        print('YES')
    else:
        print('NO')
