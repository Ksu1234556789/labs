from collections import deque
from typing import Any, Optional, Iterable


class Stack:

    def __init__(self, iterable: Optional[Iterable[Any]] = None):
        self._data: list[Any] = list(iterable) if iterable is not None else []

    def push(self, item: Any) -> None:
        self._data.append(item)

    def pop(self) -> Any:
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self) -> Optional[Any]:
        return self._data[-1] if self._data else None

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def __len__(self) -> int:
        return len(self._data)

    def __str__(self) -> str:
        return f"Stack({self._data})"


class Queue:

    def __init__(self, iterable: Optional[Iterable[Any]] = None):
        self._data: deque[Any] = deque(iterable) if iterable is not None else deque()

    def enqueue(self, item: Any) -> None:
        self._data.append(item)

    def dequeue(self) -> Any:
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._data.popleft()

    def peek(self) -> Optional[Any]:
        return self._data[0] if self._data else None

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def __len__(self) -> int:
        return len(self._data)

    def __str__(self) -> str:
        return f"Queue({list(self._data)})"


# Демонстрация работы Stack
print("ДЕМОНСТРАЦИЯ РАБОТЫ STACK (LIFO)")
print("=" * 40)

stack = Stack([10, 20, 30, 40])
print(f"Создан стек с элементами: {stack._data}")
print(f"Снимаем верхний элемент стека (pop): {stack.pop()}")
print(f"Стек после pop: {stack._data}")
print(f"Пустой ли стек? {stack.is_empty()}")
print(f"Верхний элемент (peek): {stack.peek()}")
stack.push(99)
print(f"Добавляем 99 в стек (push)")
print(f"Верхний элемент после push: {stack.peek()}")
print(f"Длина стека: {len(stack)}")
print(f"Весь стек: {stack}")
print()

# Демонстрация работы Queue
print("ДЕМОНСТРАЦИЯ РАБОТЫ QUEUE (FIFO)")
print("=" * 40)

queue = Queue([100, 200, 300, 400])
print(f"Создана очередь с элементами: {list(queue._data)}")
print(f"Первый элемент (peek): {queue.peek()}")
print(f"Извлекаем элемент из начала (dequeue): {queue.dequeue()}")
print(f"Очередь после dequeue: {list(queue._data)}")
print(f"Первый элемент после dequeue: {queue.peek()}")
queue.enqueue(777)
print(f"Добавляем 777 в очередь (enqueue)")
print(f"Первый элемент после enqueue: {queue.peek()}")
print(f"Пустая ли очередь? {queue.is_empty()}")
print(f"Количество элементов в очереди: {len(queue)}")
print(f"Вся очередь: {queue}")