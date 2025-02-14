'''A participant can make 1 submission every 30 seconds.
If a contest lasts for X minutes, what is the maximum number of submissions that the participant can make during it?
It is also given that the participant cannot make any submission in the last 5 seconds of the contest.'''
n=int(input())
for i in range(n):
    a=int(input())
    print(a*2)
