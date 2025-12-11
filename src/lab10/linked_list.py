from typing import Any, Optional, Iterator


class Node:

    def __init__(self, value: Any, next_node: Optional['Node'] = None):
        self.value = value
        self.next = next_node

    def __repr__(self) -> str:
        return f"Node({self.value})"


class SinglyLinkedList:

    def __init__(self): 
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self._size: int = 0

    def append(self, value: Any) -> None:
        new_node = Node(value)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node  # type: ignore
            self.tail = new_node
        
        self._size += 1

    def prepend(self, value: Any) -> None:
        new_node = Node(value, self.head)
        self.head = new_node
        
        if self.tail is None:
            self.tail = new_node
        
        self._size += 1

    def insert(self, idx: int, value: Any) -> None:

        if idx < 0 or idx > self._size:
            raise IndexError(f"Index {idx} out of range [0, {self._size}]")
        
        if idx == 0:
            self.prepend(value)
            return
        
        if idx == self._size:
            self.append(value)
            return
        
        # Вставка в середину списка
        current = self.head
        for _ in range(idx - 1):
            current = current.next  # type: ignore
        
        new_node = Node(value, current.next)  # type: ignore
        current.next = new_node  # type: ignore
        self._size += 1

    def remove(self, value: Any) -> None:
 
        if self.head is None:
            raise ValueError(f"Value {value} not found in list")
        
        # Удаление из головы
        if self.head.value == value:
            self.head = self.head.next
            if self.head is None:  # список стал пустым
                self.tail = None
            self._size -= 1
            return
        
        # Поиск узла для удаления
        current = self.head
        while current.next is not None and current.next.value != value:
            current = current.next
        
        if current.next is None:  # значение не найдено
            raise ValueError(f"Value {value} not found in list")
        
        # Удаление узла
        current.next = current.next.next
        
        # Если удалили tail
        if current.next is None:
            self.tail = current
        
        self._size -= 1

    def remove_at(self, idx: int) -> None:

        if idx < 0 or idx >= self._size:
            raise IndexError(f"Index {idx} out of range [0, {self._size})")
        
        if idx == 0:  # удаление головы
            self.head = self.head.next  # type: ignore
            if self.head is None:
                self.tail = None
            self._size -= 1
            return
        
        # Удаление из середины или конца
        current = self.head
        for _ in range(idx - 1):
            current = current.next  # type: ignore
        
        current.next = current.next.next  # type: ignore
        
        # Если удалили tail
        if current.next is None:  # type: ignore
            self.tail = current
        
        self._size -= 1

    def __iter__(self) -> Iterator[Any]:
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def __len__(self) -> int:
        return self._size

    def __repr__(self) -> str:
        values = list(self)
        return f"SinglyLinkedList({values})"

    def __str__(self) -> str:
        if self.head is None:
            return "SinglyLinkedList: None"
        
        parts = []
        current = self.head
        while current is not None:
            parts.append(f"[{current.value}]")
            current = current.next
        
        return "SinglyLinkedList: " + " -> ".join(parts) + " -> None"


# Демонстрация работы SinglyLinkedList
print("ДЕМОНСТРАЦИЯ РАБОТЫ LINKED LIST")
print("=" * 50)

sll = SinglyLinkedList()
print(f"Создан пустой список: {sll}")
print(f"Длина списка: {len(sll)}")

# Добавляем элементы
sll.append(1)
sll.append(2)
sll.append(3)
print(f"\nПосле добавления 1, 2, 3 в конец (append):")
print(f"Список как список: {list(sll)}")
print(f"Визуальное представление: {sll}")
print(f"Длина: {len(sll)}")

# Добавляем в начало
sll.prepend(0)
print(f"\nПосле добавления 0 в начало (prepend):")
print(f"Список как список: {list(sll)}")
print(f"Визуальное представление: {sll}")
print(f"Длина: {len(sll)}")

# Вставляем по индексу
sll.insert(2, 99)
print(f"\nПосле вставки 99 по индексу 2 (insert):")
print(f"Список как список: {list(sll)}")
print(f"Визуальное представление: {sll}")
print(f"Длина: {len(sll)}")

# Удаляем значение
sll.remove(2)
print(f"\nПосле удаления значения 2 (remove):")
print(f"Список как список: {list(sll)}")
print(f"Визуальное представление: {sll}")
print(f"Длина: {len(sll)}")

# Удаляем по индексу
sll.remove_at(1)
print(f"\nПосле удаления элемента по индексу 1 (remove_at):")
print(f"Список как список: {list(sll)}")
print(f"Визуальное представление: {sll}")
print(f"Длина: {len(sll)}")