from typing import Any, Callable, List
import networkx as nx
import matplotlib.pyplot as plt


class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value: Any) -> None:
        self.value = value
        self.left_child = None
        self.right_child = None

    def __str__(self) -> str:
        string: str = 'Value: '
        string += str(self.value)
        if self.left_child is not None:
            string += '\nLeft child value: ' + str(self.left_child.value)
        if self.right_child is not None:
            string += '\nRight child value: ' + str(self.right_child.value)
        return string

    def is_leaf(self) -> bool:
        if self.left_child is not None or self.right_child is not None:
            return False
        return True

    def add_left_child(self, value: Any) -> None:
        if self.value is not None:
            self.left_child = BinaryNode(value)

    def add_right_child(self, value: Any) -> None:
        if self.value is not None:
            self.right_child = BinaryNode(value)

    def traverse_in_order(self, visit: Callable[[Any], None]) -> None:
        if self.value is not None:
            if self.left_child:
                self.left_child.traverse_in_order(visit)
            visit(self)
            if self.right_child:
                self.right_child.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]) -> None:
        if self.value is not None:
            if self.left_child:
                self.left_child.traverse_post_order(visit)
            if self.right_child:
                self.right_child.traverse_post_order(visit)
            visit(self)

    def traverse_pre_order(self, visit: Callable[[Any], None]) -> None:
        if self.value is not None:
            visit(self)
            if self.left_child:
                self.left_child.traverse_pre_order(visit)
            if self.right_child:
                self.right_child.traverse_pre_order(visit)


class BinaryTree:
    root: BinaryNode

    def __init__(self, value) -> None:
        self.root = BinaryNode(value)

    def traverse_in_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_post_order(visit)

    def traverse_pre_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_pre_order(visit)

    def show(self) -> None:
        connections = []

        def left_nodes(node: BinaryNode, tuple_list):
            if node.left_child:
                tuple_list.append((node.value, node.left_child.value))
                left_nodes(node.left_child, tuple_list)
            if node.right_child:
                tuple_list.append((node.value, node.right_child.value))
                right_nodes(node.right_child, tuple_list)

        def right_nodes(node: BinaryNode, tuple_list):
            if node.right_child:
                tuple_list.append((node.value, node.right_child.value))
                right_nodes(node.right_child, tuple_list)
            if node.left_child:
                tuple_list.append((node.value, node.left_child.value))
                left_nodes(node.left_child, tuple_list)

        if self.root.left_child:
            left_nodes(self.root, connections)
        if self.root.right_child:
            right_nodes(self.root, connections)

        result = nx.DiGraph()
        result.add_edges_from(connections)
        pos = nx.spectral_layout(result)
        nx.draw_networkx_nodes(result, pos)
        nx.draw_networkx_edges(result, pos)
        nx.draw_networkx_labels(result, pos)
        plt.show()


def visit_node(self) -> None:
    print(str(self.value))


def top_line(tree: BinaryTree) -> List[BinaryNode]:
    top_line_list: List[BinaryNode] = []
    if tree.root.left_child:
        def get_left_side(node: BinaryNode) -> List[BinaryNode]:
            left_side: List[BinaryNode] = []
            if node.left_child:
                left_side += get_left_side(node.left_child)
            left_side.append(node)
            return left_side
        top_line_list += get_left_side(tree.root.left_child)
    top_line_list.append(tree.root)
    current = tree.root
    while current.right_child:
        top_line_list.append(current.right_child)
        current = current.right_child
    return top_line_list
