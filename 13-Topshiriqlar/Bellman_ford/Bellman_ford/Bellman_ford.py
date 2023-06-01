
def bellman_ford(graph, source):
    vertices = len(graph)
    distance = [float('inf')] * vertices
    distance[source] = 0

    for i in range(vertices - 1):
        for j in range(vertices):
            for k in range(vertices):
                if graph[j][k] != 0 and distance[j] != float('inf') and distance[j] + graph[j][k] < distance[k]:
                    distance[k] = distance[j] + graph[j][k]

    for j in range(vertices):
        for k in range(vertices):
            if graph[j][k] != 0 and distance[j] != float('inf') and distance[j] + graph[j][k] < distance[k]:
                raise Exception("Graph contains a negative-weight cycle")

    return distance

graph = [
    [0, 52, 27, 82, 23, 91, 13],
    [52, 0, 52, 13, 70, 77, 54 ],
    [27, 52, 0, 44, 96, 26, 62],
    [ 82, 13, 44, 0, 22, 16, 20],
    [23, 79, 96, 22, 0, 74, 14],
    [91, 77, 26, 16, 74, 0, 73],
    [29 ,18 ,63 ,54 ,85 ,46 ,0]
]
source = 0
distances = bellman_ford(graph, source)
for i in range(len(distances)):
    print(f"The shortest distance from vertex {source} to vertex {i} is {distances[i]}")