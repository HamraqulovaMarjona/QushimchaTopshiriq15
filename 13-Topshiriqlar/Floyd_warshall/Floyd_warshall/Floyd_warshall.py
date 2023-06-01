
def floyd_warshall(graph):
    vertices = len(graph)
    distance = list(map(lambda i: list(map(lambda j: j, i)), graph))

    for k in range(vertices):
        for i in range(vertices):
            for j in range(vertices):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

    return distance

graph = [
    [0, 52, 27, 82, 23, 91, 13],
    [52, 0, 52, 13, 70, 77, 54],
    [27, 52, 0, 44, 96, 26, 62],
    [82, 13, 44, 0, 22, 16, 20],
    [23, 79, 96, 22, 0 ,74 ,14],
    [91 ,77 ,26 ,16 ,74 ,0 ,73],
    [29 ,18 ,63 ,54 ,85 ,46 ,0]
]
distances = floyd_warshall(graph)
for i in range(len(distances)):
    for j in range(len(distances)):
        print(f"The shortest distance from vertex {i} to vertex {j} is {distances[i][j]}")