class GraphALNode:
    def __init__(self, item, next, weight):
        self.item = item
        self.weight = weight
        self.next = next


class GraphAL:
    def __init__(self, vertices, directed):
        self.al = [None] * vertices
        self.is_directed = directed

    def is_valid_vertex(self, u):
        return 0 <= u < len(self.al)

    def add_vertex(self):  # adds vertex to AL
        self.al.append(None)
        return len(self.al) - 1

    def add_edge(self, src, dest, weight=1.0):  # Adds edges from dest along with weight
        if not self.is_valid_vertex(src) or not self.is_valid_vertex(dest):
            return

        self.al[src] = GraphALNode(dest, self.al[src], weight)

        if not self.is_directed:
            self.al[dest] = GraphALNode(src, self.al[dest], weight)

    def get_num_vertices(self):  # returns the length of the adjacency list
        return len(self.al)

    def get_adj_vertices(self, vertex):  # This will return those vertices that are next to some given vertex.
        if vertex >= len(self.al):
            return None
        adj_list = list()
        temp = self.al[vertex]
        while temp is not None:
            adj_list.append(temp.item)
            temp = temp.next
        return adj_list
