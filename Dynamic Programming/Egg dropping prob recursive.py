import sys
def eggDroppingProb(e,f):
    ans=sys.maxsize
    if f==0 or f==1:
        return f
    if e==1:
        return f
    for k in range(1,f+1):
        temp=1+max(eggDroppingProb(e-1,k-1),eggDroppingProb(e,f-k))  #Max is used for worst case
        if temp<ans:
            ans=temp #Min used for minimum number of effects
    return ans
        
e=3
f=5
print(eggDroppingProb(e,f))