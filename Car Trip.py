'''
Chef rented a car for a day
Usually, the cost of the car is Rs 10 per km. However, since Chef has booked the car for the whole day, he needs to pay for at least 300 kms even if the car runs less than 300 kms.
If the car ran X kms, determine the cost Chef needs to pay.
'''n=int(input())
for i in range(n):
    a=int(input())
    if(a<300):
        print(3000)
    else:
        print(a*10)
