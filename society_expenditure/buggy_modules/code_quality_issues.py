"""
Code quality issues module with nested call graphs
Contains: Long functions, code duplication, poor naming, etc.
"""
import datetime
import json

class DataProcessor:
    """Class with various code quality issues"""
    
    def __init__(self):
        self.data = []
        self.x = 0  # Poor variable naming
        self.temp = None
        self.flag = False
    
    def processData(self, input_data):  # Poor naming convention
        """Level 1 - Process data with quality issues"""
        return self.validateAndTransform(input_data)
    
    def validateAndTransform(self, data):
        """Level 2 - Long function with multiple responsibilities"""
        return self.doComplexProcessing(data)
    
    def doComplexProcessing(self, d):  # Poor parameter naming
        """Level 3 - Very long function with multiple issues"""
        # This function is way too long and does too many things
        result = []
        temp_var = None
        x = 0
        y = 0
        z = 0
        
        # Code duplication starts here
        if d is not None:
            if len(d) > 0:
                for item in d:
                    if item is not None:
                        if isinstance(item, dict):
                            if 'id' in item:
                                if item['id'] is not None:
                                    if item['id'] > 0:
                                        temp_var = item['id']
                                        x = temp_var * 2
                                        y = x + 1
                                        z = y * 3
                                        result.append({
                                            'processed_id': z,
                                            'original': item,
                                            'timestamp': datetime.datetime.now(),
                                            'processed_by': 'system'
                                        })
        
        # More code duplication
        if d is not None:
            if len(d) > 0:
                for item in d:
                    if item is not None:
                        if isinstance(item, dict):
                            if 'name' in item:
                                if item['name'] is not None:
                                    if len(item['name']) > 0:
                                        temp_var = item['name']
                                        x = len(temp_var)
                                        y = x + 1
                                        z = y * 2
                                        result.append({
                                            'processed_name': temp_var.upper(),
                                            'length': z,
                                            'original': item,
                                            'timestamp': datetime.datetime.now(),
                                            'processed_by': 'system'
                                        })
        
        return result

class UtilityFunctions:
    """Utility class with poor code quality"""
    
    def calculate_something(self, a, b, c, d, e, f, g, h):  # Too many parameters
        """Level 1 - Function with too many parameters"""
        return self.do_calculation(a, b, c, d, e, f, g, h)
    
    def do_calculation(self, a, b, c, d, e, f, g, h):
        """Level 2 - Complex calculation with poor structure"""
        return self.final_calculation(a, b, c, d, e, f, g, h)
    
    def final_calculation(self, a, b, c, d, e, f, g, h):
        """Level 3 - Final calculation with magic numbers"""
        # Magic numbers everywhere
        result = a * 3.14159 + b * 2.71828 - c * 1.41421
        result += d * 0.57721 - e * 1.61803 + f * 2.30258
        result *= g * 0.69314 + h * 1.20205
        
        # Nested conditions without clear logic
        if result > 100:
            if result < 200:
                if result % 2 == 0:
                    result = result * 1.5
                else:
                    result = result * 0.75
            else:
                if result > 500:
                    result = result / 2
                else:
                    result = result * 2
        
        return result

# Global variables (bad practice)
global_counter = 0
global_data = {}
global_flag = True

def function_with_globals():
    """Function that modifies global state"""
    global global_counter, global_data, global_flag
    global_counter += 1
    global_data[global_counter] = datetime.datetime.now()
    global_flag = not global_flag
    return process_global_data()

def process_global_data():
    """Level 2 - Process global data"""
    return manipulate_globals()

def manipulate_globals():
    """Level 3 - Manipulate global variables"""
    global global_counter, global_data
    # Poor error handling
    try:
        result = global_data[global_counter]
        return str(result)
    except:  # Bare except clause
        return "error"

# Duplicate code blocks
def duplicate_function_1(data):
    """Duplicate processing logic"""
    result = []
    for item in data:
        if item:
            processed = {
                'value': item * 2,
                'timestamp': datetime.datetime.now(),
                'processed': True
            }
            result.append(processed)
    return result

def duplicate_function_2(data):
    """Almost identical to duplicate_function_1"""
    result = []
    for item in data:
        if item:
            processed = {
                'value': item * 2,
                'timestamp': datetime.datetime.now(),
                'processed': True
            }
            result.append(processed)
    return result

# Poor class design
class BadDesign:
    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 3
        self.d = 4
        self.e = 5
        # Too many instance variables
    
    def method1(self):
        return self.method2()
    
    def method2(self):
        return self.method3()
    
    def method3(self):
        # Method that does everything
        return self.a + self.b + self.c + self.d + self.e
