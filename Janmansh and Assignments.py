'''
Janmansh has to submit 3 assignments for Chingari before 10 pm and he starts to do the assignments at X pm. Each assignment takes him 1 hour to complete. Can you tell whether he'll be able to complete all assignments on time or not?
'''
n=int(input())
for i in range(n):
    a=int(input())
    if(a+3)<=10:
        print('YES')
    else:
        print('NO')
