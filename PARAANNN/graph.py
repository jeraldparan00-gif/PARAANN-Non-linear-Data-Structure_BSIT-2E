r"""
Graph structure - PARAN

Vertices: P, A1, R, A2, N (the two A's are numbered to tell them apart)
Edges (directed): P-A1, P-R, A1-A2, A1-R, R-A2, A2-N

            P
          /   \
        A1 --> R
          \   /
           A2
            |
            N
"""
from collections import deque


class Graph:
    def __init__(self):
        self.adjacency = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency:
            self.adjacency[vertex] = []

    def add_edge(self, source, target):
        self.add_vertex(source)
        self.add_vertex(target)
        self.adjacency[source].append(target)

    def display(self):
        print("=== GRAPH ===")
        for vertex, neighbors in self.adjacency.items():
            print(f"{vertex}: {', '.join(neighbors) if neighbors else '-'}")

    def bfs(self, start):
        visited = [start]
        queue = deque([start])
        while queue:
            vertex = queue.popleft()
            for neighbor in self.adjacency[vertex]:
                if neighbor not in visited:
                    visited.append(neighbor)
                    queue.append(neighbor)
        return visited

    def dfs(self, start, visited=None):
        if visited is None:
            visited = []
        visited.append(start)
        for neighbor in self.adjacency[start]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)
        return visited


def build_graph():
    graph = Graph()
    graph.add_edge("P", "A1")
    graph.add_edge("P", "R")
    graph.add_edge("A1", "A2")
    graph.add_edge("A1", "R")
    graph.add_edge("R", "A2")
    graph.add_edge("A2", "N")
    return graph


def show_graph():
    graph = build_graph()
    graph.display()
    print("BFS:", " -> ".join(graph.bfs("P")))
    print("DFS:", " -> ".join(graph.dfs("P")))


if __name__ == "__main__":
    show_graph()
