"""
Nested functions and classes for call graph testing
"""

class Calculator:
    def __init__(self):
        self.history = []
    
    def calculate(self, operation, a, b):
        # Depth 1 nesting
        result = self.perform_operation(operation, a, b)
        self.save_to_history(operation, a, b, result)
        return result
    
    def perform_operation(self, op, x, y):
        # Depth 2 nesting
        if op == 'add':
            return self.add_numbers(x, y)
        elif op == 'multiply':
            return self.multiply_numbers(x, y)
        else:
            return self.handle_unknown_operation(op)
    
    def add_numbers(self, x, y):
        return x + y
    
    def multiply_numbers(self, x, y):
        return x * y
    
    def handle_unknown_operation(self, op):
        return 0
    
    def save_to_history(self, op, a, b, result):
        entry = f"{a} {op} {b} = {result}"
        self.history.append(entry)

class UserService:
    def __init__(self):
        self.users = {}
    
    def register_user(self, username, email):
        # Depth 1 nesting
        if self.validate_user_data(username, email):
            return self.create_user_account(username, email)
        return None
    
    def validate_user_data(self, username, email):
        # Depth 2 nesting
        return self.check_username(username) and self.check_email_format(email)
    
    def check_username(self, username):
        return len(username) >= 3
    
    def check_email_format(self, email):
        return '@' in email and '.' in email
    
    def create_user_account(self, username, email):
        user_id = len(self.users) + 1
        self.users[user_id] = {
            'username': username,
            'email': email,
            'active': True
        }
        return user_id

def process_order(order_data):
    # Depth 1 nesting
    validated_order = validate_order(order_data)
    if validated_order:
        return calculate_total(validated_order)
    return None

def validate_order(order):
    # Depth 2 nesting
    if check_order_items(order):
        return apply_discounts(order)
    return None

def check_order_items(order):
    return 'items' in order and len(order['items']) > 0

def apply_discounts(order):
    # Simple discount logic
    total = sum(item['price'] for item in order['items'])
    if total > 100:
        order['discount'] = 0.1
    return order

def calculate_total(order):
    subtotal = sum(item['price'] for item in order['items'])
    discount = order.get('discount', 0)
    return subtotal * (1 - discount)
