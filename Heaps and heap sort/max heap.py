import heapq

heap=[]
heapq.heappush(heap,-1*5)
heapq.heappush(heap,-1*2)
heapq.heappush(heap,-1*10)
print([-1*i for i in heap])

heapq.heappop(heap)
heapq.heappop(heap)
print([-1*i for i in heap])

heapq.heappush(heap,-1*7)
heapq.heappush(heap,-1*12)
print([-1*i for i in heap])

heapq.heappop(heap)
heapq.heappop(heap)
print([-1*i for i in heap])