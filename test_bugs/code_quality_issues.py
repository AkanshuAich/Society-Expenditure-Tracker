"""
Code quality issues for testing
"""

# Global variables (bad practice)
GLOBAL_COUNTER = 0
user_data = {}

class UserManager:
    def __init__(self):
        self.users = []
        
    def add_user(self, name, age, email):
        # Long parameter list
        user = {
            'name': name,
            'age': age, 
            'email': email,
            'created_at': None,
            'updated_at': None,
            'status': 'active'
        }
        self.users.append(user)
        return self.validate_user(user)
    
    def validate_user(self, user):
        # Nested validation calls (depth 1)
        if self.check_name(user['name']):
            return self.check_email(user['email'])
        return False
    
    def check_name(self, name):
        return len(name) > 0
    
    def check_email(self, email):
        return '@' in email

def process_data(data):
    # Too many nested if statements
    if data:
        if isinstance(data, dict):
            if 'users' in data:
                if len(data['users']) > 0:
                    if data['users'][0]:
                        return True
    return False

def calculate_something(x, y, z, a, b, c, d, e):
    # Too many parameters
    global GLOBAL_COUNTER
    GLOBAL_COUNTER += 1
    
    # Complex nested calculation (depth 2)
    result = complex_math(x, y)
    return final_calculation(result, z, a, b, c, d, e)

def complex_math(x, y):
    return advanced_operation(x * y)

def advanced_operation(value):
    return value ** 2

def final_calculation(base, *args):
    return sum(args) + base

class DataProcessor:
    def __init__(self):
        self.data = None
        
    def process(self, input_data):
        # Method too long
        self.data = input_data
        if not self.data:
            return None
        
        processed = []
        for item in self.data:
            if item:
                if isinstance(item, str):
                    processed.append(item.upper())
                elif isinstance(item, int):
                    processed.append(item * 2)
                elif isinstance(item, list):
                    for subitem in item:
                        processed.append(str(subitem))
                else:
                    processed.append(str(item))
        
        return self.finalize_processing(processed)
    
    def finalize_processing(self, data):
        return [item for item in data if item]
