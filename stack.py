from typing import Any
from linkedlist import Node, LinkedList

class Stack:
    _storage: LinkedList

    def __init__(self) -> None:
        self._storage = LinkedList()

    def __str__(self) -> str:
        string: str = ''
        if self._storage.head is None:
            string = 'None'
            return string
        element: Node = self._storage.head
        while(element.next):
            string += str(element.value) + '\n'
            element = element.next
        string += str(element.value)
        return string

    def __len__(self) -> int:
        length: int = 0
        if self._storage.head is None:
            return length
        element: Node = self._storage.head
        while(element.next):
            length += 1
            element = element.next
        length += 1
        return length

    def push(self, value: Any) -> None:
        self._storage.push(value)

    def pop(self) -> Any:
        if self._storage.head is None:
            raise Warning("The stack is empty!")
        return self._storage.pop()


stack = Stack()
assert len(stack) == 0

stack.push(3)
stack.push(10)
stack.push(1)
print(stack)
assert len(stack) == 3

top_value = stack.pop()
assert top_value == 1

assert len(stack) == 2

