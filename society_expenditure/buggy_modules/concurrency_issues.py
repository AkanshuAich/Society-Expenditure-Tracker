"""
Concurrency issues module with nested call graphs
Contains: Race conditions, deadlocks, thread safety issues, etc.
"""
import threading
import time
import queue
import random

class RaceConditionGenerator:
    """Class that generates race conditions"""
    
    def __init__(self):
        self.shared_counter = 0
        self.shared_data = {}
        self.lock = threading.Lock()  # Lock exists but not used properly
    
    def start_race_condition(self, thread_count):
        """Level 1 - Start race condition scenario"""
        return self._create_competing_threads(thread_count)
    
    def _create_competing_threads(self, count):
        """Level 2 - Create competing threads"""
        return self._launch_unsafe_threads(count)
    
    def _launch_unsafe_threads(self, num_threads):
        """Level 3 - Launch threads with race conditions"""
        threads = []
        for i in range(num_threads):
            thread = threading.Thread(target=self._unsafe_counter_increment)
            threads.append(thread)
            thread.start()
        
        # Wait for all threads but race condition occurs
        for thread in threads:
            thread.join()
        
        return self.shared_counter
    
    def _unsafe_counter_increment(self):
        """Unsafe counter increment causing race condition"""
        for _ in range(1000):
            # Race condition: no synchronization
            temp = self.shared_counter
            time.sleep(0.0001)  # Simulate processing time
            self.shared_counter = temp + 1  # Lost updates possible

class DeadlockGenerator:
    """Class that generates deadlocks"""
    
    def __init__(self):
        self.lock1 = threading.Lock()
        self.lock2 = threading.Lock()
        self.resource1 = 0
        self.resource2 = 0
    
    def create_deadlock_scenario(self):
        """Level 1 - Create deadlock scenario"""
        return self._setup_deadlock_threads()
    
    def _setup_deadlock_threads(self):
        """Level 2 - Setup deadlock threads"""
        return self._start_deadlocking_operations()
    
    def _start_deadlocking_operations(self):
        """Level 3 - Start operations that cause deadlock"""
        thread1 = threading.Thread(target=self._operation_a)
        thread2 = threading.Thread(target=self._operation_b)
        
        thread1.start()
        thread2.start()
        
        # These threads will deadlock
        thread1.join(timeout=5)  # Will timeout due to deadlock
        thread2.join(timeout=5)  # Will timeout due to deadlock
        
        return "Deadlock scenario completed"
    
    def _operation_a(self):
        """Operation A - acquires lock1 then lock2"""
        with self.lock1:
            time.sleep(0.1)  # Hold lock1
            with self.lock2:  # Try to acquire lock2 (deadlock!)
                self.resource1 += 1
    
    def _operation_b(self):
        """Operation B - acquires lock2 then lock1"""
        with self.lock2:
            time.sleep(0.1)  # Hold lock2
            with self.lock1:  # Try to acquire lock1 (deadlock!)
                self.resource2 += 1

class ThreadSafetyIssues:
    """Class with thread safety issues"""
    
    def __init__(self):
        self.unsafe_list = []
        self.unsafe_dict = {}
        self.counter = 0
    
    def concurrent_list_operations(self, thread_count):
        """Level 1 - Concurrent list operations"""
        return self._perform_list_operations(thread_count)
    
    def _perform_list_operations(self, count):
        """Level 2 - Perform list operations"""
        return self._unsafe_list_modifications(count)
    
    def _unsafe_list_modifications(self, num_threads):
        """Level 3 - Unsafe list modifications"""
        threads = []
        for i in range(num_threads):
            thread = threading.Thread(target=self._modify_shared_list, args=(i,))
            threads.append(thread)
            thread.start()
        
        for thread in threads:
            thread.join()
        
        return len(self.unsafe_list)
    
    def _modify_shared_list(self, thread_id):
        """Modify shared list without synchronization"""
        for i in range(100):
            # Thread-unsafe operations
            self.unsafe_list.append(f"thread_{thread_id}_item_{i}")
            if len(self.unsafe_list) > 50:
                try:
                    self.unsafe_list.pop(0)  # Race condition possible
                except IndexError:
                    pass  # List might be empty due to race condition

class ProducerConsumerBugs:
    """Class with producer-consumer bugs"""
    
    def __init__(self):
        self.buffer = queue.Queue(maxsize=10)
        self.produced_count = 0
        self.consumed_count = 0
    
    def start_producer_consumer(self, producers, consumers):
        """Level 1 - Start producer-consumer scenario"""
        return self._setup_producers_consumers(producers, consumers)
    
    def _setup_producers_consumers(self, prod_count, cons_count):
        """Level 2 - Setup producers and consumers"""
        return self._launch_buggy_workers(prod_count, cons_count)
    
    def _launch_buggy_workers(self, num_producers, num_consumers):
        """Level 3 - Launch buggy producer-consumer workers"""
        threads = []
        
        # Start producers
        for i in range(num_producers):
            thread = threading.Thread(target=self._buggy_producer, args=(i,))
            threads.append(thread)
            thread.start()
        
        # Start consumers
        for i in range(num_consumers):
            thread = threading.Thread(target=self._buggy_consumer, args=(i,))
            threads.append(thread)
            thread.start()
        
        # Wait for threads
        for thread in threads:
            thread.join(timeout=2)  # Short timeout causes issues
        
        return f"Produced: {self.produced_count}, Consumed: {self.consumed_count}"
    
    def _buggy_producer(self, producer_id):
        """Buggy producer with race conditions"""
        for i in range(20):
            try:
                item = f"producer_{producer_id}_item_{i}"
                self.buffer.put(item, timeout=0.1)  # Short timeout
                # Race condition on counter
                temp = self.produced_count
                time.sleep(0.001)
                self.produced_count = temp + 1
            except queue.Full:
                break  # Give up too easily
    
    def _buggy_consumer(self, consumer_id):
        """Buggy consumer with race conditions"""
        while True:
            try:
                item = self.buffer.get(timeout=0.1)  # Short timeout
                # Simulate processing
                time.sleep(random.uniform(0.01, 0.05))
                # Race condition on counter
                temp = self.consumed_count
                time.sleep(0.001)
                self.consumed_count = temp + 1
                self.buffer.task_done()
            except queue.Empty:
                break  # Exit too early

class AtomicityViolations:
    """Class with atomicity violations"""
    
    def __init__(self):
        self.account_balance = 1000
        self.transaction_log = []
    
    def perform_transfers(self, transfer_count):
        """Level 1 - Perform money transfers"""
        return self._execute_transfers(transfer_count)
    
    def _execute_transfers(self, count):
        """Level 2 - Execute transfers"""
        return self._concurrent_money_transfers(count)
    
    def _concurrent_money_transfers(self, num_transfers):
        """Level 3 - Concurrent money transfers (atomicity violation)"""
        threads = []
        for i in range(num_transfers):
            amount = random.randint(10, 100)
            thread = threading.Thread(target=self._transfer_money, args=(amount,))
            threads.append(thread)
            thread.start()
        
        for thread in threads:
            thread.join()
        
        return self.account_balance
    
    def _transfer_money(self, amount):
        """Transfer money without atomic operations"""
        # Non-atomic operation - can be interrupted
        if self.account_balance >= amount:
            time.sleep(0.001)  # Simulate processing delay
            old_balance = self.account_balance
            time.sleep(0.001)  # More delay - atomicity violation
            self.account_balance = old_balance - amount
            
            # Log transaction (also non-atomic)
            self.transaction_log.append({
                'amount': amount,
                'balance_after': self.account_balance,
                'timestamp': time.time()
            })

# Global shared state without proper synchronization
global_shared_state = {
    'counter': 0,
    'data': [],
    'flags': {}
}

def unsafe_global_update(key, value):
    """Function that unsafely updates global state"""
    return modify_global_state(key, value)

def modify_global_state(k, v):
    """Level 2 - Modify global state"""
    return final_global_update(k, v)

def final_global_update(key, value):
    """Level 3 - Final global update (race condition prone)"""
    global global_shared_state
    
    # Race condition: non-atomic read-modify-write
    current_counter = global_shared_state['counter']
    time.sleep(0.001)  # Simulate processing
    global_shared_state['counter'] = current_counter + 1
    
    # More race conditions
    global_shared_state['data'].append(value)
    global_shared_state['flags'][key] = True
    
    return global_shared_state['counter']
