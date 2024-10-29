'''
There is a fair going on in Chefland. Chef wants to visit the fair along with his N friends.
Chef manages to collect K passes for the fair. Will Chef be able to enter the fair with all his N friends? A person can enter the fair using one pass, and each pass can be used by only one person.
'''n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    if(a<b):
        print('YES')
    else:
        print('NO')
