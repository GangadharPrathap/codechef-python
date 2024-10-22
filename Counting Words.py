'''
Harsh was recently gifted a book consisting of N pages. Each page contains exactly M words printed on it. As he was bored, he decided to count the number of words in the book.
Help Harsh find the total number of words in the book.'''
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    print(a*b)
