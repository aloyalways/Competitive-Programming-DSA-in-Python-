import heapq

def addnumber(value,maxHeap,minHeap):
    if len(maxHeap)==0 or -1*maxHeap[0]>value:
        heapq.heappush(maxHeap,-1*value)
    else:
        heapq.heappush(minHeap,value)

def rebalance(maxHeap,minHeap):
    if abs(len(maxHeap)-len(minHeap))==2:
        if len(maxHeap)>len(minHeap):
            heapq.heappush(minHeap,-1*heapq.heappop(maxHeap))
        else:
            heapq.heappush(maxHeap,-1*heapq.heappop(minHeap))

def medians(maxHeap,minHeap):
    if len(maxHeap)==len(minHeap):
        return (-1*maxHeap[0]+minHeap[0])/2
    elif len(maxHeap)>len(minHeap):
        return float(-1*maxHeap[0])
    else:
        return float(minHeap[0])

n=int(input())
maxHeap=[]                  #For lower values
minHeap=[]                  #For higher values
heapq.heapify(maxHeap)
heapq.heapify(minHeap)
for i in range(n):
    value=int(input())
    addnumber(value,maxHeap,minHeap) #Adding numbers in the heaps
    rebalance(maxHeap,minHeap)       #Rebalancing if the length of any heap exceeds more than two
    print(medians(maxHeap,minHeap))  #Calculating the medians