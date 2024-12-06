'''
Alice wrote an exam containing N true or false questions
(i.e. questions whose answer is either true or false). Each question is worth 1 mark and there is no negative marking in the examination. Alice scored K marks out of N.
'''n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    print(a-b)
    
