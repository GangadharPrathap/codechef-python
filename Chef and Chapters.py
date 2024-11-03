'''
This semester, Chef took X courses. Each course has Y units and each unit has Z chapters in it.
Find the total number of chapters Chef has to study this semester.
'''
n=int(input())
for i in range(n):
    a,s,d=map(int,input().split())
    print(a*s*d)
