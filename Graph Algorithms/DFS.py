#Depth-first search explores a graph from a source vertex.
#It explores all the nodes it can from the 1st neighbor
#before moving on to the next neighbor.

from collections import defaultdict
def dfs(node):
    print("Visited "+str(node))
    visited.append(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor)
    
graph=defaultdict(list)
edges=[(0,1),(0,2),(0,3),(2,4),(4,1)]
for i in range(len(edges)):              #Using undirected graph
    x=edges[i][0]
    y=edges[i][1]
    graph[x].append(y)
    graph[y].append(x)
visited=[]
dfs(0)