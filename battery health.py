'''Apple considers any iPhone with a battery health of 80% or above, to be in optimal condition.
Given that your iPhone has X% battery health, find whether it is in optimal condition.'''
n=int(input())
for i in range(n):
    a=int(input())
    if a>=80:
        print("YES")
    else:
        print('NO')
