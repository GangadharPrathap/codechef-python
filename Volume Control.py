'''
Chef is watching TV. The current volume of the TV is X.
Pressing the volume up button of the TV remote increases the volume by 1 while pressing the volume down button decreases the volume by 1.
Chef wants to change the volume from X to Y. Find the minimum number of button presses required to do so.
'''n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    s=abs(b-a)
    print(s)
