#Segment Tree(XOR of given Range)
from math import ceil,log2

def getMid(s,e):
    return s+(e-s)//2
    
""" A recursive function to update the nodes  
which have the given index in their range.  
The following are parameters st, si, ss and se  
are same as getSumUtil()  
i --> index of the element to be updated.  
      This index is in the input array.  
diff --> Value to be added to all nodes  
which have i in range """
def updateValueUtil(st,ss,se,i,diff,si):
    if i<ss or i>se:
        return
    st[si]+=diff
    if se!=ss:
        mid=getMid(ss,se)
        updateValueUtil(st,ss,mid,i,diff,2*si+1)
        updateValueUtil(st,mid+1,se,i,diff,2*si+2)
    
def updateValue(arr,st,n,i,new_val):
    if i<0 or i>n-1:
        print("Invalid Input")
        return 
    diff=new_val-arr[i]
    arr[i]=new_val
    updateValueUtil(st,0,n-1,i,diff,0)
    
""" A recursive function to get the sum of values  
    in the given range of the array. The following  
    are parameters for this function.  
  
    st --> Pointer to segment tree  
    si --> Index of current node in the segment tree.  
           Initially 0 is passed as root is always at index 0  
    ss & se --> Starting and ending indexes of the segment 
                represented by current node, i.e., st[si]  
    qs & qe --> Starting and ending indexes of query range """
def RMQUtil(st,ss,se,qs,qe,si):
    if qs<=ss and qe>=se:
        return st[si]
        
    if se<qs or ss>qe:
        return 0
        
    mid=getMid(ss,se)
    return RMQUtil(st,ss,mid,qs,qe,2*si+1)^RMQUtil(st,mid+1,se,qs,qe,2*si+2)
    
def RMQ(st,n,start,end):
    if start<0 or end>n-1 or start>end:
        print("Invalid Input")
        return -1 
    return RMQUtil(st,0,n-1,start,end,0)

#A recursive function that constructs  
#Segment Tree for array[ss..se].  
#si is index of current node in segment tree st
def constructSTUtil(arr,ss,se,st,si):
    if ss==se:
        st[si]=arr[ss]
        return arr[ss]
        
    mid=getMid(ss,se)
    st[si]=constructSTUtil(arr,ss,mid,st,si*2+1)^constructSTUtil(arr,mid+1,se,st,si*2+2)
    return st[si]

def constructST(arr,n):
    x=int(ceil(log2(n))) #Height of the segment tree 
    max_size=2*int(2**x)-1 #Max size of segment tree 
    
    st=[0]*max_size #Allocate memory 
    constructSTUtil(arr,0,n-1,st,0) #Filling the allocated memory st 
    
    return st  

arr=[10,20,30,40]
n=len(arr)
st=constructST(arr,n) #Constructing segment tree

print("XOR of values in the given range from 1 to 3: ",RMQ(st,n,0,2))
updateValue(arr,st,n,0,0) #Updating arr[1]=10
print("updated XOR of values in the given range: ",RMQ(st,n,0,2))
