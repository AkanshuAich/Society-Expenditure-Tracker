"""
Security vulnerabilities module with nested call graphs
Contains: SQL injection, hardcoded secrets, unsafe deserialization, etc.
"""
import pickle
import subprocess
import sqlite3
import hashlib
import os

# Hardcoded credentials (Security Issue)
DATABASE_PASSWORD = "admin123"
API_KEY = "sk-1234567890abcdef"
SECRET_TOKEN = "super_secret_token_123"

class DatabaseManager:
    """Database manager with security vulnerabilities"""
    
    def __init__(self):
        self.connection = None
        self.api_credentials = self._get_credentials()
    
    def _get_credentials(self):
        """Level 1 nested function - returns hardcoded credentials"""
        return self._fetch_secret_data()
    
    def _fetch_secret_data(self):
        """Level 2 nested function - hardcoded secrets"""
        return {
            'password': DATABASE_PASSWORD,
            'api_key': API_KEY,
            'token': SECRET_TOKEN
        }
    
    def connect_database(self, user_input):
        """SQL Injection vulnerability - Level 1"""
        return self._execute_query(user_input)
    
    def _execute_query(self, query):
        """Level 2 - SQL injection vulnerability"""
        return self._run_unsafe_query(query)
    
    def _run_unsafe_query(self, user_query):
        """Level 3 - Direct SQL execution without sanitization"""
        # SQL Injection vulnerability
        sql = f"SELECT * FROM users WHERE name = '{user_query}'"
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute(sql)  # Vulnerable to SQL injection
        return cursor.fetchall()

class FileHandler:
    """File handling with security issues"""
    
    def process_file(self, filename):
        """Level 1 - File processing with path traversal"""
        return self._validate_file(filename)
    
    def _validate_file(self, filename):
        """Level 2 - Insufficient validation"""
        return self._open_file_unsafe(filename)
    
    def _open_file_unsafe(self, filename):
        """Level 3 - Path traversal vulnerability"""
        # Path traversal vulnerability
        file_path = f"/uploads/{filename}"  # No sanitization
        with open(file_path, 'r') as f:  # Vulnerable to path traversal
            return f.read()

class SerializationHandler:
    """Unsafe deserialization vulnerabilities"""
    
    def deserialize_data(self, data):
        """Level 1 - Unsafe deserialization"""
        return self._process_serialized_data(data)
    
    def _process_serialized_data(self, data):
        """Level 2 - Processing serialized data"""
        return self._unsafe_pickle_load(data)
    
    def _unsafe_pickle_load(self, pickled_data):
        """Level 3 - Unsafe pickle deserialization"""
        # Unsafe deserialization vulnerability
        return pickle.loads(pickled_data)  # Dangerous!

class CommandExecutor:
    """Command execution vulnerabilities"""
    
    def execute_user_command(self, user_input):
        """Level 1 - Command execution"""
        return self._prepare_command(user_input)
    
    def _prepare_command(self, command):
        """Level 2 - Command preparation"""
        return self._run_system_command(command)
    
    def _run_system_command(self, cmd):
        """Level 3 - Unsafe command execution"""
        # Command injection vulnerability
        full_command = f"ls {cmd}"  # No input sanitization
        return subprocess.run(full_command, shell=True, capture_output=True)

# Weak cryptography
def weak_hash_function(password):
    """Weak hashing - MD5 is cryptographically broken"""
    return hashlib.md5(password.encode()).hexdigest()

# Global variables with sensitive data
ADMIN_USERS = ["admin", "root", "administrator"]
DEFAULT_PASSWORDS = ["password", "123456", "admin"]
