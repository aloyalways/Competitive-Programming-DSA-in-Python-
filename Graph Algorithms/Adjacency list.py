from collections import defaultdict

graph=defaultdict(list)
n=5
edges=[(0,1),(0,2),(0,3),(2,4),(4,1)]

for i in range(n):
    x=edges[i][0]
    y=edges[i][1]
    graph[x].append(y)
    graph[y].append(x)
print(graph)
#This is only for undirected graph
#In case of directed graph, for edge x->y push back only graph[x].append[y]