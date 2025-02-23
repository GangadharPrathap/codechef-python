'''
Most programmers will tell you that one of the ways to improve your performance in competitive programming is to practice a lot of problems.
Our Chef took the above advice very seriously and decided to set a target for himself.
Chef decides to solve at least 10 problems every week for 4 weeks.
Given the number of problems he actually solved in each week over 4 weeks as P1,P2,P3,and P4, output the number of weeks in which Chef met his target.
'''def c(P1, P2, P3, P4):
    count = 0
    if P1 >= 10:
        count += 1
    if P2 >= 10:
        count += 1
    if P3 >= 10:
        count += 1
    if P4 >= 10:
        count += 1
    
    return count
P1, P2, P3, P4 = map(int, input().split())
print(c(P1, P2, P3, P4))
