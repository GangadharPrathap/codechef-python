'''
Chef is shopping for masks. In the shop, he encounters 2 types of masks:
Disposable Masks — cost X but last only 1 day.Cloth Masks — cost Y but last 10 days.'''
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    if(a*100<10*b):
       print('Disposable') 
    else:
        print('Cloth')
