import sys
def mcm(arr,i,j):
    ans=sys.maxsize
    if i>=j:
        return 0
    for k in range(i,j):
        temp_ans=mcm(arr,i,k)+mcm(arr,k+1,j)+arr[i-1]*arr[k]*arr[j]
        if temp_ans<ans:
            ans=temp_ans
    return ans
        
arr=[40,20,30,10,30]
print(mcm(arr,1,len(arr)-1))