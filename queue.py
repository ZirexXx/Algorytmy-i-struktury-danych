from typing import Any
from linkedlist import Node, LinkedList

class Queue:
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
            string += str(element.value) + ', '
            element = element.next
        string += str(element.value)
        return string

    def __len__(self) -> int:
        length: int = 0
        if self._storage.head is None:
            return length
        element: Node = self._storage.head
        while (element.next):
            length += 1
            element = element.next
        length += 1
        return length

    def peek(self) -> Any:
        if self._storage.head is None:
            raise Warning("The queue is empty!")
        return self._storage.head.value

    def enqueue(self, value: Any) -> None:
        self._storage.append(value)

    def dequeue(self) -> Any:
        if self._storage.head is None:
            raise Warning("The queue is empty!")
        return self._storage.pop()


queue = Queue()
assert len(queue) == 0

queue.enqueue('klient1')
queue.enqueue('klient2')
queue.enqueue('klient3')
assert str(queue) == 'klient1, klient2, klient3'
client_first = queue.dequeue()
assert client_first == 'klient1'
assert str(queue) == 'klient2, klient3'
assert len(queue) == 2
