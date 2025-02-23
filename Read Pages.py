'''
Chef has started studying for the upcoming test. The textbook has N pages in total. Chef wants to read at most X pages a day for Y days.
Find out whether it is possible for Chef to complete the whole book.'''
# cook your dish here
n=int(input())
for i in range(n):
    a,s,d=map(int,input().split())
    if(s*d)>=a:
        print('YES')
    else:
        print('NO')
