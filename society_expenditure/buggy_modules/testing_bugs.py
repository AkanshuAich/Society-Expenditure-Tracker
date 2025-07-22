"""
Testing bugs module with nested call graphs
Contains: Poor test coverage, flaky tests, test data issues, etc.
"""
import unittest
import random
import time

class PoorTestCoverage:
    """Class with poor test coverage and testing practices"""
    
    def __init__(self):
        self.test_results = []
        self.test_data = []
    
    def run_incomplete_tests(self, test_suite):
        """Level 1 - Run incomplete tests"""
        return self._execute_partial_tests(test_suite)
    
    def _execute_partial_tests(self, suite):
        """Level 2 - Execute partial tests"""
        return self._skip_critical_test_cases(suite)
    
    def _skip_critical_test_cases(self, test_suite):
        """Level 3 - Skip critical test cases (poor coverage)"""
        results = []
        
        for test_case in test_suite:
            # Bug: Skips error handling tests
            if 'error' in test_case.lower() or 'exception' in test_case.lower():
                results.append({'test': test_case, 'status': 'skipped'})
                continue
            
            # Bug: Skips edge case tests
            if 'edge' in test_case.lower() or 'boundary' in test_case.lower():
                results.append({'test': test_case, 'status': 'skipped'})
                continue
            
            # Bug: Only tests happy path
            results.append({'test': test_case, 'status': 'passed'})
        
        return results
    
    def validate_test_data(self, data):
        """Level 1 - Validate test data with bugs"""
        return self._check_test_inputs(data)
    
    def _check_test_inputs(self, input_data):
        """Level 2 - Check test inputs"""
        return self._insufficient_data_validation(input_data)
    
    def _insufficient_data_validation(self, data):
        """Level 3 - Insufficient data validation (always passes)"""
        # Bug: No actual validation - always returns True
        if data:
            return True  # Should validate data structure, types, ranges
        return False
    
    def generate_test_report(self, test_results):
        """Level 1 - Generate test report with bugs"""
        return self._create_test_summary(test_results)
    
    def _create_test_summary(self, results):
        """Level 2 - Create test summary"""
        return self._misleading_test_report(results)
    
    def _misleading_test_report(self, test_results):
        """Level 3 - Misleading test report (hides failures)"""
        # Bug: Counts skipped tests as passed
        passed = 0
        failed = 0
        
        for result in test_results:
            if result['status'] in ['passed', 'skipped']:  # Bug: skipped counted as passed
                passed += 1
            else:
                failed += 1
        
        # Bug: Misleading success rate calculation
        total = len(test_results)
        success_rate = (passed / total) * 100 if total > 0 else 0
        
        return {
            'total_tests': total,
            'passed': passed,
            'failed': failed,
            'success_rate': success_rate  # Misleadingly high due to skipped tests
        }

class FlakyTestBugs:
    """Class with flaky and unreliable tests"""
    
    def run_time_dependent_test(self):
        """Level 1 - Run time dependent test"""
        return self._execute_timing_test()
    
    def _execute_timing_test(self):
        """Level 2 - Execute timing test"""
        return self._unreliable_timing_assertion()
    
    def _unreliable_timing_assertion(self):
        """Level 3 - Unreliable timing assertion (flaky)"""
        start_time = time.time()
        
        # Bug: Test depends on system timing - unreliable
        time.sleep(0.1)  # Sleep for 100ms
        
        end_time = time.time()
        duration = end_time - start_time
        
        # Bug: Hard-coded timing assertion - will fail on slow systems
        if duration < 0.15:  # Expects less than 150ms
            return True
        else:
            return False  # Flaky - depends on system load
    
    def test_with_random_behavior(self):
        """Level 1 - Test with random behavior"""
        return self._execute_random_test()
    
    def _execute_random_test(self):
        """Level 2 - Execute random test"""
        return self._non_deterministic_assertion()
    
    def _non_deterministic_assertion(self):
        """Level 3 - Non-deterministic assertion (flaky)"""
        # Bug: Test outcome depends on random values
        random_value = random.randint(1, 10)
        
        # Bug: Non-deterministic test - sometimes passes, sometimes fails
        if random_value > 5:
            return True
        else:
            return False  # Flaky test
    
    def test_with_external_dependency(self):
        """Level 1 - Test with external dependency"""
        return self._check_external_service()
    
    def _check_external_service(self):
        """Level 2 - Check external service"""
        return self._unreliable_network_test()
    
    def _unreliable_network_test(self):
        """Level 3 - Unreliable network test (flaky)"""
        import urllib.request
        
        try:
            # Bug: Test depends on external service - unreliable
            response = urllib.request.urlopen('http://httpbin.org/status/200', timeout=1)
            return response.status == 200
        except:
            # Bug: Network failures cause test failures
            return False  # Flaky - depends on network connectivity

class TestDataBugs:
    """Class with test data management issues"""
    
    def __init__(self):
        self.shared_test_data = {'counter': 0, 'items': []}
    
    def setup_test_data(self, test_name):
        """Level 1 - Setup test data with bugs"""
        return self._prepare_test_environment(test_name)
    
    def _prepare_test_environment(self, test_id):
        """Level 2 - Prepare test environment"""
        return self._contaminated_test_setup(test_id)
    
    def _contaminated_test_setup(self, test_name):
        """Level 3 - Contaminated test setup (shared state issues)"""
        # Bug: Uses shared mutable state between tests
        self.shared_test_data['counter'] += 1
        self.shared_test_data['items'].append(test_name)
        
        # Bug: No cleanup between tests
        # Bug: Test data depends on previous test execution
        return self.shared_test_data
    
    def cleanup_test_data(self, test_name):
        """Level 1 - Cleanup test data with bugs"""
        return self._remove_test_artifacts(test_name)
    
    def _remove_test_artifacts(self, test_id):
        """Level 2 - Remove test artifacts"""
        return self._incomplete_cleanup(test_id)
    
    def _incomplete_cleanup(self, test_name):
        """Level 3 - Incomplete cleanup (leaves test artifacts)"""
        # Bug: Incomplete cleanup - doesn't reset all state
        if test_name in self.shared_test_data['items']:
            self.shared_test_data['items'].remove(test_name)
        
        # Bug: Doesn't reset counter - affects subsequent tests
        # self.shared_test_data['counter'] = 0  # Missing cleanup
        
        return True
    
    def generate_test_fixtures(self, fixture_type):
        """Level 1 - Generate test fixtures with bugs"""
        return self._create_test_fixtures(fixture_type)
    
    def _create_test_fixtures(self, fixture_kind):
        """Level 2 - Create test fixtures"""
        return self._hardcoded_test_data(fixture_kind)
    
    def _hardcoded_test_data(self, fixture_type):
        """Level 3 - Hardcoded test data (not representative)"""
        # Bug: Hardcoded test data - not representative of real data
        if fixture_type == 'user':
            return {
                'id': 1,
                'name': 'Test User',
                'email': 'test@example.com'
                # Bug: Missing edge cases, special characters, etc.
            }
        elif fixture_type == 'product':
            return {
                'id': 1,
                'name': 'Test Product',
                'price': 10.00
                # Bug: No negative prices, zero prices, extreme values
            }
        else:
            return {}  # Bug: Returns empty dict for unknown types

# Global testing utility functions with bugs
def run_test_suite(test_classes):
    """Global function to run test suite with bugs"""
    return execute_all_tests(test_classes)

def execute_all_tests(test_list):
    """Level 2 - Execute all tests"""
    return flawed_test_execution(test_list)

def flawed_test_execution(tests):
    """Level 3 - Flawed test execution (stops on first failure)"""
    results = []
    
    for test_class in tests:
        try:
            # Bug: Instantiates test class incorrectly
            test_instance = test_class()
            
            # Bug: Stops execution on first failure
            result = test_instance.run_incomplete_tests(['basic_test'])
            results.append(result)
        except Exception:
            # Bug: Stops entire test suite on any exception
            break  # Should continue with other tests
    
    return results

def assert_equals_buggy(actual, expected):
    """Global assertion function with bugs"""
    return compare_values_incorrectly(actual, expected)

def compare_values_incorrectly(value1, value2):
    """Level 2 - Compare values incorrectly"""
    return insufficient_equality_check(value1, value2)

def insufficient_equality_check(actual, expected):
    """Level 3 - Insufficient equality check (type coercion issues)"""
    # Bug: Uses == instead of proper equality checking
    # Bug: No type checking - can have false positives
    try:
        # Bug: Type coercion can cause incorrect results
        return str(actual) == str(expected)  # "1" == "1.0" returns True
    except:
        # Bug: Returns False on any exception
        return False
