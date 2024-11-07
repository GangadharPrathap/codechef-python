'''
There were initially X million people in a town, out of which Y million people left the town and Z million people immigrated to this town.
Determine the final population of town in millions.
'''n=int(input())
for i in range(n):
    a,b,c=map(int,input().split())
    print(a-b+c)
  
