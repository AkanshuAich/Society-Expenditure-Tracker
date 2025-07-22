"""
Performance and efficiency issues
"""

class SlowProcessor:
    def __init__(self):
        self.data = []
        self.cache = {}
    
    def process_large_dataset(self, items):
        # Inefficient nested loops - O(n²)
        results = []
        for i in items:
            for j in items:
                if i != j:
                    # Depth 1 nesting
                    comparison = self.compare_items(i, j)
                    results.append(comparison)
        return results
    
    def compare_items(self, item1, item2):
        # Depth 2 nesting with inefficient operations
        return self.expensive_calculation(item1) + self.expensive_calculation(item2)
    
    def expensive_calculation(self, item):
        # Simulates expensive operation without caching
        result = 0
        for i in range(1000):
            result += hash(str(item) + str(i))
        return result

def inefficient_search(data, target):
    # Linear search instead of using built-in optimized methods
    found_indices = []
    for i in range(len(data)):
        if data[i] == target:
            found_indices.append(i)
    
    # Depth 1 nesting
    return validate_results(found_indices)

def validate_results(indices):
    # Unnecessary processing
    return [i for i in indices if i >= 0]

class StringProcessor:
    def __init__(self):
        self.processed = []
    
    def process_strings(self, string_list):
        # Inefficient string concatenation
        result = ""
        for s in string_list:
            result += s + " "  # Creates new string each time
        
        # Depth 1 nesting
        return self.finalize_string(result)
    
    def finalize_string(self, text):
        # More inefficient operations
        return text.strip().upper().lower().strip()

def memory_intensive_operation(size):
    # Creates unnecessary large data structures
    large_list = []
    for i in range(size):
        # Each iteration creates a new list
        temp_list = [j for j in range(i)]
        large_list.append(temp_list)
    
    # Depth 1 nesting
    return process_large_structure(large_list)

def process_large_structure(data):
    # Inefficient processing of large data
    flattened = []
    for sublist in data:
        for item in sublist:
            flattened.append(item)
    return flattened
