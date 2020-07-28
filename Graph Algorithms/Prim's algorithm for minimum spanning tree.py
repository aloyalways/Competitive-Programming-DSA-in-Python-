from collections import defaultdict
import heapq

n=5
edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0), (1, 4), (1, 3)]
weight = [1, 4, 2, 6, 7, 5, 3]
graph=defaultdict(list)

for i in range(len(edges)):
    x=edges[i][0]
    y=edges[i][1]
    graph[x].append((weight[i],y))
    graph[y].append((weight[i],x))
    
heap=[]
visited=[False]*n

# start at an arbitrary node - here 0
# add edge to heap with edge weight priority
for i in range(len(graph[0])):
    heapq.heappush(heap,(graph[0][i],0))
visited[0]=True
cost=0
mst=[]

# while there is an unvisited node
# here we consider that the given graph is connected
while len(mst)<n-1:
    # get minimum-weight edge to an unvisited node from heap
    # heap[0] gives the top element in the min heap with edge weight priority
    w=heap[0][0][0]
    previousNode=heap[0][1]
    node=heap[0][0][1]
    heapq.heappop(heap)
    
    # already visited 
    if visited[node]:
        continue
    
    # found new reachable node. Mark visited and update MST 
    visited[node]=True
    cost+=w
    mst.append((node,previousNode))
    
    # add all edges from this node to the heap
    for i in range(len(graph[node])):
        heapq.heappush(heap,(graph[node][i],node))
        
print("Minimum cost of spanning tree is: " + str(cost))
print("Following are the edges in MST: ")
for i in range(len(mst)):
    print(str(mst[i][0]) + " " + str(mst[i][1]))
