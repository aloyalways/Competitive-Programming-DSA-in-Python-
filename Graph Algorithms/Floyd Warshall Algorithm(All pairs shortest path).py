vertices=4
graph=[[0,3,float('inf'),7],[8,0,2,float('inf')],[5,float('inf'),0,1],[2,float('inf'),float('inf'),0]]

for k in range(vertices):
    for i in range(vertices):
        for j in range(vertices):
            graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])
print(graph)