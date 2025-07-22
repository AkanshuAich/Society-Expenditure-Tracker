"""
Threading and concurrency issues
"""
import threading
import time

# Global variable without proper synchronization
shared_counter = 0
shared_data = {}

class UnsafeCounter:
    def __init__(self):
        self.count = 0
        self.lock = threading.Lock()  # Lock created but not used properly
    
    def increment(self):
        # Race condition - no synchronization
        current = self.count
        time.sleep(0.001)  # Simulates processing time
        self.count = current + 1
        
        # Depth 1 nesting
        return self.get_status()
    
    def get_status(self):
        return f"Count: {self.count}"
    
    def safe_increment(self):
        # Proper synchronization example
        with self.lock:
            self.count += 1
        return self.validate_count()
    
    def validate_count(self):
        # Depth 1 nesting
        return self.count > 0

class DataProcessor:
    def __init__(self):
        self.processing = False
        self.results = []
    
    def process_data(self, data_list):
        # Multiple threads might call this simultaneously
        if self.processing:
            return "Already processing"
        
        self.processing = True
        
        # Depth 1 nesting with race conditions
        results = self.parallel_process(data_list)
        
        self.processing = False
        return results
    
    def parallel_process(self, data):
        # Depth 2 nesting
        threads = []
        for item in data:
            thread = threading.Thread(target=self.process_item, args=(item,))
            threads.append(thread)
            thread.start()
        
        # Doesn't wait for threads to complete
        return self.collect_results()
    
    def process_item(self, item):
        # Modifies shared state without synchronization
        global shared_counter
        shared_counter += 1
        
        result = str(item).upper()
        self.results.append(result)  # Race condition on list
    
    def collect_results(self):
        return self.results.copy()

def create_deadlock():
    lock1 = threading.Lock()
    lock2 = threading.Lock()
    
    def worker1():
        with lock1:
            time.sleep(0.1)
            # Depth 1 nesting leading to deadlock
            return acquire_second_lock(lock2)
    
    def worker2():
        with lock2:
            time.sleep(0.1)
            # Depth 1 nesting leading to deadlock
            return acquire_first_lock(lock1)
    
    def acquire_second_lock(lock):
        with lock:
            return "Worker1 done"
    
    def acquire_first_lock(lock):
        with lock:
            return "Worker2 done"
    
    # Creates potential deadlock
    t1 = threading.Thread(target=worker1)
    t2 = threading.Thread(target=worker2)
    
    t1.start()
    t2.start()
    
    return t1, t2
