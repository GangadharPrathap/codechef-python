'''
Chef was driving on a highway at a speed of X km/hour.
To avoid accidents, there are fine imposed on overspeeding as follows:
No fine if the speed of the car ≤70 km/hour.Rs 500 fine if the speed of the car is strictly greater than 70 and ≤100.
Rs 2000 fine if the speed of the car is strictly greater than 100.
Determine the fine Chef needs to pay.
'''
n=int(input())
for i in range(n):
    a=int(input())
    if(a<=70):
        print(0)
    elif(70<a<=100):
        print(500)
    else:
        print(2000)
