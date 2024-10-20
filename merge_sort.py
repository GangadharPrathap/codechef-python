li=list(map(int,input().split()))

def merge(li,start,mid,end):
    left = li[start:mid+1]
    right = li[mid+1:end+1]
    i=0
    j=0
    x=[]
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            x.append(left[i])
            i=i+1
        else:
            x.append(right[j])
            j=j+1
    while i < len(left):
        x.append(left[i])
        i=i+1
    while j < len(right):
        x.append(right[j])
        j=j+1    
    li[start:end+1] = x[:]
    
def div(li,start,end):
    if(start<end):
        mid=(start+end)//2
        div(li,start,mid)
        div(li,mid+1,end) 
        merge(li,start,mid,end)

div(li,0,len(li)-1)
print(li)
