n=int(input())
for i in range(n):
    a=int(input())
    if(a<=100):
        print(a)
    if(a>100 and a<=1000):
        print(a-25)
    if(a>1000 and a<=5000):
        print(a-100)
    if(a>5000):
        print(a-500)
    
