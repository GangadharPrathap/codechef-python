'''
In Chefland, there are X schools, and each school has Y students.
The year end results are in and a total of Z students passed the exams.Assuming that all students appeared for the exams, find whether the number of students who passed in Chefland was strictly greater than 50%.
'''n=int(input())
for i in range(n):
    a,b,c=map(int,input().split())
    d=a*b
    if((c/d)*100)>50:
        print('YES')
    else:
        print('NO')
