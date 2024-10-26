'''
Chef is playing a mobile game. In the game, Chef's character Chefario can perform special attacks. However, one special attack costs X mana points to Chefario.
If Chefario currently has Y mana points, determine the maximum number of special attacks he can perform.'''
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    c=b//a
    print(c)
