'''
For each bill you pay using CRED, you earn X CRED coins.
At CodeChef store, each bag is worth 100 CRED coins.Chef pays Y number of bills using CRED. Find the maximum number of bags he can get from the CodeChef store.'''
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    c=a*b
    print(c//(100))
        
