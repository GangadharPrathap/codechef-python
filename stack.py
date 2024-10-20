'''
**********************************************stacks:*********************************************************
    1. the last item on the top is removed first during removal.
    2. first insertion is always bottom.
    3. only the top most element can be deleted but not the ones in middle.
    4 when we are about to add a part even the stack is filled fully then it is called stack overflow.
    5. similarly the removal of a part when it is empty is called stack underflow
    6. deletion is used as pop   and  insertion is used as push.
    '''
l=[]
n=9
m=[10,23,5,4689,26,9,5,2355,64,2314,56,2031,153,201,5613,20315,3,2031,53,203,51,2023,12,03]    
for i in range(len(m)):
    if(len(m)<n):
        l.append(m[i])
    else:
        print('pora overflow')    