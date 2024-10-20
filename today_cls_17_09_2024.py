'''
different methods in lists:
1. slicing:
    the process of dividing  a list into different parts
    syntax:
      lsit_name[start:stop:increment]
    . it divides as per our requriements and sends us a copy of it instead of disturbing the originsl list  
2. Looping:
    as similar of using loops in an array
    syntax:
        for i in range(start:len(list):increment)
    . NOTE:
        important application:
        x=[1,2,3,4,5,6,7] be a list then we know that it has indexes starting from 0-n but it also has
        negative indexes -1 to -n from the end of the list 
    .   in the same way as before we can utlise the negative indexes from back side
    . for example:
    print(x[-5:-2:1])
    we get to print the values [3,4,5] as same as in positive but if use a decrement value then we get to
    alter the start and stop positions as per the values or negative indexes  
'''
print(1)
l=[1,2,3,4,5,6,7,8,9,10]
print(l[1:9:2])
print(l[::-1])
print(l[-1:-5:-1])
for i in range(len(l)):
    print(i,l[i])