'''
Uttu broke his phone. He can get it repaired by spending 
X
X rupees or he can buy a new phone by spending 
Y
Y rupees. Uttu wants to spend as little money as possible. Find out if it is better to get the phone repaired or to buy a new phone.''''n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    if(a>b):
        print('NEW PHONE')
    elif(a<b):
        print('REPAIR')
    else:
        print('ANY')
