class DynamicArray:
    def __init__(self):
        self.capacity = 2
        self.size = 0
        self.arr = [None] * self.capacity

    def append(self, x):
        if self.size == self.capacity:
            self.capacity *= 2
            new_arr = [None] * self.capacity
            for i in range(self.size):
                new_arr[i] = self.arr[i]
            self.arr = new_arr

        self.arr[self.size] = x
        self.size += 1

    def pop(self):
        if self.size == 0:
            return None
        val = self.arr[self.size - 1]
        self.size -= 1
        return val

    def print_array(self):
        print(self.arr[:self.size])

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_begin(self, x):
        new = Node(x)
        new.next = self.head
        self.head = new

    def insert_end(self, x):
        new = Node(x)
        if not self.head:
            self.head = new
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new

    def delete(self, x):
        temp = self.head
        if temp and temp.data == x:
            self.head = temp.next
            return
        prev = None
        while temp and temp.data != x:
            prev = temp
            temp = temp.next
        if temp:
            prev.next = temp.next

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, x):
        new = DNode(x)
        if not self.head:
            self.head = new
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new
        new.prev = temp

    def insert_after(self, target, x):
        temp = self.head
        while temp:
            if temp.data == target:
                new = DNode(x)
                new.next = temp.next
                new.prev = temp
                if temp.next:
                    temp.next.prev = new
                temp.next = new
                return
            temp = temp.next

    def delete_pos(self, pos):
        if not self.head:
            return
        temp = self.head

        if pos == 0:
            self.head = temp.next
            if self.head:
                self.head.prev = None
            return

        for _ in range(pos):
            if not temp:
                return
            temp = temp.next

        if not temp:
            return

        if temp.prev:
            temp.prev.next = temp.next
        if temp.next:
            temp.next.prev = temp.prev

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

class Stack:
    def __init__(self):
        self.head = None

    def push(self, x):
        new = Node(x)
        new.next = self.head
        self.head = new

    def pop(self):
        if not self.head:
            return None
        val = self.head.data
        self.head = self.head.next
        return val

    def peek(self):
        return self.head.data if self.head else None


class Queue:
    def __init__(self):
        self.front_node = None
        self.rear = None

    def enqueue(self, x):
        new = Node(x)
        if not self.rear:
            self.front_node = self.rear = new
            return
        self.rear.next = new
        self.rear = new

    def dequeue(self):
        if not self.front_node:
            return None
        val = self.front_node.data
        self.front_node = self.front_node.next
        if not self.front_node:
            self.rear = None
        return val

    def front(self):
        return self.front_node.data if self.front_node else None

def is_balanced(expr):
    stack = Stack()
    pairs = {')': '(', '}': '{', ']': '['}

    for ch in expr:
        if ch in "({[":
            stack.push(ch)
        elif ch in ")}]":
            if not stack.head or stack.pop() != pairs[ch]:
                return False

    return stack.head is None


if __name__ == "__main__":

    print("Dynamic Array:")
    da = DynamicArray()
    for i in range(10):
        da.append(i)
    da.print_array()
    print("Pop:", da.pop())
    da.print_array()

    print("\nSingly Linked List:")
    sll = SinglyLinkedList()
    sll.insert_begin(1)
    sll.insert_end(2)
    sll.insert_end(3)
    sll.traverse()
    sll.delete(2)
    sll.traverse()

    print("\nDoubly Linked List:")
    dll = DoublyLinkedList()
    dll.insert_end(10)
    dll.insert_end(20)
    dll.insert_end(30)
    dll.insert_after(20, 25)
    dll.traverse()
    dll.delete_pos(1)
    dll.traverse()

    print("\nStack:")
    st = Stack()
    st.push(10)
    st.push(20)
    print("Pop:", st.pop())

    print("\nQueue:")
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    print("Dequeue:", q.dequeue())

    print("\nBalanced Check:")
    print("([]):", is_balanced("([])"))
    print("([)]:", is_balanced("([)]"))