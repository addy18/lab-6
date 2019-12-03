from lab_6 import topological_sort
from GraphAL import GraphAL
from lab_6 import kruskal_algorithm


def main():
    graph_kruskal_algorithm = GraphAL(vertices=4, directed=False)
    graph_kruskal_algorithm.add_edge(0, 4, 5.0)
    graph_kruskal_algorithm.add_edge(8, 7, 1.0)
    graph_kruskal_algorithm.add_edge(9, 1, 3.0)
    graph_kruskal_algorithm.add_edge(0, 2, 1.0)
    graph_kruskal_algorithm.add_edge(0, 1, 7.0)
    graph_kruskal_algorithm.add_edge(2, 1, 2.0)
    print("minimum spanning tree")

    for value in kruskal_algorithm(graph_kruskal_algorithm):
        print(value)

    # testing kruskal's algorithm with another graph

    graph_kruskal_algorithm = GraphAL(vertices=5, directed=False)  # arbitrary values
    graph_kruskal_algorithm.add_edge(0, 1, 7.0)
    graph_kruskal_algorithm.add_edge(4, 5, 8.0)
    graph_kruskal_algorithm.add_edge(2, 3, 4.0)
    graph_kruskal_algorithm.add_edge(1, 2, 4.0)
    graph_kruskal_algorithm.add_edge(0, 6, 3.0)
    graph_kruskal_algorithm.add_edge(5, 4, 2.0)
    graph_kruskal_algorithm.add_edge(2, 4, 1.0)
    print("minimum spanning tree:")

    for value in kruskal_algorithm(graph_kruskal_algorithm):
        print(value)

    # testing tropological's algorithm

    graph_topological = GraphAL(vertices=6, directed=True)
    graph_topological.add_edge(0, 1)
    graph_topological.add_edge(0, 2)
    graph_topological.add_edge(0, 3)
    graph_topological.add_edge(2, 5)
    graph_topological.add_edge(3, 4)
    graph_topological.add_edge(5, 4)
    print("The topological order of the first graph is:")
    print(topological_sort(graph_topological))

    # testing topological sorting algorithm with another graph

    graph_topological = GraphAL(vertices=4, directed=True)
    graph_topological.add_edge(0, 1)
    graph_topological.add_edge(0, 2)
    graph_topological.add_edge(1, 3)
    graph_topological.add_edge(3, 2)
    print("The topological order of the second graph is:")
    print(topological_sort(graph_topological))


main()
