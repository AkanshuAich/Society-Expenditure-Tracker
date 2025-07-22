"""
Security vulnerability examples for testing
"""
import os
import subprocess
import pickle

class DatabaseManager:
    def __init__(self):
        self.connection = None
    
    def connect_to_db(self, user_input):
        # SQL Injection vulnerability
        query = f"SELECT * FROM users WHERE name = '{user_input}'"
        return self.execute_query(query)
    
    def execute_query(self, query):
        # Simulated database execution
        print(f"Executing: {query}")
        return "result"

def execute_command(user_command):
    # Command injection vulnerability
    os.system(user_command)
    return subprocess.call(user_command, shell=True)

def load_user_data(file_path):
    # Unsafe deserialization
    with open(file_path, 'rb') as f:
        data = pickle.load(f)
    return data

class FileHandler:
    def read_file(self, filename):
        # Path traversal vulnerability
        with open(filename, 'r') as f:
            return f.read()
    
    def process_file(self, filename):
        content = self.read_file(filename)
        return self.analyze_content(content)
    
    def analyze_content(self, content):
        return len(content)

def main():
    db = DatabaseManager()
    handler = FileHandler()
    
    # Nested function calls (depth 1)
    result = db.connect_to_db("admin' OR '1'='1")
    
    # Nested function calls (depth 2)
    file_result = handler.process_file("../../../etc/passwd")
    
    return result, file_result
