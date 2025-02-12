'''
MOST IMPORTANT:::::
Chef has opened a new airline. Chef has 10 airplanes where each airplane has a capacity of X passengers.
On the first day itself, Y people are willing to book a seat in any one of Chef's airplanes.
Given that Chef charges Z rupees for each ticket, find the maximum amount he can earn on the first day.
'''def solve():
    x, y, z = map(int, input().split())
    capacity = 10 * x
    
    if y <= capacity:
        print(y * z)
    else:
        print(capacity * z)

t = int(input())
for _ in range(t):
    solve()
