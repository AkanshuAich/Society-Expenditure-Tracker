"""
Runtime errors module with simplified call graphs (max depth 2)
Contains: IndexError, KeyError, TypeError, AttributeError, etc.
"""
import json
import datetime

class ErrorProneClass:
    """Class designed to generate runtime errors"""
    
    def __init__(self):
        self.data = [1, 2, 3]
        self.config = {'name': 'test', 'value': 42}
        self.nested_data = None
    
    def process_list_data(self, index):
        """Level 1 - Process list with potential IndexError"""
        return self._get_element_value(index)
    
    def _get_element_value(self, index):
        """Level 2 - Get element value (IndexError prone)"""
        # IndexError: list index out of range
        return self.data[index]  # No bounds checking
    
    def process_dict_data(self, key):
        """Level 1 - Process dictionary with potential KeyError"""
        return self._get_dict_element(key)
    
    def _get_dict_element(self, key):
        """Level 2 - Get dictionary element (KeyError prone)"""
        # KeyError: key not found
        return self.config[key]  # No key existence check
    
    def process_none_data(self):
        """Level 1 - Process None data (AttributeError prone)"""
        return self._call_none_method()
    
    def _call_none_method(self):
        """Level 2 - Call method on None (AttributeError)"""
        # AttributeError: 'NoneType' object has no attribute 'upper'
        return self.nested_data.upper()

class TypeErrorGenerator:
    """Class that generates type errors"""
    
    def concatenate_mixed_types(self, a, b):
        """Level 1 - Concatenate different types"""
        return self._perform_concatenation(a, b)
    
    def _perform_concatenation(self, x, y):
        """Level 2 - Perform concatenation"""
        return self._unsafe_concatenation(x, y)
    
    def _unsafe_concatenation(self, item1, item2):
        """Level 3 - Unsafe concatenation (TypeError prone)"""
        # TypeError: can't concatenate str and int
        return item1 + item2  # No type checking
    
    def divide_by_string(self, number, divisor):
        """Level 1 - Division with wrong types"""
        return self._calculate_division(number, divisor)
    
    def _calculate_division(self, num, div):
        """Level 2 - Calculate division"""
        return self._unsafe_division(num, div)
    
    def _unsafe_division(self, numerator, denominator):
        """Level 3 - Unsafe division (TypeError/ZeroDivisionError prone)"""
        # TypeError: unsupported operand type(s) for /: 'int' and 'str'
        # ZeroDivisionError: division by zero
        return numerator / denominator  # No type or zero checking

class RecursionErrorGenerator:
    """Class that generates recursion errors"""
    
    def start_infinite_recursion(self, value):
        """Level 1 - Start infinite recursion"""
        return self._recursive_function_1(value)
    
    def _recursive_function_1(self, val):
        """Level 2 - Recursive function 1"""
        return self._recursive_function_2(val)
    
    def _recursive_function_2(self, val):
        """Level 3 - Recursive function 2"""
        # RecursionError: maximum recursion depth exceeded
        return self._recursive_function_1(val)  # Infinite recursion

def function_with_value_error(text):
    """Function that generates ValueError"""
    return convert_to_number(text)

def convert_to_number(string_value):
    """Level 2 - Convert string to number"""
    return parse_integer(string_value)

def parse_integer(value):
    """Level 3 - Parse integer (ValueError prone)"""
    # ValueError: invalid literal for int() with base 10
    return int(value)  # No validation for non-numeric strings

def function_with_file_error(filename):
    """Function that generates FileNotFoundError"""
    return open_and_read_file(filename)

def open_and_read_file(file_path):
    """Level 2 - Open and read file"""
    return read_file_content(file_path)

def read_file_content(path):
    """Level 3 - Read file content (FileNotFoundError prone)"""
    # FileNotFoundError: No such file or directory
    with open(path, 'r') as f:  # No file existence check
        return f.read()

class UnboundLocalErrorGenerator:
    """Class that generates UnboundLocalError"""
    
    def process_with_unbound_local(self, condition):
        """Level 1 - Process with unbound local variable"""
        return self._check_condition(condition)
    
    def _check_condition(self, cond):
        """Level 2 - Check condition"""
        return self._handle_unbound_variable(cond)
    
    def _handle_unbound_variable(self, condition):
        """Level 3 - Handle unbound variable (UnboundLocalError prone)"""
        if condition:
            result = "initialized"
        
        # UnboundLocalError: local variable 'result' referenced before assignment
        return result  # 'result' not defined if condition is False

def function_with_import_error():
    """Function that generates ImportError"""
    return import_nonexistent_module()

def import_nonexistent_module():
    """Level 2 - Import nonexistent module"""
    return use_nonexistent_module()

def use_nonexistent_module():
    """Level 3 - Use nonexistent module (ImportError prone)"""
    # ImportError/ModuleNotFoundError: No module named 'nonexistent_module'
    import nonexistent_module
    return nonexistent_module.some_function()

# Global function that causes multiple errors
def error_cascade_function(data, index, key, filename):
    """Function that can cause multiple types of errors"""
    # This function calls multiple error-prone functions
    try:
        list_result = ErrorProneClass().process_list_data(index)
        dict_result = ErrorProneClass().process_dict_data(key)
        file_result = function_with_file_error(filename)
        type_result = TypeErrorGenerator().concatenate_mixed_types(data, index)
        
        return {
            'list': list_result,
            'dict': dict_result,
            'file': file_result,
            'type': type_result
        }
    except Exception as e:
        # Poor error handling - catching all exceptions
        return f"Error occurred: {str(e)}"
