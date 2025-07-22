"""
Data validation bugs module with nested call graphs
Contains: Input validation issues, data sanitization problems, type checking errors, etc.
"""
import re
import datetime
import json

class InputValidationBugs:
    """Class with input validation issues"""
    
    def __init__(self):
        self.valid_emails = []
        self.user_data = {}
    
    def validate_email_address(self, email):
        """Level 1 - Validate email with bugs"""
        return self._check_email_format(email)
    
    def _check_email_format(self, email_str):
        """Level 2 - Check email format"""
        return self._regex_email_validation(email_str)
    
    def _regex_email_validation(self, email):
        """Level 3 - Regex email validation (buggy)"""
        # Buggy regex - too permissive
        pattern = r".*@.*"  # Accepts almost anything with @
        
        if not email:
            return False
        
        # No length validation
        if re.match(pattern, email):
            return True
        
        return False
    
    def validate_phone_number(self, phone):
        """Level 1 - Validate phone number"""
        return self._process_phone_input(phone)
    
    def _process_phone_input(self, phone_str):
        """Level 2 - Process phone input"""
        return self._check_phone_format(phone_str)
    
    def _check_phone_format(self, phone):
        """Level 3 - Check phone format (validation bugs)"""
        if not phone:
            return True  # Bug: empty phone should be invalid
        
        # Bug: only checks if it contains digits, not format
        if any(char.isdigit() for char in phone):
            return True
        
        return False
    
    def validate_age_input(self, age_str):
        """Level 1 - Validate age input"""
        return self._convert_age(age_str)
    
    def _convert_age(self, age_input):
        """Level 2 - Convert age"""
        return self._parse_age_value(age_input)
    
    def _parse_age_value(self, age):
        """Level 3 - Parse age value (validation bugs)"""
        try:
            age_int = int(age)
            # Bug: no range validation
            return age_int  # Accepts negative ages, ages > 200, etc.
        except ValueError:
            # Bug: returns 0 for invalid input instead of error
            return 0

class DataSanitizationIssues:
    """Class with data sanitization problems"""
    
    def sanitize_user_input(self, user_input):
        """Level 1 - Sanitize user input"""
        return self._clean_input_data(user_input)
    
    def _clean_input_data(self, input_str):
        """Level 2 - Clean input data"""
        return self._remove_dangerous_chars(input_str)
    
    def _remove_dangerous_chars(self, data):
        """Level 3 - Remove dangerous characters (insufficient)"""
        if not data:
            return data
        
        # Bug: insufficient sanitization
        cleaned = data.replace("<script>", "")  # Only removes exact match
        cleaned = cleaned.replace("'", "")  # Removes all single quotes
        
        # Bug: doesn't handle other dangerous patterns
        return cleaned
    
    def sanitize_sql_input(self, query_input):
        """Level 1 - Sanitize SQL input"""
        return self._prepare_sql_data(query_input)
    
    def _prepare_sql_data(self, sql_str):
        """Level 2 - Prepare SQL data"""
        return self._escape_sql_chars(sql_str)
    
    def _escape_sql_chars(self, sql_input):
        """Level 3 - Escape SQL characters (buggy)"""
        if not sql_input:
            return sql_input
        
        # Bug: incomplete SQL injection prevention
        escaped = sql_input.replace("'", "''")  # Only handles single quotes
        # Missing: double quotes, semicolons, comments, etc.
        
        return escaped
    
    def sanitize_file_path(self, file_path):
        """Level 1 - Sanitize file path"""
        return self._validate_path(file_path)
    
    def _validate_path(self, path_str):
        """Level 2 - Validate path"""
        return self._clean_path_traversal(path_str)
    
    def _clean_path_traversal(self, path):
        """Level 3 - Clean path traversal (insufficient)"""
        if not path:
            return path
        
        # Bug: insufficient path traversal prevention
        cleaned = path.replace("../", "")  # Only removes exact pattern
        # Missing: ..\\, ....//.../, encoded traversals, etc.
        
        return cleaned

class TypeValidationErrors:
    """Class with type validation errors"""
    
    def process_numeric_input(self, value):
        """Level 1 - Process numeric input"""
        return self._validate_number(value)
    
    def _validate_number(self, num_input):
        """Level 2 - Validate number"""
        return self._check_numeric_type(num_input)
    
    def _check_numeric_type(self, value):
        """Level 3 - Check numeric type (validation bugs)"""
        # Bug: doesn't validate type properly
        if value:  # Bug: doesn't check if it's actually numeric
            return float(value)  # Will crash on non-numeric strings
        
        return 0
    
    def validate_list_input(self, data):
        """Level 1 - Validate list input"""
        return self._check_list_structure(data)
    
    def _check_list_structure(self, list_data):
        """Level 2 - Check list structure"""
        return self._process_list_elements(list_data)
    
    def _process_list_elements(self, data):
        """Level 3 - Process list elements (type validation bugs)"""
        # Bug: assumes data is always a list
        result = []
        for item in data:  # Will crash if data is not iterable
            # Bug: no type checking for items
            result.append(item.upper())  # Will crash if item is not string
        
        return result
    
    def validate_dict_input(self, data):
        """Level 1 - Validate dict input"""
        return self._check_dict_keys(data)
    
    def _check_dict_keys(self, dict_data):
        """Level 2 - Check dict keys"""
        return self._process_dict_values(dict_data)
    
    def _process_dict_values(self, data):
        """Level 3 - Process dict values (type validation bugs)"""
        # Bug: assumes data is always a dict
        result = {}
        for key, value in data.items():  # Will crash if data is not dict
            # Bug: no validation of key/value types
            result[key.lower()] = str(value).upper()  # Crashes if key is not string
        
        return result

class BusinessLogicValidationBugs:
    """Class with business logic validation issues"""
    
    def validate_credit_card(self, card_number):
        """Level 1 - Validate credit card"""
        return self._check_card_format(card_number)
    
    def _check_card_format(self, card_num):
        """Level 2 - Check card format"""
        return self._luhn_algorithm_check(card_num)
    
    def _luhn_algorithm_check(self, number):
        """Level 3 - Luhn algorithm check (buggy implementation)"""
        if not number:
            return False
        
        # Bug: doesn't remove spaces/dashes
        digits = [int(d) for d in number if d.isdigit()]
        
        # Bug: incorrect Luhn algorithm implementation
        checksum = 0
        for i, digit in enumerate(digits):
            if i % 2 == 0:  # Bug: wrong condition
                doubled = digit * 2
                if doubled > 9:
                    doubled = doubled - 9
                checksum += doubled
            else:
                checksum += digit
        
        # Bug: wrong validation
        return checksum % 10 != 0  # Should be == 0
    
    def validate_password_policy(self, password):
        """Level 1 - Validate password policy"""
        return self._check_password_rules(password)
    
    def _check_password_rules(self, pwd):
        """Level 2 - Check password rules"""
        return self._enforce_password_policy(pwd)
    
    def _enforce_password_policy(self, password):
        """Level 3 - Enforce password policy (validation bugs)"""
        if not password:
            return False
        
        # Bug: wrong length check
        if len(password) < 8 or len(password) > 12:  # Too restrictive upper limit
            return False
        
        # Bug: insufficient complexity checks
        has_letter = any(c.isalpha() for c in password)
        has_number = any(c.isdigit() for c in password)
        
        # Bug: missing uppercase, lowercase, special char checks
        return has_letter and has_number
    
    def validate_date_range(self, start_date, end_date):
        """Level 1 - Validate date range"""
        return self._check_date_order(start_date, end_date)
    
    def _check_date_order(self, start, end):
        """Level 2 - Check date order"""
        return self._compare_dates(start, end)
    
    def _compare_dates(self, date1, date2):
        """Level 3 - Compare dates (validation bugs)"""
        # Bug: assumes dates are always datetime objects
        if date1 and date2:
            # Bug: allows start date to be equal to end date
            return date1 <= date2  # Should be < for proper range
        
        # Bug: returns True for None dates
        return True

class DataFormatValidationBugs:
    """Class with data format validation issues"""
    
    def validate_json_structure(self, json_str):
        """Level 1 - Validate JSON structure"""
        return self._parse_json_data(json_str)
    
    def _parse_json_data(self, json_string):
        """Level 2 - Parse JSON data"""
        return self._check_json_validity(json_string)
    
    def _check_json_validity(self, data):
        """Level 3 - Check JSON validity (validation bugs)"""
        try:
            parsed = json.loads(data)
            # Bug: doesn't validate structure, only syntax
            return True  # Should check for required fields
        except json.JSONDecodeError:
            # Bug: returns True for invalid JSON
            return True
    
    def validate_url_format(self, url):
        """Level 1 - Validate URL format"""
        return self._check_url_structure(url)
    
    def _check_url_structure(self, url_str):
        """Level 2 - Check URL structure"""
        return self._regex_url_validation(url_str)
    
    def _regex_url_validation(self, url):
        """Level 3 - Regex URL validation (buggy)"""
        # Bug: overly simple regex
        pattern = r"http.*"  # Accepts anything starting with "http"
        
        if not url:
            return True  # Bug: empty URL should be invalid
        
        return bool(re.match(pattern, url))

# Global validation functions with bugs
def validate_user_registration(username, email, password, age):
    """Global validation function with bugs"""
    return check_registration_data(username, email, password, age)

def check_registration_data(user, mail, pwd, user_age):
    """Level 2 - Check registration data"""
    return final_registration_validation(user, mail, pwd, user_age)

def final_registration_validation(username, email, password, age):
    """Level 3 - Final registration validation (multiple bugs)"""
    validator = InputValidationBugs()
    
    # Bug: doesn't check username at all
    email_valid = validator.validate_email_address(email)
    age_valid = validator.validate_age_input(str(age))
    
    # Bug: doesn't validate password
    # Bug: wrong logic - should be AND, not OR
    return email_valid or age_valid  # Should be AND
