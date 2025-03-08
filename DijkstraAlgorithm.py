import heapq as hp

adj_list = {
    'A': {'B': 5, 'D': 3},
    'B': {'C': 7},
    'C': {},
    'D': {'C': 10}
}


def dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    previous = {vertex: None for vertex in graph}
    # print(distances, previous)
    priority_queue = [(0, start)]

    while priority_queue:
        distance, node = hp.heappop(priority_queue)
        if distance > distances[node]:
            continue
        for neighbour, weight in graph[node].items():
            # print(weight)
            new_distance = distance + weight

            if new_distance < distances[neighbour]:
                # print(neighbour)
                distances[neighbour] = new_distance
                previous[neighbour] = node
                hp.heappush(priority_queue, (new_distance, neighbour))
    return distances, previous


final_distances, final_previous = dijkstra(adj_list, 'A')
print(final_distances)
print(final_previous)
