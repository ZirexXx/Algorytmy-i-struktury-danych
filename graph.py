from enum import Enum
from typing import Any, Optional, Dict, List, Callable
from queue import Queue
import networkx as nx
import matplotlib.pyplot as plt


class EdgeType(Enum):
    directed = 1
    undirected = 2


class Vertex:
    data: Any
    index: int

    next_index = 0

    def __init__(self, value: Any):
        self.data = value
        self.index = int(Vertex.next_index)
        Vertex.next_index += 0.5


class Edge:
    source: Vertex
    destination: Vertex
    weight: Optional[float]

    def __init__(self, s_vertex: Vertex, d_vertex: Vertex, weight: Optional[float] = None):
        self.source = s_vertex
        self.destination = d_vertex
        self.weight = weight


class Graph:
    adjacencies: Dict[Vertex, List[Edge]]

    def __init__(self):
        self.adjacencies = {}

    def create_vertex(self, data: Any) -> Vertex:
        vertex: Vertex = Vertex(data)
        self.adjacencies[vertex] = []
        return Vertex(data)

    def add_directed_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        self.adjacencies[source].append(Edge(source, destination, weight))

    def add_undirected_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        self.adjacencies[source].append(Edge(source, destination, weight))
        self.adjacencies[destination].append(Edge(destination, source, weight))

    def add(self, edge: EdgeType, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        if edge == 1:
            self.add_directed_edge(source, destination, weight)
        elif edge == 2:
            self.add_undirected_edge(source, destination, weight)

    def traverse_breadth_first(self, visit: Callable[[Any], None]) -> None:
        vx = list(self.adjacencies.keys())[0]
        visited: List[Vertex] = []
        queue: Queue = Queue()

        visit(vx)
        visited.append(vx)
        queue.enqueue(vx)
        while len(queue) != 0:
            v: Vertex = queue.peek()
            visited.append(v)
            edges = self.adjacencies[v]
            for i in range(len(edges)):
                neighbour: Vertex = edges[i].destination
                if neighbour not in visited:
                    visit(neighbour)
                    visited.append(neighbour)
                    queue.enqueue(neighbour)
            queue.dequeue()

    def traverse_depth_first(self, vx: Vertex, visited: List[Vertex], visit: Callable[[Any], None]) -> None:
        visit(vx)
        visited.append(vx)
        edges = self.adjacencies[vx]
        for i in range(len(edges)):
            if edges[i].destination not in visited:
                self.traverse_depth_first(edges[i].destination, visited, visit)

    def show(self) -> None:
        connections = []
        weights: Dict = {}
        for vx in self.adjacencies.keys():
            edges = self.adjacencies[vx]
            for i in range(len(edges)):
                connections.append((edges[i].source.data, edges[i].destination.data))
                weights[(edges[i].source.data, edges[i].destination.data)] = edges[i].weight

        result = nx.DiGraph()
        result.add_edges_from(connections)
        pos = nx.planar_layout(result)
        nx.draw_networkx_nodes(result, pos)
        nx.draw_networkx_edges(result, pos)
        nx.draw_networkx_edge_labels(result, pos, edge_labels=weights)
        nx.draw_networkx_labels(result, pos)
        plt.show()

    def __str__(self) -> str:
        vertexes = self.adjacencies.keys()
        string: str = ''
        for vx in vertexes:
            string += '- ' + str(vx.index) + ': ' + str(vx.data) + ': ----> ['
            vals = self.adjacencies[vx]
            for i in range(len(vals)):
                string += str(vals[i].destination.index) + ': ' + str(vals[i].destination.data)
                if i < len(vals) - 1:
                    string += ', '
            string += ']\n'
        return string


def visit_vx(vx: Vertex) -> None:
    print(vx.data + " ", end='')
