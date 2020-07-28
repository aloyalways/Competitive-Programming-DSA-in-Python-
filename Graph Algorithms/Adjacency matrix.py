n=5

#initialising a nxn matrix with 0
adj_matrix=[[0]*n for _ in range(n)]

#adding the following edges
edges=[(0,1),(0,2),(0,3),(2,4),(4,1)]

for i in range(n):
    x=edges[i][0]
    y=edges[i][1]
    adj_matrix[x][y]=1
    adj_matrix[y][x]=1
print(adj_matrix)
#This is for undirected graph
#In case of directed graph, we will only make x->y adj_matrix[x][y]=1
#In case we want to store weights, the adj_matrix[x][y]=w
