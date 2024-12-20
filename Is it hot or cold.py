'''
Chef considers the climate HOT if the temperature is above 20, otherwise he considers it COLD. You are given the temperature C, find whether the climate is HOT or COLD.
'''v=int(input())
for i in range(v):
    a=int(input())
    if(a>20):
        print("HOT")
    if(a<=20):
        print('COLD')
