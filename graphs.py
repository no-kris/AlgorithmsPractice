from typing import Optional


class Vertex:
    def __init__(self, value) -> None:
        self.value = value
        self.adjacent_vertices = []

    def add_adjacent_vertex(self, vertex: "Vertex"):
        self.adjacent_vertices.append(vertex)
        vertex.adjacent_vertices.append(self)


class WeightedGraphVertex:
    def __init__(self, value) -> None:
        self.value = value
        self.adjacent_vertices = {}

    def add_adjacent_vertex(self, vertex, weight):
        self.adjacent_vertices[vertex] = weight


class Graph:
    def __init__(self) -> None:
        pass

    def dfs_traverse(self, vertex: Vertex, visited: dict = {}):
        visited[vertex.value] = True
        print(vertex.value)
        for neighbor in vertex.adjacent_vertices:
            if not visited.get(neighbor.value):
                self.dfs_traverse(neighbor, visited)

    def dfs_search(
        self, vertex: Vertex, search_item, visited: dict = {}
    ) -> Optional[Vertex]:
        if vertex.value == search_item:
            return vertex
        visited[vertex.value] = True
        for neighbor in vertex.adjacent_vertices:
            if not visited.get(neighbor.value):
                vertex_found = self.dfs_search(neighbor, search_item, visited)
                if vertex_found:
                    return vertex_found
        return None

    def bfs_traversal(self, vertex: Vertex):
        queue = []
        visited = {}
        visited[vertex.value] = True
        queue.append(vertex)
        while queue:
            current_vertex = queue.pop(0)
            print(current_vertex.value)
            for neighbor in current_vertex.adjacent_vertices:
                if not visited.get(neighbor.value):
                    visited[neighbor.value] = True
                    queue.append(neighbor)

    def bfs_search(self, vertex: Vertex, search_item) -> Optional[Vertex]:
        queue = []
        visited = {}
        visited[vertex.value] = True
        queue.append(vertex)
        while queue:
            current_vertex = queue.pop(0)
            if current_vertex.value == search_item:
                return current_vertex
            else:
                for neighbor in current_vertex.adjacent_vertices:
                    if not visited.get(neighbor.value):
                        visited[neighbor.value] = True
                        queue.append(neighbor)
        return None
