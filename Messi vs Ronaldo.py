'''
In Chefland, a football player gets 2 points for each goal and 1 point for each assist.
Messi has A goals and B assists this season, whereas Ronaldo has X goals and Y assists.
Find out the player with more points this season.
'''
a,b,c,d=map(int,input().split())
if((a*2+b)>(c*2+d)):
    print('Messi')
elif((a*2+b)==(c*2+d)):
    print("Equal")
else:
    print('Ronaldo')
