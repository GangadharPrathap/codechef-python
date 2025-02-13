'''
On every CodeChef user's profile page, the list of problems that they have set, tested, and written editorials for, is listed at the bottom.
Given the number of problems in each of these 3 categories as X,Y, and Z respectively (where all three integers are distinct), find if the user has been most active as a Setter, Tester, or Editorialist.
'''n=int(input())
for i in range(n):
    a,b,c=map(int,input().split())
    if a>b and a>c:
        print('Setter')
    if b>a and b>c:
        print('Tester')
    if c>a and c>b:
        print('Editorialist')
