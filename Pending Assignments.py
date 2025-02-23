'''
Chef has finally decided to complete all of his pending assignments.There are X assignments where each assignment takes Y minutes to complete.
Find whether Chef would be able to complete all the assignments in Z days.
'''n=int(input())
for i in range(n):
    a,b,c=map(int,input().split())
    if a*b<=c*24*60:
        print('YES')
    else:
        print('NO')
