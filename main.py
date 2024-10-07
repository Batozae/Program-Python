import sys
import heapq

def dijkstra(graph, start, end):
    distances = {node: sys.maxsize for node in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances[end]

# Example graph represented as a dictionary
graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'D': 4, 'E': 5},
    'C': {'A': 3, 'F': 1},
    'D': {'B': 4},
    'E': {'B': 5, 'F': 2},
    'F': {'C': 1, 'E': 2}
}

start_node = 'A'
end_node = 'F'

route_distance = dijkstra(graph, start_node, end_node)

print(f"The shortest distance from {start_node} to {end_node} is {route_distance}")
