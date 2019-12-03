from dsf import DisjointSetForest
from collections import deque


def topological_sort(graph):
    if graph.al is None:
        return None
    all_in_degrees = compute_indegree_every_vertex(graph)
    sort_result = list()
    queue = deque([])

    for i in range(len(all_in_degrees)):
        if all_in_degrees[i] == 0:
            queue.append(i)

    while len(queue) != 0:
        u = queue.popleft()
        sort_result.append(u)

        for adj_vertex in graph.get_adj_vertices(u):
            all_in_degrees[adj_vertex] -= 1

            if all_in_degrees[adj_vertex] == 0:
                queue.append(adj_vertex)

    if len(sort_result) != len(graph.al):
        return None

    return sort_result


def kruskal_algorithm(graph):
    if graph.al is None:
        return None
    edges = list()

    for i in range(len(graph.al)):
        tmp = graph.al[i]
        while tmp is not None:
            edges.append([i, tmp.item, tmp.weight])
            tmp = tmp.next

    def sort_key(elem):
        return elem[2]

    edges = sorted(edges, key=sort_key)
    tree = list()
    dsf = DisjointSetForest(len(graph.al))

    for edge in edges:
        if dsf.find(edge[0]) != dsf.find(edge[1]):
            dsf.union(edge[0], edge[1])
            tree.append(edge)

    return tree


def compute_indegree_every_vertex(graph):
    if graph.al is None:
        return None
    final = [0] * len(graph.al)
    for i in range(len(graph.al)):
        tmp = graph.al[i]
        while tmp is not None:
            final[tmp.item] += 1
            tmp = tmp.next
        return final
