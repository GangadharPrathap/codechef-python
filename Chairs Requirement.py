'''
Chef's coding class is very famous in Chefland.This year X students joined his class
and each student will require one chair to sit on. Chef already has Y chairs in his class. Determine the minimum number of new chairs Chef must buy so that every student is able to get one chair to sit on.'''
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    if(a>=b):
        print(a-b)
    else:
        print(0)
