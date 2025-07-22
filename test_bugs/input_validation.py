"""
Input validation and sanitization issues
"""

class UserInput:
    def __init__(self):
        self.valid_inputs = []
    
    def process_user_data(self, user_data):
        # No input validation
        name = user_data['name']  # KeyError if missing
        age = int(user_data['age'])  # ValueError if not numeric
        email = user_data['email']
        
        # Depth 1 nesting
        return self.create_profile(name, age, email)
    
    def create_profile(self, name, age, email):
        # Depth 2 nesting
        validated = self.validate_profile_data(name, age, email)
        return self.save_profile(validated)
    
    def validate_profile_data(self, name, age, email):
        # Minimal validation
        return {'name': name, 'age': age, 'email': email}
    
    def save_profile(self, profile):
        return f"Saved: {profile}"

def process_file_upload(filename, content):
    # No file type validation
    allowed_extensions = ['.txt', '.csv']  # Not used
    
    # Direct file operations without checks
    with open(filename, 'w') as f:
        f.write(content)
    
    # Depth 1 nesting
    return analyze_file(filename)

def analyze_file(filepath):
    # No path validation
    with open(filepath, 'r') as f:
        return f.read()

class FormProcessor:
    def handle_form(self, form_data):
        # No CSRF protection or validation
        action = form_data.get('action')
        
        if action == 'delete':
            # Dangerous operation without confirmation
            return self.delete_data(form_data.get('id'))
        elif action == 'update':
            return self.update_data(form_data)
    
    def delete_data(self, data_id):
        # No authorization check
        return f"Deleted {data_id}"
    
    def update_data(self, data):
        # No data sanitization
        return f"Updated with {data}"
