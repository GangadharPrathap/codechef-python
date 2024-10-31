'''
Chef is not feeling well today. He measured his body temperature using a thermometer and it came out to be X °F.
A person is said to have fever if his body temperature is strictly greater than 98 °F.
Determine if Chef has fever or not.
'''n=int(input())
for i in range(n):
    r=int(input())
    if(r>98):
        print('YES')
    else:
        print('NO')
