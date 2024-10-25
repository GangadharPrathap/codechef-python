'''
Chef wants to conduct a lecture for which he needs to set up an online meeting of exactly X minutes.
The meeting platform supports a meeting of maximum 30 minutes without subscription and a meeting of unlimited duration with subscription.
Determine whether Chef needs to take a subscription or not for setting up the meet.
'''
n=int(input())
for i in range(n):
    a=int(input())
    if a>30:
        print('YES')
    else:
        print('NO')
