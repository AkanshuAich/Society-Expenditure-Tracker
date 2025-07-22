"""
Error handling issues module with nested call graphs
Contains: Bare except clauses, swallowed exceptions, improper error handling, etc.
"""
import json
import os
import logging

class PoorErrorHandling:
    """Class with poor error handling practices"""
    
    def __init__(self):
        self.data = {}
        self.errors = []
    
    def process_json_data(self, json_string):
        """Level 1 - Process JSON data with poor error handling"""
        return self._parse_json(json_string)
    
    def _parse_json(self, json_str):
        """Level 2 - Parse JSON"""
        return self._unsafe_json_parsing(json_str)
    
    def _unsafe_json_parsing(self, data):
        """Level 3 - Unsafe JSON parsing"""
        try:
            result = json.loads(data)
            return result
        except:  # Bare except clause - catches everything!
            return {}  # Swallows all exceptions
    
    def file_operations_with_poor_handling(self, filename):
        """Level 1 - File operations with poor error handling"""
        return self._read_file_unsafe(filename)
    
    def _read_file_unsafe(self, file_path):
        """Level 2 - Read file unsafe"""
        return self._process_file_content(file_path)
    
    def _process_file_content(self, path):
        """Level 3 - Process file content with poor error handling"""
        try:
            with open(path, 'r') as f:
                content = f.read()
                return json.loads(content)
        except FileNotFoundError:
            pass  # Silent failure - no indication of error
        except PermissionError:
            pass  # Silent failure
        except json.JSONDecodeError:
            pass  # Silent failure
        except:
            pass  # Catches everything else and ignores it
        
        return None  # No way to distinguish between different errors

class ExceptionSwallowing:
    """Class that swallows exceptions inappropriately"""
    
    def divide_numbers(self, a, b):
        """Level 1 - Divide numbers with exception swallowing"""
        return self._perform_division(a, b)
    
    def _perform_division(self, numerator, denominator):
        """Level 2 - Perform division"""
        return self._unsafe_division(numerator, denominator)
    
    def _unsafe_division(self, num, den):
        """Level 3 - Unsafe division with swallowed exceptions"""
        try:
            result = num / den
            return result
        except ZeroDivisionError:
            # Swallows exception and returns misleading result
            return 0  # Should raise or return None/error indicator
        except TypeError:
            # Swallows type errors
            return 0
        except:
            # Catches and swallows everything else
            return 0
    
    def list_operations_with_swallowing(self, data, index):
        """Level 1 - List operations with exception swallowing"""
        return self._access_list_element(data, index)
    
    def _access_list_element(self, lst, idx):
        """Level 2 - Access list element"""
        return self._get_element_with_swallowing(lst, idx)
    
    def _get_element_with_swallowing(self, data, index):
        """Level 3 - Get element with exception swallowing"""
        try:
            return data[index]
        except IndexError:
            # Swallows IndexError - caller doesn't know what happened
            return None
        except TypeError:
            # Swallows TypeError if data is not subscriptable
            return None
        except:
            # Swallows all other exceptions
            return None

class IncorrectExceptionHandling:
    """Class with incorrect exception handling patterns"""
    
    def validate_and_process(self, data):
        """Level 1 - Validate and process with incorrect handling"""
        return self._validate_data(data)
    
    def _validate_data(self, input_data):
        """Level 2 - Validate data"""
        return self._process_with_wrong_exceptions(input_data)
    
    def _process_with_wrong_exceptions(self, data):
        """Level 3 - Process with wrong exception handling"""
        try:
            # Multiple operations that can fail in different ways
            result = []
            for item in data:
                processed = item.upper().strip()
                number = int(processed)
                result.append(number * 2)
            return result
        except ValueError as e:
            # Wrong: catching ValueError but handling as if it's a different error
            print(f"File not found: {e}")  # Misleading error message
            return []
        except AttributeError as e:
            # Wrong: catching AttributeError but handling incorrectly
            print(f"Network error: {e}")  # Misleading error message
            return []
        except Exception as e:
            # Too broad exception handling
            print(f"Unknown error: {e}")
            return []  # Doesn't re-raise or handle properly
    
    def database_operations_wrong_handling(self, query):
        """Level 1 - Database operations with wrong handling"""
        return self._execute_query(query)
    
    def _execute_query(self, sql):
        """Level 2 - Execute query"""
        return self._run_query_with_wrong_handling(sql)
    
    def _run_query_with_wrong_handling(self, query):
        """Level 3 - Run query with wrong exception handling"""
        import sqlite3
        
        try:
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            cursor.execute(query)
            results = cursor.fetchall()
            conn.close()
            return results
        except sqlite3.OperationalError as e:
            # Wrong: treating SQL errors as file errors
            print(f"File permission error: {e}")
            return []
        except sqlite3.IntegrityError as e:
            # Wrong: treating integrity errors as network errors
            print(f"Network timeout: {e}")
            return []
        except Exception as e:
            # Too broad - doesn't distinguish between different database errors
            print(f"General error: {e}")
            return []

class ResourceLeakInErrorHandling:
    """Class with resource leaks in error handling"""
    
    def process_multiple_files(self, filenames):
        """Level 1 - Process multiple files with resource leaks"""
        return self._open_and_process_files(filenames)
    
    def _open_and_process_files(self, files):
        """Level 2 - Open and process files"""
        return self._handle_files_with_leaks(files)
    
    def _handle_files_with_leaks(self, file_list):
        """Level 3 - Handle files with resource leaks"""
        results = []
        
        for filename in file_list:
            try:
                f = open(filename, 'r')  # File opened but not in try-finally
                content = f.read()
                processed = content.upper()
                results.append(processed)
                f.close()  # This won't execute if exception occurs above
            except FileNotFoundError:
                # File handle leaked if exception occurs after open()
                continue
            except PermissionError:
                # File handle leaked
                continue
            except:
                # File handle leaked for any other exception
                break
        
        return results
    
    def network_operations_with_leaks(self, urls):
        """Level 1 - Network operations with resource leaks"""
        return self._fetch_urls(urls)
    
    def _fetch_urls(self, url_list):
        """Level 2 - Fetch URLs"""
        return self._download_with_leaks(url_list)
    
    def _download_with_leaks(self, urls):
        """Level 3 - Download with resource leaks"""
        import urllib.request
        
        results = []
        for url in urls:
            try:
                response = urllib.request.urlopen(url)  # Connection opened
                data = response.read()
                results.append(data)
                response.close()  # Won't execute if exception occurs
            except urllib.error.URLError:
                # Connection leaked
                continue
            except urllib.error.HTTPError:
                # Connection leaked
                continue
            except:
                # Connection leaked
                break
        
        return results

class MisleadingErrorMessages:
    """Class with misleading error messages"""
    
    def authenticate_user(self, username, password):
        """Level 1 - Authenticate user with misleading errors"""
        return self._check_credentials(username, password)
    
    def _check_credentials(self, user, pwd):
        """Level 2 - Check credentials"""
        return self._validate_login(user, pwd)
    
    def _validate_login(self, username, password):
        """Level 3 - Validate login with misleading error messages"""
        valid_users = {'admin': 'password123', 'user': 'secret'}
        
        try:
            if username not in valid_users:
                # Security issue: reveals if username exists
                raise ValueError(f"Username '{username}' does not exist")
            
            if valid_users[username] != password:
                # Security issue: reveals that username exists but password is wrong
                raise ValueError(f"Incorrect password for user '{username}'")
            
            return True
        except ValueError as e:
            # Misleading: treating authentication errors as value errors
            print(f"Data validation error: {e}")
            return False
        except Exception as e:
            # Misleading: generic error message doesn't help debugging
            print(f"System error occurred during login")
            return False

# Global error handling functions with issues
def global_error_handler(func, *args, **kwargs):
    """Global error handler with poor practices"""
    return execute_with_poor_handling(func, *args, **kwargs)

def execute_with_poor_handling(function, *arguments, **keyword_args):
    """Level 2 - Execute with poor handling"""
    return run_function_unsafely(function, *arguments, **keyword_args)

def run_function_unsafely(fn, *args, **kwargs):
    """Level 3 - Run function unsafely"""
    try:
        return fn(*args, **kwargs)
    except:  # Bare except - catches everything including KeyboardInterrupt
        # Poor logging - no context about what failed
        logging.error("Something went wrong")
        return None  # Swallows all exceptions

class ExceptionChainBreaking:
    """Class that breaks exception chains"""
    
    def process_data_chain(self, data):
        """Level 1 - Process data with broken exception chain"""
        return self._transform_data(data)
    
    def _transform_data(self, input_data):
        """Level 2 - Transform data"""
        return self._break_exception_chain(input_data)
    
    def _break_exception_chain(self, data):
        """Level 3 - Break exception chain"""
        try:
            result = self._risky_operation(data)
            return result
        except Exception as e:
            # Breaks exception chain - loses original context
            raise ValueError("Data processing failed")  # Should use 'from e'
    
    def _risky_operation(self, data):
        """Risky operation that can fail"""
        return data / 0  # Will raise ZeroDivisionError
