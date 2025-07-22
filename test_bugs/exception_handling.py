"""
Exception handling issues and bugs
"""

class DatabaseConnection:
    def __init__(self):
        self.connected = False
        self.connection = None
    
    def connect(self):
        # Poor exception handling
        try:
            self.connection = self.establish_connection()
            self.connected = True
        except:  # Bare except
            print("Connection failed")
            # Doesn't re-raise or handle properly
    
    def establish_connection(self):
        # Simulated connection that might fail
        import random
        if random.random() < 0.5:
            raise ConnectionError("Database unavailable")
        return "mock_connection"
    
    def query_data(self, sql):
        # Depth 1 nesting with poor error handling
        if not self.connected:
            raise RuntimeError("Not connected")
        
        return self.execute_query(sql)
    
    def execute_query(self, sql):
        # Depth 2 nesting
        try:
            result = self.run_sql(sql)
            return self.format_results(result)
        except Exception as e:
            # Swallows all exceptions
            return []
    
    def run_sql(self, sql):
        # Might raise various exceptions
        if "DROP" in sql.upper():
            raise PermissionError("Cannot drop tables")
        return ["mock", "data"]
    
    def format_results(self, data):
        return [str(item) for item in data]

def divide_numbers(a, b):
    # No exception handling for division by zero
    return a / b

def process_list(items):
    # Index errors not handled
    first = items[0]  # Crashes if empty list
    last = items[-1]
    
    # Depth 1 nesting with errors
    return calculate_difference(first, last)

def calculate_difference(x, y):
    # Type errors not handled
    return x - y  # Crashes if x, y are incompatible types

class FileManager:
    def __init__(self):
        self.files = {}
    
    def read_config(self, filename):
        # Multiple exception types not handled properly
        try:
            with open(filename) as f:
                content = f.read()
            return self.parse_config(content)
        except FileNotFoundError:
            return {}  # Silent failure
        # Other exceptions like PermissionError not caught
    
    def parse_config(self, content):
        # Depth 1 nesting with JSON errors
        import json
        data = json.loads(content)  # JSONDecodeError not handled
        return self.validate_config(data)
    
    def validate_config(self, config):
        # KeyError not handled
        required_keys = ['host', 'port', 'database']
        for key in required_keys:
            if config[key] is None:  # KeyError if key missing
                raise ValueError(f"Missing {key}")
        return config

def unsafe_conversion(value):
    # Multiple conversion errors possible
    as_int = int(value)  # ValueError if not numeric
    as_float = float(value)  # ValueError if not numeric
    
    # Depth 1 nesting
    return process_numbers(as_int, as_float)

def process_numbers(i, f):
    # Overflow not handled
    return i ** f  # Can cause OverflowError
