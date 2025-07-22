"""
Data structure and algorithm issues
"""

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def add_node(self, value):
        # Memory leak potential - nodes not properly managed
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            # Inefficient - traverses entire list
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        
        self.size += 1
        # Depth 1 nesting
        return self.validate_list()
    
    def validate_list(self):
        # Depth 2 nesting
        return self.check_integrity()
    
    def check_integrity(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
            if count > 1000:  # Infinite loop protection
                break
        return count == self.size

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  # Poor collision handling
    
    def hash_function(self, key):
        # Poor hash function
        return len(str(key)) % self.size
    
    def insert(self, key, value):
        # No duplicate key checking
        index = self.hash_function(key)
        self.table[index].append((key, value))
        
        # Depth 1 nesting
        return self.check_load_factor()
    
    def check_load_factor(self):
        # Doesn't actually resize when needed
        total_items = sum(len(bucket) for bucket in self.table)
        load_factor = total_items / self.size
        return load_factor < 0.75  # Returns boolean but doesn't act on it

def bubble_sort(arr):
    # Inefficient O(n²) sorting
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    # Depth 1 nesting
    return verify_sorted(arr)

def verify_sorted(arr):
    # Inefficient verification
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

class Stack:
    def __init__(self):
        self.items = []
        self.max_size = 100
    
    def push(self, item):
        # No overflow checking
        self.items.append(item)
        
        # Depth 1 nesting
        return self.update_statistics()
    
    def update_statistics(self):
        # Unnecessary computation on each push
        return {
            'size': len(self.items),
            'top': self.items[-1] if self.items else None,
            'is_full': len(self.items) >= self.max_size
        }
    
    def pop(self):
        # No underflow checking
        return self.items.pop()  # IndexError if empty
