
import heapq

def dijkstra(graph, start):
    distances = [float('inf')] * len(graph)
    distances[start] = 0
    pq = [(0, start)]
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in enumerate(graph[current_node]):
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances

graph = [[0, 52, 27, 82, 23, 91, 13], [52, 0, 52, 13, 70, 77, 54], [27, 52, 0, 44, 96, 26, 62], [82, 13, 44, 0, 22, 16, 20], [23, 79, 96, 22, 0 ,74 ,14], [91 ,77 ,26 ,16 ,74 ,0 ,73], [29 ,18 ,63 ,54 ,85 ,46 ,0]]
start = 0
print(dijkstra(graph,start))