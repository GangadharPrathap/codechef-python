'''
Chef decided to redecorate his house, and now needs to decide between two different styles of interior design.
For the first style, tiling the floor will cost X1 rupees and painting the walls will cost Y1 rupees.
For the second style, tiling the floor will cost X2 rupees and painting the walls will cost Y2 rupees.
Chef will choose whichever style has the lower total cost. How much will Chef pay for his interior design?'''
n=int(input())
for i in range(n):
    a,s,d,f=map(int,input().split())
    if((a+s)<(d+f)):
            print(a+s)
    else:
        print(d+f)
