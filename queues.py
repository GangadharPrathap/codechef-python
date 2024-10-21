'''
++++++++++++++++++++++++++++++++++++++++++++++++++QUEUES++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    1. It can be used same as stacks but we can remove from both ends but not the ones in the middle
    2. follows first in first out or last in last out rule
    3. 
'''
Front,Rear=-1,-1
l=[]
n=5
def Size(Front,Rear):
  return abs(Front-Rear)

def Display(Front,Rear):
  for i in range(Front,Rear):
    print(l[i],end=" ")

def Enqueue(element,Front,Rear):
  if Size(Front,Rear)<n:
    l.append(element)
    Rear=Rear+1
    return [Front,Rear]
  else:
    print("Queue is Full")
    return [Front,Rear]
    
def Dequeue(Front,Rear):
  if Size(Front,Rear)>0:
    l.pop(0)
    Front=Front+1
    return [Front,Rear]
  else:
    print("Queue is Empty")
    return [Front,Rear]

x=Enqueue(10,Front,Rear)
Front,Rear=x[0],x[1]
x=Enqueue(20,Front,Rear)
Front,Rear=x[0],x[1]
x=Enqueue(30,Front,Rear)
Front,Rear=x[0],x[1]
x=Enqueue(40,Front,Rear)
Front,Rear=x[0],x[1]
x=Enqueue(50,Front,Rear)
Front,Rear=x[0],x[1]
x=Dequeue(Front,Rear)
Front,Rear=x[0],x[1]
print(Size(Front,Rear))
Display(Front,Rear)