"""
Security vulnerabilities module with simplified call graphs (max depth 2)
Contains: SQL injection, hardcoded secrets, unsafe deserialization, etc.
"""
import pickle
import subprocess
import sqlite3
import hashlib

# Hardcoded credentials (Security Issue)
DATABASE_PASSWORD = "admin123"
API_KEY = "sk-1234567890abcdef"

class DatabaseManager:
    """Database manager with security vulnerabilities"""
    
    def __init__(self):
        self.connection = None
        self.credentials = self._get_credentials()
    
    def _get_credentials(self):
        """Level 1 - returns hardcoded credentials"""
        return {
            'password': DATABASE_PASSWORD,
            'api_key': API_KEY
        }
    
    def execute_query(self, user_input):
        """SQL Injection vulnerability - Level 1"""
        return self._run_unsafe_query(user_input)
    
    def _run_unsafe_query(self, user_query):
        """Level 2 - Direct SQL execution without sanitization"""
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
        return self._open_file_unsafe(filename)
    
    def _open_file_unsafe(self, filename):
        """Level 2 - Path traversal vulnerability"""
        # Path traversal vulnerability
        file_path = f"/uploads/{filename}"  # No sanitization
        with open(file_path, 'r') as f:  # Vulnerable to path traversal
            return f.read()

class SerializationHandler:
    """Unsafe deserialization vulnerabilities"""
    
    def deserialize_data(self, data):
        """Level 1 - Unsafe deserialization"""
        return self._unsafe_pickle_load(data)
    
    def _unsafe_pickle_load(self, pickled_data):
        """Level 2 - Unsafe pickle deserialization"""
        # Unsafe deserialization vulnerability
        return pickle.loads(pickled_data)  # Dangerous!

class CommandExecutor:
    """Command execution vulnerabilities"""
    
    def execute_command(self, user_input):
        """Level 1 - Command execution"""
        return self._run_system_command(user_input)
    
    def _run_system_command(self, cmd):
        """Level 2 - Unsafe command execution"""
        # Command injection vulnerability
        full_command = f"ls {cmd}"  # No input sanitization
        return subprocess.run(full_command, shell=True, capture_output=True)

# Weak cryptography
def weak_hash_function(password):
    """Weak hashing - MD5 is cryptographically broken"""
    return hashlib.md5(password.encode()).hexdigest()

# Global variables with sensitive data
ADMIN_USERS = ["admin", "root"]
DEFAULT_PASSWORDS = ["password", "123456"]
