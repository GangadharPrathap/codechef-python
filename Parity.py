'''
Ashu and Arvind participated in a coding contest, as a result of which they received N chocolates. Now they want to divide the chocolates between them equally.
Can you help them by deciding if it is possible for them to divide all the N chocolates in such a way that they each get an equal number of chocolates?
You cannot break a chocolate in two or more pieces.'''
n=int(input())
for i in range(n):
    a=int(input())
    if a%2==0:
        print('Yes')
    else:
        print('No')
