"""
Memory leaks and performance issues module with nested call graphs
Contains: Memory leaks, infinite loops, inefficient algorithms, etc.
"""
import gc
import threading
import time

class MemoryLeakGenerator:
    """Class that generates memory leaks"""
    
    def __init__(self):
        self.data_store = []
        self.circular_refs = []
        self.thread_pool = []
    
    def create_memory_leak(self, size):
        """Level 1 - Create memory leak"""
        return self._allocate_memory(size)
    
    def _allocate_memory(self, amount):
        """Level 2 - Allocate memory without cleanup"""
        return self._infinite_allocation(amount)
    
    def _infinite_allocation(self, size):
        """Level 3 - Infinite memory allocation"""
        # Memory leak: continuously allocating without cleanup
        while True:
            large_data = [0] * size * 1000000  # Allocate large chunks
            self.data_store.append(large_data)  # Never cleaned up
            if len(self.data_store) > 100:
                break  # Eventually breaks but memory not freed
        return len(self.data_store)
    
    def create_circular_references(self, count):
        """Level 1 - Create circular references"""
        return self._build_circular_structure(count)
    
    def _build_circular_structure(self, num):
        """Level 2 - Build circular structure"""
        return self._link_objects_circularly(num)
    
    def _link_objects_circularly(self, count):
        """Level 3 - Link objects in circular manner"""
        # Circular reference memory leak
        objects = []
        for i in range(count):
            obj = {'id': i, 'data': [0] * 10000}
            objects.append(obj)
        
        # Create circular references
        for i in range(len(objects)):
            objects[i]['next'] = objects[(i + 1) % len(objects)]
            objects[i]['prev'] = objects[i - 1]
        
        self.circular_refs.extend(objects)
        return len(self.circular_refs)

class InfiniteLoopGenerator:
    """Class that generates infinite loops"""
    
    def start_infinite_processing(self, data):
        """Level 1 - Start infinite processing"""
        return self._begin_processing(data)
    
    def _begin_processing(self, input_data):
        """Level 2 - Begin processing"""
        return self._infinite_loop_processing(input_data)
    
    def _infinite_loop_processing(self, data):
        """Level 3 - Infinite loop processing"""
        # Infinite loop - never terminates
        counter = 0
        while True:  # No exit condition
            counter += 1
            processed = data * counter
            if counter > 1000000:  # This condition is never checked properly
                continue  # Continue instead of break
        return processed

class InefficientAlgorithms:
    """Class with inefficient algorithms"""
    
    def inefficient_search(self, data, target):
        """Level 1 - Inefficient search"""
        return self._perform_search(data, target)
    
    def _perform_search(self, dataset, item):
        """Level 2 - Perform search"""
        return self._nested_loop_search(dataset, item)
    
    def _nested_loop_search(self, data, target):
        """Level 3 - O(n^3) search algorithm"""
        # Extremely inefficient O(n^3) algorithm
        found_indices = []
        for i in range(len(data)):
            for j in range(len(data)):
                for k in range(len(data)):
                    if data[i] == target:
                        found_indices.append((i, j, k))
        return found_indices
    
    def inefficient_sorting(self, data):
        """Level 1 - Inefficient sorting"""
        return self._sort_data(data)
    
    def _sort_data(self, dataset):
        """Level 2 - Sort data"""
        return self._bubble_sort_worst_case(dataset)
    
    def _bubble_sort_worst_case(self, arr):
        """Level 3 - Worst case bubble sort O(n^2)"""
        # Inefficient bubble sort with unnecessary operations
        n = len(arr)
        for i in range(n):
            for j in range(n):  # Should be (n-i-1)
                for k in range(n):  # Unnecessary third loop
                    if j < n - 1 and arr[j] > arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

class ThreadLeakGenerator:
    """Class that generates thread leaks"""
    
    def create_thread_leak(self, count):
        """Level 1 - Create thread leak"""
        return self._spawn_threads(count)
    
    def _spawn_threads(self, num_threads):
        """Level 2 - Spawn threads"""
        return self._create_unmanaged_threads(num_threads)
    
    def _create_unmanaged_threads(self, count):
        """Level 3 - Create unmanaged threads"""
        # Thread leak: creating threads without proper cleanup
        for i in range(count):
            thread = threading.Thread(target=self._infinite_worker, args=(i,))
            thread.start()  # Never joined or cleaned up
            self.thread_pool.append(thread)
        return len(self.thread_pool)
    
    def _infinite_worker(self, worker_id):
        """Worker function that runs indefinitely"""
        while True:  # Infinite loop in thread
            time.sleep(0.1)
            # Simulate work but never exits

class ResourceLeakGenerator:
    """Class that generates resource leaks"""
    
    def leak_file_handles(self, file_count):
        """Level 1 - Leak file handles"""
        return self._open_files(file_count)
    
    def _open_files(self, count):
        """Level 2 - Open files"""
        return self._open_without_closing(count)
    
    def _open_without_closing(self, num_files):
        """Level 3 - Open files without closing"""
        # File handle leak: opening files without closing
        file_handles = []
        for i in range(num_files):
            try:
                # Creating temporary files but never closing them
                filename = f"/tmp/leak_file_{i}.txt"
                f = open(filename, 'w')  # Never closed
                f.write(f"Data for file {i}")
                file_handles.append(f)
            except:
                pass  # Ignore errors, making leak worse
        return len(file_handles)

# Global variables that grow indefinitely
global_cache = {}
global_history = []
global_connections = []

def add_to_global_cache(key, value):
    """Function that grows global cache indefinitely"""
    return update_cache_level_2(key, value)

def update_cache_level_2(k, v):
    """Level 2 - Update cache"""
    return final_cache_update(k, v)

def final_cache_update(key, value):
    """Level 3 - Final cache update (memory leak)"""
    global global_cache, global_history
    # Cache grows indefinitely - never cleaned
    global_cache[key] = value
    global_history.append((key, value, time.time()))
    # No cleanup mechanism
    return len(global_cache)

class DatabaseConnectionLeak:
    """Class that leaks database connections"""
    
    def __init__(self):
        self.connections = []
    
    def create_connection_leak(self, db_count):
        """Level 1 - Create connection leak"""
        return self._establish_connections(db_count)
    
    def _establish_connections(self, count):
        """Level 2 - Establish connections"""
        return self._open_db_connections(count)
    
    def _open_db_connections(self, num_connections):
        """Level 3 - Open database connections without closing"""
        import sqlite3
        # Database connection leak
        for i in range(num_connections):
            try:
                conn = sqlite3.connect(':memory:')  # Never closed
                cursor = conn.cursor()
                cursor.execute('CREATE TABLE test (id INTEGER)')
                self.connections.append(conn)
            except:
                pass  # Ignore errors
        return len(self.connections)
