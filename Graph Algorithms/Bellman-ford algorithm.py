vertices=5
graph=[[0,1,-1],[0,2,4],[1,2,3],[1,3,2],[1,4,2],[3,2,5],[3,1,1],[4,3,-3]]
distance=[float('inf')]*vertices
parent=['nill']*vertices
distance[0]=0

for i in range(vertices-1):
    for u,v,w in graph:
        if distance[v]>distance[u]+w:
            distance[v]=distance[u]+w
            parent[v]=u

negCycle=False            
for u,v,w in graph:
    if distance[v]>distance[u]+w:
        negCycle=True
        break
        
if negCycle:
    print("A negative weight cycle exists")
else:
    for i in range(vertices):
        print("Minimum distance between source and {} is {}".format(i,distance[i]))
        print(parent)
