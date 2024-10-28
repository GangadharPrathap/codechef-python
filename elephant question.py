'''
An elephant decided visit his friend. it turned out that the elephant's house is located at point 0 and his friend's house is located at pointx(x>0) of the coordiante line.
in i=one step it can move 1,2,3,4,5 positions forward.Determine, what is minimum number of steps he need to make in order to get his friend's house.
'''
n=int(input())
d=n//5
s=n%5
if(n%5==0):
    print(d)
else:
    print(d+1)    
