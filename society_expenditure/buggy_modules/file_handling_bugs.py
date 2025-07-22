"""
File handling bugs module with nested call graphs
Contains: Path traversal, file leaks, encoding issues, etc.
"""
import os
import shutil
import json
import csv

class FileHandlingBugs:
    """Class with file handling issues"""
    
    def __init__(self):
        self.temp_files = []
        self.open_handles = []
    
    def read_user_file(self, filename):
        """Level 1 - Read user file with path traversal"""
        return self._open_file_unsafe(filename)
    
    def _open_file_unsafe(self, file_path):
        """Level 2 - Open file unsafe"""
        return self._read_file_content(file_path)
    
    def _read_file_content(self, path):
        """Level 3 - Read file content (path traversal vulnerability)"""
        # Bug: No path validation - vulnerable to path traversal
        full_path = f"/uploads/{path}"  # User can use ../../../etc/passwd
        
        try:
            with open(full_path, 'r') as f:  # Vulnerable to path traversal
                return f.read()
        except (FileNotFoundError, PermissionError):
            return ""
    
    def write_user_data(self, filename, data):
        """Level 1 - Write user data with bugs"""
        return self._prepare_file_write(filename, data)
    
    def _prepare_file_write(self, file_name, content):
        """Level 2 - Prepare file write"""
        return self._unsafe_file_write(file_name, content)
    
    def _unsafe_file_write(self, filename, data):
        """Level 3 - Unsafe file write (multiple bugs)"""
        # Bug: No filename validation
        file_path = f"/tmp/{filename}"  # Can overwrite system files
        
        try:
            # Bug: File handle not properly closed on exception
            f = open(file_path, 'w')
            f.write(data)
            f.close()  # Won't execute if exception occurs above
            return True
        except Exception:
            # Bug: File handle leaked if exception occurs
            return False
    
    def process_csv_file(self, csv_path):
        """Level 1 - Process CSV file with bugs"""
        return self._read_csv_data(csv_path)
    
    def _read_csv_data(self, file_path):
        """Level 2 - Read CSV data"""
        return self._parse_csv_content(file_path)
    
    def _parse_csv_content(self, path):
        """Level 3 - Parse CSV content (encoding and error bugs)"""
        try:
            # Bug: No encoding specified - will fail on non-ASCII
            with open(path, 'r') as f:  # Should specify encoding='utf-8'
                reader = csv.reader(f)
                data = []
                for row in reader:
                    data.append(row)
                return data
        except UnicodeDecodeError:
            # Bug: Returns empty list instead of proper error handling
            return []
        except Exception:
            return []

class FileResourceLeaks:
    """Class with file resource leaks"""
    
    def batch_file_processing(self, file_list):
        """Level 1 - Batch file processing with leaks"""
        return self._process_multiple_files(file_list)
    
    def _process_multiple_files(self, files):
        """Level 2 - Process multiple files"""
        return self._handle_file_batch(files)
    
    def _handle_file_batch(self, file_paths):
        """Level 3 - Handle file batch (resource leaks)"""
        results = []
        
        for file_path in file_paths:
            try:
                # Bug: File opened but not guaranteed to be closed
                f = open(file_path, 'r')
                content = f.read()
                processed = content.upper()
                results.append(processed)
                # Bug: f.close() not in finally block
                f.close()
            except FileNotFoundError:
                # Bug: File handle leaked if exception occurs after open
                continue
            except Exception:
                # Bug: File handle leaked
                break
        
        return results
    
    def create_temp_files(self, count):
        """Level 1 - Create temp files with leaks"""
        return self._generate_temp_files(count)
    
    def _generate_temp_files(self, num_files):
        """Level 2 - Generate temp files"""
        return self._create_temporary_files(num_files)
    
    def _create_temporary_files(self, count):
        """Level 3 - Create temporary files (never cleaned up)"""
        import tempfile
        
        temp_files = []
        for i in range(count):
            try:
                # Bug: Temporary files created but never cleaned up
                temp_file = tempfile.NamedTemporaryFile(delete=False)
                temp_file.write(f"Temp data {i}".encode())
                temp_file.close()  # File closed but not deleted
                temp_files.append(temp_file.name)
            except Exception:
                continue
        
        # Bug: No cleanup mechanism for temp files
        return temp_files

class DirectoryTraversalBugs:
    """Class with directory traversal vulnerabilities"""
    
    def list_directory_contents(self, dir_path):
        """Level 1 - List directory with traversal bugs"""
        return self._scan_directory(dir_path)
    
    def _scan_directory(self, directory):
        """Level 2 - Scan directory"""
        return self._unsafe_directory_listing(directory)
    
    def _unsafe_directory_listing(self, path):
        """Level 3 - Unsafe directory listing (traversal vulnerability)"""
        # Bug: No path validation - can access any directory
        base_dir = "/app/uploads"
        full_path = os.path.join(base_dir, path)  # Still vulnerable
        
        try:
            # Bug: Can list contents of any directory
            return os.listdir(full_path)
        except (FileNotFoundError, PermissionError):
            return []
    
    def delete_user_file(self, filename):
        """Level 1 - Delete user file with traversal risk"""
        return self._remove_file(filename)
    
    def _remove_file(self, file_name):
        """Level 2 - Remove file"""
        return self._unsafe_file_deletion(file_name)
    
    def _unsafe_file_deletion(self, filename):
        """Level 3 - Unsafe file deletion (traversal vulnerability)"""
        # Bug: No filename validation - can delete any file
        file_path = f"/uploads/{filename}"  # User can use ../../../important_file
        
        try:
            os.remove(file_path)  # Dangerous - can delete system files
            return True
        except (FileNotFoundError, PermissionError):
            return False
    
    def copy_user_file(self, source, destination):
        """Level 1 - Copy user file with traversal bugs"""
        return self._perform_file_copy(source, destination)
    
    def _perform_file_copy(self, src, dest):
        """Level 2 - Perform file copy"""
        return self._unsafe_file_copy(src, dest)
    
    def _unsafe_file_copy(self, source, destination):
        """Level 3 - Unsafe file copy (double traversal vulnerability)"""
        # Bug: Both source and destination vulnerable to traversal
        src_path = f"/uploads/{source}"
        dest_path = f"/uploads/{destination}"
        
        try:
            # Bug: Can copy from/to any location on filesystem
            shutil.copy2(src_path, dest_path)
            return True
        except (FileNotFoundError, PermissionError, shutil.Error):
            return False

class FilePermissionBugs:
    """Class with file permission issues"""
    
    def create_file_with_permissions(self, filename, content):
        """Level 1 - Create file with permission bugs"""
        return self._setup_file_permissions(filename, content)
    
    def _setup_file_permissions(self, file_name, data):
        """Level 2 - Setup file permissions"""
        return self._create_file_insecure(file_name, data)
    
    def _create_file_insecure(self, filename, content):
        """Level 3 - Create file insecure (permission bugs)"""
        file_path = f"/tmp/{filename}"
        
        try:
            # Bug: Creates file with overly permissive permissions
            with open(file_path, 'w') as f:
                f.write(content)
            
            # Bug: Sets world-writable permissions (777)
            os.chmod(file_path, 0o777)  # Dangerous permissions
            return True
        except Exception:
            return False
    
    def backup_sensitive_data(self, data):
        """Level 1 - Backup sensitive data with permission bugs"""
        return self._create_backup_file(data)
    
    def _create_backup_file(self, sensitive_data):
        """Level 2 - Create backup file"""
        return self._write_backup_insecure(sensitive_data)
    
    def _write_backup_insecure(self, data):
        """Level 3 - Write backup insecure (permission bugs)"""
        backup_path = "/tmp/sensitive_backup.txt"
        
        try:
            # Bug: Sensitive data written with default permissions
            with open(backup_path, 'w') as f:
                f.write(json.dumps(data))
            
            # Bug: No permission restriction on sensitive file
            # File is readable by all users
            return backup_path
        except Exception:
            return None

# Global file utility functions with bugs
def read_config_file(config_path):
    """Global function to read config with bugs"""
    return load_configuration_data(config_path)

def load_configuration_data(file_path):
    """Level 2 - Load configuration data"""
    return parse_config_file(file_path)

def parse_config_file(path):
    """Level 3 - Parse config file (multiple bugs)"""
    try:
        # Bug: No path validation
        # Bug: No encoding specification
        # Bug: File handle not properly managed
        f = open(path, 'r')
        content = f.read()
        f.close()
        
        # Bug: Assumes file is always JSON
        return json.loads(content)
    except Exception:
        # Bug: Returns empty dict instead of proper error
        return {}

def write_log_entry(message, log_file="/var/log/app.log"):
    """Global function to write log with bugs"""
    return append_to_log_file(message, log_file)

def append_to_log_file(msg, file_path):
    """Level 2 - Append to log file"""
    return unsafe_log_write(msg, file_path)

def unsafe_log_write(message, log_path):
    """Level 3 - Unsafe log write (multiple bugs)"""
    try:
        # Bug: No log rotation - file grows indefinitely
        # Bug: No file locking - concurrent writes can corrupt
        # Bug: File handle not properly closed on exception
        f = open(log_path, 'a')
        f.write(f"{message}\n")
        f.close()
        return True
    except Exception:
        # Bug: Swallows all exceptions
        return False
