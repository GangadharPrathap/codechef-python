'''
Chef has recently started playing chess, and wants to play as many games as possible.
He calculated that playing one game of chess takes at least 20 minutes of his time.
Chef has N hours of free time. What is the maximum number of complete chess games he can play in that time?'''

n=int(input())
for i in range(n):
    a=int(input())
    d=a*60//20
    print(d)
