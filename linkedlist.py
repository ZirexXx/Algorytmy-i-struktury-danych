from typing import Any

class Node:
    value: Any
    next: 'Node'

    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class LinkedList:
    head: Node
    tail: Node

    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __str__(self) -> str:
        string: str = ''
        if self.head is None:
            string = 'None'
            return string
        element: Node = self.head
        while(element.next):
            string += str(element.value) + ' -> '
            element = element.next
        string += str(element.value)
        return string

    def __len__(self) -> int:
        length: int = 0
        if self.head is None:
            return length
        element: Node = self.head
        while(element.next):
            length += 1
            element = element.next
        length += 1
        return length

    def push(self, value: Any) -> None:
        new_element: Node = Node(value)
        if self.head is None:
            self.head = new_element
            self.tail = self.head
        else:
            new_element.next = self.head
            self.head = new_element
            self.tail = self.head.next

    def append(self, value: Any) -> None:
        new_element: Node = Node(value)
        if self.head is None:
            self.head = new_element
            self.tail = self.head
        else:
            element: Node = self.head
            while(element.next):
                element = element.next
            element.next = new_element
            self.tail = element.next

    def node(self, at: int) -> Node:
        element: Node = self.head
        if at >= len(self):
            raise Warning(f'There is no element at position {at} in the list')
        for i in range(at+1):
            if i == at:
                return element.value
            element = element.next

    def insert(self, value: Any, after: Node) -> None:
        element: Node = self.head
        while(element.value != after):
            if element.next is None:
                raise Warning(f'There is no element {after} in the list')
            element = element.next
        new_element: Node = Node(value)
        new_element.next = element.next
        if element == self.tail:
            self.tail = new_element
        element.next = new_element

    def pop(self) -> Any:
        if self.head is None:
            raise Warning("The list is empty!")
        tmp: Node = self.head
        self.head = self.head.next
        return tmp.value

    def remove_last(self) -> Any:
        if self.head is None:
            raise Warning("The list is empty!")
        tmp: Node = self.tail
        element: Node = self.head
        if element.next is None:
            tmp = self.head
            self.head = None
            return tmp.value
        while(element.next.next):
            element = element.next
        self.tail = element
        element.next = None
        return tmp.value

    def remove(self, after: Node) -> Any:
        if self.head is None:
            raise Warning("The list is empty!")
        element: Node = self.head
        tmp: Node
        while(element.value != after):
            element = element.next
        tmp = element.next
        if element.next == self.tail:
            self.tail = element
        element.next = element.next.next
        return tmp.value


list_ = LinkedList()
assert list_.head == None

list_.push(1)
list_.push(0)
assert str(list_) == '0 -> 1'

list_.append(9)
list_.append(10)
assert str(list_) == '0 -> 1 -> 9 -> 10'

middle_node = list_.node(at=1)
list_.insert(5, after=middle_node)
assert str(list_) == '0 -> 1 -> 5 -> 9 -> 10'

first_element = list_.node(at=0)
returned_first_element = list_.pop()
assert first_element == returned_first_element

last_element = list_.node(at=3)
returned_last_element = list_.remove_last()
assert last_element == returned_last_element
assert str(list_) == '1 -> 5 -> 9'

second_node = list_.node(at=1)
list_.remove(second_node)
assert str(list_) == '1 -> 5'
