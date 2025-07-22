"""
Security vulnerabilities - mixed nesting depths
Contains: SQL injection, hardcoded secrets, command injection
"""
import sqlite3
import subprocess
import hashlib

# Hardcoded credentials (Security Issue)
API_KEY = "sk-1234567890abcdef"

class DatabaseManager:
    """Database with SQL injection - depth 2 nesting"""
    
    def query_user(self, user_input):
        """SQL Injection vulnerability - depth 1"""
        return self._execute_unsafe_query(user_input)
    
    def _execute_unsafe_query(self, user_input):
        """SQL execution - depth 2"""
        # Bug: SQL injection
        sql = f"SELECT * FROM users WHERE name = '{user_input}'"
        conn = sqlite3.connect('database.db')
        return conn.execute(sql).fetchall()

class FileHandler:
    """File handler - depth 1 (direct call)"""
    
    def read_file(self, filename):
        """Path traversal vulnerability - depth 1"""
        # Bug: Path traversal
        file_path = f"/uploads/{filename}"
        with open(file_path, 'r') as f:
            return f.read()

class CommandExecutor:
    """Command executor - depth 2 nesting"""
    
    def run_command(self, cmd):
        """Command injection - depth 1"""
        return self._execute_system_command(cmd)
    
    def _execute_system_command(self, cmd):
        """System command execution - depth 2"""
        # Bug: Command injection
        return subprocess.run(f"ls {cmd}", shell=True)

# Weak hashing - depth 1 (direct function)
def hash_password(password):
    """Weak MD5 hashing - depth 1"""
    return hashlib.md5(password.encode()).hexdigest()
