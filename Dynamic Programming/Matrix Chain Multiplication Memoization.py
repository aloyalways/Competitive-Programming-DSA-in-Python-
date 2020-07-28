import sys
def mcm(arr,i,j):
    t=[[-1]*1001 for _ in range(1001)]
    ans=sys.maxsize
    if i>=j:
        return 0
    if t[i][j]!=-1:
        return t[i][j]
    for k in range(i,j):
        temp_ans=mcm(arr,i,k)+mcm(arr,k+1,j)+arr[i-1]*arr[k]*arr[j]
        if temp_ans<ans:
            ans=temp_ans
    t[i][j]=ans
    return t[i][j]
        
arr=[40,20,30,10,30]
print(mcm(arr,1,len(arr)-1))