'''
Chef is eagerly waiting for a piece of information. His secret agent told him that this information would be revealed to him after 
K weeks.X days have already passed and Chef is getting restless now. Find the number of remaining days Chef has to wait for, to get the information.
It is guaranteed that the information has not been revealed to the Chef yet.
'''
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    d=a*7-b
    print(d)
