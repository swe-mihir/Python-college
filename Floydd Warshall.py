graph = [[0, 8, float('inf'), 1],
         [float('inf'),0, 1,float('inf')],
         [4, float('inf'), 0, float('inf')],
         [float('inf'), 2, 9, 0]
         ]


def input_graph():
    nodes = int(input("Enter the number of nodes: "))
    graph = [[float('inf')] * nodes for _ in range(nodes)]
    for i in range(0, nodes):
        neighbours = int(input(f"Enter the number of neighbors for node {i+1}: "))
        for j in range(0, neighbours):
            neighbor, weight = input("Enter neighbor and weight (neighbor weight): ").split()
            graph[i][int(neighbor)-1] = int(weight)
        graph[i][i] = 0

    return graph

graph = input_graph()

def display():
    for rows in graph:
        print(rows)

def floyd(graph):
    length = len(graph)
    for k in range(0, length):
        for i in range(0, length):
            for j in range(0, length):
                if graph[i][k]+graph[k][j] > 0:
                    graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
        print(f"\nD{k+1}:")
        display()

print("D0:")
display()
floyd(graph)
