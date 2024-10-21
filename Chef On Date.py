'''
Chef and his girlfriend went on a date. Chef took X dollars with him, and was quite sure that this would be enough to pay the bill. At the end, the waiter brought a bill of Y dollars.
Print "YES" if Chef has enough money to pay the bill, or "NO" if he has to borrow from his girlfriend and leave a bad impression on her.
'''
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    if(a>=b):
        print('YES')
    else:
        print('NO')
