"""
Performance bugs module with nested call graphs
Contains: Inefficient algorithms, memory issues, slow operations, etc.
"""
import time
import threading

class AlgorithmicComplexityBugs:
    """Class with algorithmic complexity issues"""
    
    def __init__(self):
        self.data = list(range(1000))
        self.cache = {}
    
    def inefficient_search(self, target):
        """Level 1 - Inefficient search with O(n^2) complexity"""
        return self._perform_nested_search(target)
    
    def _perform_nested_search(self, item):
        """Level 2 - Perform nested search"""
        return self._quadratic_search_algorithm(item)
    
    def _quadratic_search_algorithm(self, target):
        """Level 3 - O(n^2) search algorithm"""
        found_positions = []
        # Bug: Unnecessary nested loops - O(n^2) complexity
        for i in range(len(self.data)):
            for j in range(len(self.data)):
                if self.data[i] == target:
                    found_positions.append((i, j))
        return found_positions
    
    def slow_fibonacci(self, n):
        """Level 1 - Slow fibonacci with exponential complexity"""
        return self._calculate_fibonacci(n)
    
    def _calculate_fibonacci(self, num):
        """Level 2 - Calculate fibonacci"""
        return self._recursive_fibonacci(num)
    
    def _recursive_fibonacci(self, n):
        """Level 3 - Recursive fibonacci O(2^n) - extremely slow"""
        # Bug: Exponential time complexity - no memoization
        if n <= 1:
            return n
        return self._recursive_fibonacci(n-1) + self._recursive_fibonacci(n-2)
    
    def inefficient_sorting(self, data):
        """Level 1 - Inefficient sorting algorithm"""
        return self._sort_data_slowly(data)
    
    def _sort_data_slowly(self, dataset):
        """Level 2 - Sort data slowly"""
        return self._bubble_sort_worst_case(dataset)
    
    def _bubble_sort_worst_case(self, arr):
        """Level 3 - Bubble sort with worst case O(n^3)"""
        n = len(arr)
        # Bug: Triple nested loop - O(n^3) complexity
        for i in range(n):
            for j in range(n):
                for k in range(n-1):
                    if arr[k] > arr[k+1]:
                        arr[k], arr[k+1] = arr[k+1], arr[k]
        return arr

class MemoryLeakBugs:
    """Class with memory leak issues"""
    
    def __init__(self):
        self.growing_list = []
        self.circular_refs = []
    
    def create_memory_leak(self, iterations):
        """Level 1 - Create memory leak"""
        return self._allocate_memory_continuously(iterations)
    
    def _allocate_memory_continuously(self, count):
        """Level 2 - Allocate memory continuously"""
        return self._never_free_memory(count)
    
    def _never_free_memory(self, iterations):
        """Level 3 - Never free allocated memory"""
        # Bug: Continuously allocates memory without cleanup
        for i in range(iterations):
            # Bug: Large objects added to list, never removed
            large_object = [0] * 100000  # 100k integers
            self.growing_list.append(large_object)
            
            # Bug: Creates circular references
            obj1 = {'id': i, 'data': large_object}
            obj2 = {'id': i+1, 'ref': obj1}
            obj1['ref'] = obj2  # Circular reference
            self.circular_refs.append(obj1)
        
        return len(self.growing_list)
    
    def cache_without_limits(self, key, value):
        """Level 1 - Cache without limits"""
        return self._store_in_unlimited_cache(key, value)
    
    def _store_in_unlimited_cache(self, k, v):
        """Level 2 - Store in unlimited cache"""
        return self._add_to_growing_cache(k, v)
    
    def _add_to_growing_cache(self, key, value):
        """Level 3 - Add to growing cache (no size limit)"""
        # Bug: Cache grows indefinitely - no eviction policy
        if not hasattr(self, 'unlimited_cache'):
            self.unlimited_cache = {}
        
        # Bug: No size limit or TTL
        self.unlimited_cache[key] = {
            'value': value,
            'timestamp': time.time(),
            'access_count': 0
        }
        
        return len(self.unlimited_cache)

class IOPerformanceBugs:
    """Class with I/O performance issues"""
    
    def read_file_inefficiently(self, filename):
        """Level 1 - Read file inefficiently"""
        return self._process_file_slowly(filename)
    
    def _process_file_slowly(self, file_path):
        """Level 2 - Process file slowly"""
        return self._byte_by_byte_reading(file_path)
    
    def _byte_by_byte_reading(self, filename):
        """Level 3 - Read file byte by byte (extremely slow)"""
        content = ""
        try:
            with open(filename, 'r') as f:
                # Bug: Reading one character at a time - very slow
                while True:
                    char = f.read(1)  # Read one character
                    if not char:
                        break
                    content += char
                    # Bug: Unnecessary processing for each character
                    time.sleep(0.001)  # Artificial delay
        except FileNotFoundError:
            pass
        
        return content
    
    def write_file_inefficiently(self, filename, data):
        """Level 1 - Write file inefficiently"""
        return self._save_file_slowly(filename, data)
    
    def _save_file_slowly(self, file_path, content):
        """Level 2 - Save file slowly"""
        return self._character_by_character_writing(file_path, content)
    
    def _character_by_character_writing(self, filename, data):
        """Level 3 - Write file character by character"""
        try:
            with open(filename, 'w') as f:
                # Bug: Writing one character at a time - very slow
                for char in data:
                    f.write(char)
                    f.flush()  # Bug: Flush after every character
                    time.sleep(0.001)  # Artificial delay
        except IOError:
            return False
        
        return True

class DatabasePerformanceBugs:
    """Class with database performance issues"""
    
    def __init__(self):
        self.query_results = []
    
    def query_without_indexes(self, table_name, search_value):
        """Level 1 - Query without indexes"""
        return self._perform_full_table_scan(table_name, search_value)
    
    def _perform_full_table_scan(self, table, value):
        """Level 2 - Perform full table scan"""
        return self._inefficient_database_query(table, value)
    
    def _inefficient_database_query(self, table_name, search_term):
        """Level 3 - Inefficient database query"""
        # Bug: Simulates N+1 query problem
        results = []
        
        # Bug: Multiple individual queries instead of JOIN
        for i in range(1000):  # Simulate 1000 records
            # Bug: Individual query for each record
            query_result = f"SELECT * FROM {table_name} WHERE id = {i}"
            
            # Bug: Another query for related data
            related_query = f"SELECT * FROM related_table WHERE foreign_id = {i}"
            
            # Bug: Yet another query for additional data
            extra_query = f"SELECT * FROM extra_table WHERE ref_id = {i}"
            
            results.append({
                'main': query_result,
                'related': related_query,
                'extra': extra_query
            })
        
        return results
    
    def batch_operations_inefficiently(self, operations):
        """Level 1 - Batch operations inefficiently"""
        return self._process_operations_individually(operations)
    
    def _process_operations_individually(self, ops):
        """Level 2 - Process operations individually"""
        return self._execute_one_by_one(ops)
    
    def _execute_one_by_one(self, operations):
        """Level 3 - Execute operations one by one"""
        results = []
        
        # Bug: Processes batch operations individually
        for operation in operations:
            # Bug: Individual transaction for each operation
            result = self._single_operation_transaction(operation)
            results.append(result)
            
            # Bug: Artificial delay between operations
            time.sleep(0.01)
        
        return results
    
    def _single_operation_transaction(self, operation):
        """Helper method for single operation"""
        # Simulate database operation
        return f"Executed: {operation}"

# Global performance utility functions with bugs
def process_large_dataset(data):
    """Global function to process large dataset inefficiently"""
    return transform_data_slowly(data)

def transform_data_slowly(dataset):
    """Level 2 - Transform data slowly"""
    return apply_inefficient_transformations(dataset)

def apply_inefficient_transformations(data):
    """Level 3 - Apply inefficient transformations"""
    results = []
    
    # Bug: Nested loops for simple transformation - O(n^2)
    for i, item in enumerate(data):
        transformed_item = item
        
        # Bug: Unnecessary nested loop
        for j in range(len(data)):
            if i == j:
                # Bug: Expensive operation in inner loop
                transformed_item = str(item).upper().lower().strip()
                time.sleep(0.001)  # Artificial delay
        
        results.append(transformed_item)
    
    return results

def calculate_statistics_slowly(numbers):
    """Global function to calculate statistics slowly"""
    return compute_stats_inefficiently(numbers)

def compute_stats_inefficiently(data):
    """Level 2 - Compute stats inefficiently"""
    return slow_statistical_calculations(data)

def slow_statistical_calculations(numbers):
    """Level 3 - Slow statistical calculations"""
    # Bug: Recalculates everything multiple times
    stats = {}
    
    # Bug: Multiple passes through data instead of single pass
    stats['count'] = len(numbers)
    
    # Bug: Inefficient sum calculation
    total = 0
    for num in numbers:
        total += num
    stats['sum'] = total
    
    # Bug: Inefficient average calculation
    average = 0
    for num in numbers:
        average += num
    stats['average'] = average / len(numbers)
    
    # Bug: Inefficient min/max calculation
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    stats['min'] = minimum
    
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    stats['max'] = maximum
    
    return stats
