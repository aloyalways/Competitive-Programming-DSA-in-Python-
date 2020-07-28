#Breath-first search explores a graph from a source 
#vertex in a way such that all nodes at a distance 
#of 1 are encountered first, then all nodes at a 
#distance of 2, then all nodes at a distance of 3 and so on.

from collections import defaultdict,deque
graph=defaultdict(list)
edges=[(0,1),(0,2),(0,3),(2,4),(4,1)]
for i in range(len(edges)):              #Using undirected graph
    x=edges[i][0]
    y=edges[i][1]
    graph[x].append(y)
    graph[y].append(x)

visited,queue=set(),deque([0])
visited.add(0)
while queue:
    vertex=queue.popleft()
    print("Visited "+str(vertex))
    for neighbour in graph[vertex]:
        if neighbour not in visited:
            visited.add(neighbour)
            queue.append(neighbour)