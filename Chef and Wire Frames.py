'''
Chef has a rectangular plate of length 
Ncm and width Mcm. He wants to make a wireframe around the plate. The wireframe costs X rupees per cm.
Determine the cost Chef needs to incur to buy the wireframe.'''a=int(input())
for i in range(a):
    a,b,c=map(int,input().split())
    s=2*a+2*b
    print(s*c)
  
