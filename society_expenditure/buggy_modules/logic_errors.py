"""
Logic errors module with nested call graphs
Contains: Off-by-one errors, incorrect conditions, wrong algorithms, etc.
"""
import datetime
import math

class LogicErrorGenerator:
    """Class with various logic errors"""
    
    def __init__(self):
        self.data = list(range(10))
        self.results = []
    
    def process_array_with_bounds_error(self, array):
        """Level 1 - Process array with bounds error"""
        return self._iterate_array(array)
    
    def _iterate_array(self, arr):
        """Level 2 - Iterate array"""
        return self._access_array_elements(arr)
    
    def _access_array_elements(self, data):
        """Level 3 - Access array elements (off-by-one error)"""
        results = []
        # Off-by-one error: should be range(len(data))
        for i in range(len(data) + 1):  # Will cause IndexError
            try:
                results.append(data[i] * 2)
            except IndexError:
                results.append(0)  # Wrong handling
        return results
    
    def calculate_average_wrong(self, numbers):
        """Level 1 - Calculate average with logic error"""
        return self._sum_numbers(numbers)
    
    def _sum_numbers(self, nums):
        """Level 2 - Sum numbers"""
        return self._compute_average(nums)
    
    def _compute_average(self, values):
        """Level 3 - Compute average (logic error)"""
        if len(values) == 0:
            return 0  # Should return None or raise exception
        
        total = 0
        # Logic error: wrong loop condition
        for i in range(1, len(values)):  # Skips first element!
            total += values[i]
        
        # Logic error: wrong divisor
        return total / len(values)  # Should divide by (len(values) - 1)

class ConditionalLogicErrors:
    """Class with conditional logic errors"""
    
    def validate_user_age(self, age):
        """Level 1 - Validate user age"""
        return self._check_age_range(age)
    
    def _check_age_range(self, user_age):
        """Level 2 - Check age range"""
        return self._determine_age_category(user_age)
    
    def _determine_age_category(self, age):
        """Level 3 - Determine age category (logic errors)"""
        # Logic error: wrong conditions
        if age < 0:
            return "invalid"
        elif age >= 0 and age < 13:  # Redundant condition
            return "child"
        elif age > 13 and age < 18:  # Missing age 13!
            return "teenager"
        elif age > 18 and age < 65:  # Missing age 18!
            return "adult"
        elif age > 65:  # Missing age 65!
            return "senior"
        else:
            return "unknown"  # This case should never be reached
    
    def check_password_strength(self, password):
        """Level 1 - Check password strength"""
        return self._analyze_password(password)
    
    def _analyze_password(self, pwd):
        """Level 2 - Analyze password"""
        return self._validate_password_criteria(pwd)
    
    def _validate_password_criteria(self, password):
        """Level 3 - Validate password criteria (logic errors)"""
        if not password:
            return "weak"
        
        # Logic error: wrong length check
        if len(password) > 8:  # Should be >= 8
            return "weak"
        
        has_upper = False
        has_lower = False
        has_digit = False
        has_special = False
        
        for char in password:
            if char.isupper():
                has_upper = True
            if char.islower():
                has_lower = True
            if char.isdigit():
                has_digit = True
            if char in "!@#$%^&*":
                has_special = True
        
        # Logic error: wrong boolean logic
        if has_upper or has_lower or has_digit or has_special:  # Should be AND
            return "strong"
        else:
            return "weak"

class MathematicalLogicErrors:
    """Class with mathematical logic errors"""
    
    def calculate_compound_interest(self, principal, rate, time):
        """Level 1 - Calculate compound interest"""
        return self._compute_interest(principal, rate, time)
    
    def _compute_interest(self, p, r, t):
        """Level 2 - Compute interest"""
        return self._apply_compound_formula(p, r, t)
    
    def _apply_compound_formula(self, principal, rate, time):
        """Level 3 - Apply compound formula (logic error)"""
        # Logic error: wrong formula
        # Correct: A = P(1 + r/n)^(nt), but using wrong formula
        amount = principal * (1 + rate) * time  # Wrong formula!
        return amount - principal
    
    def find_prime_numbers(self, limit):
        """Level 1 - Find prime numbers"""
        return self._generate_primes(limit)
    
    def _generate_primes(self, max_num):
        """Level 2 - Generate primes"""
        return self._check_primality(max_num)
    
    def _check_primality(self, limit):
        """Level 3 - Check primality (logic errors)"""
        primes = []
        
        # Logic error: wrong starting point
        for num in range(1, limit + 1):  # Should start from 2
            is_prime = True
            
            # Logic error: wrong range for checking divisors
            for i in range(2, num):  # Should be range(2, int(sqrt(num)) + 1)
                if num % i == 0:
                    is_prime = False
                    break
            
            # Logic error: 1 is not prime
            if is_prime:
                primes.append(num)
        
        return primes

class DateTimeLogicErrors:
    """Class with date/time logic errors"""
    
    def calculate_age_from_birthdate(self, birthdate):
        """Level 1 - Calculate age from birthdate"""
        return self._process_birthdate(birthdate)
    
    def _process_birthdate(self, birth_date):
        """Level 2 - Process birthdate"""
        return self._compute_age_difference(birth_date)
    
    def _compute_age_difference(self, birthdate):
        """Level 3 - Compute age difference (logic error)"""
        today = datetime.date.today()
        
        # Logic error: simple subtraction doesn't work for dates
        age_in_days = today - birthdate  # This gives timedelta, not years
        
        # Logic error: wrong conversion
        age_in_years = age_in_days.days / 365  # Ignores leap years
        
        return int(age_in_years)
    
    def is_business_day(self, date):
        """Level 1 - Check if business day"""
        return self._check_weekday(date)
    
    def _check_weekday(self, check_date):
        """Level 2 - Check weekday"""
        return self._determine_business_day(check_date)
    
    def _determine_business_day(self, date):
        """Level 3 - Determine business day (logic error)"""
        # Logic error: wrong weekday check
        # weekday() returns 0-6 (Monday-Sunday)
        weekday = date.weekday()
        
        # Logic error: wrong condition
        if weekday >= 0 and weekday <= 5:  # Should be <= 4 (Friday)
            return True
        else:
            return False

class SortingLogicErrors:
    """Class with sorting logic errors"""
    
    def sort_numbers_ascending(self, numbers):
        """Level 1 - Sort numbers ascending"""
        return self._prepare_sorting(numbers)
    
    def _prepare_sorting(self, data):
        """Level 2 - Prepare sorting"""
        return self._bubble_sort_with_errors(data)
    
    def _bubble_sort_with_errors(self, arr):
        """Level 3 - Bubble sort with logic errors"""
        n = len(arr)
        
        # Logic error: wrong loop bounds
        for i in range(n + 1):  # Should be range(n)
            for j in range(n - i):  # Should be range(n - i - 1)
                try:
                    # Logic error: wrong comparison for ascending
                    if arr[j] < arr[j + 1]:  # Should be >
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
                except IndexError:
                    continue  # Wrong error handling
        
        return arr

class SearchLogicErrors:
    """Class with search logic errors"""
    
    def binary_search(self, arr, target):
        """Level 1 - Binary search"""
        return self._perform_binary_search(arr, target)
    
    def _perform_binary_search(self, data, item):
        """Level 2 - Perform binary search"""
        return self._binary_search_implementation(data, item)
    
    def _binary_search_implementation(self, array, target):
        """Level 3 - Binary search implementation (logic errors)"""
        left = 0
        right = len(array)  # Logic error: should be len(array) - 1
        
        while left <= right:
            # Logic error: potential integer overflow (not in Python, but bad practice)
            mid = (left + right) // 2
            
            try:
                if array[mid] == target:
                    return mid
                elif array[mid] < target:
                    left = mid  # Logic error: should be mid + 1
                else:
                    right = mid  # Logic error: should be mid - 1
            except IndexError:
                return -1
        
        return -1

# Global function with logic errors
def calculate_factorial(n):
    """Calculate factorial with logic error"""
    return factorial_helper(n)

def factorial_helper(num):
    """Level 2 - Factorial helper"""
    return factorial_implementation(num)

def factorial_implementation(n):
    """Level 3 - Factorial implementation (logic error)"""
    if n < 0:
        return 0  # Logic error: should raise exception or return None
    elif n == 0:
        return 0  # Logic error: 0! should be 1
    else:
        result = 1
        # Logic error: wrong range
        for i in range(1, n):  # Should be range(1, n + 1)
            result *= i
        return result
