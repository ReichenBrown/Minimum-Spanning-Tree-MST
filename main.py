import re

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)

    if root_x != root_y:
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

def kruskal(graph):
    graph.sort(key=lambda x: x[2])  # Sort edges by the third element (weight)
    n = len(graph)
    parent = list(range(n))
    rank = [0] * n
    mst_weight = 0

    for edge in graph:
        v1, v2, weight = edge
        if find(parent, v1) != find(parent, v2):
            mst_weight += weight
            union(parent, rank, v1, v2)

    return mst_weight

# Calculate MST weight for files 1.txt to 10.txt
for i in range(1, 11):
    filename = f"{i}.txt"
    with open(filename, "r") as file:
        edge_list_text = file.read()

    # Use regular expressions to parse the edge list from the text file
    edge_list = re.findall(r'{(\d+), (\d+), ([\d.]+)}', edge_list_text)

    # Convert the parsed data to tuples
    edge_list = [(int(v1), int(v2), float(weight)) for v1, v2, weight in edge_list]

    # Calculate the MST weight
    mst_weight = kruskal(edge_list)
    print(f"The weight of the Minimum Spanning Tree in {filename} is: {mst_weight}")
