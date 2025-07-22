"""
Main integration module with nested call graphs
This module integrates all buggy modules and demonstrates call graph relationships
Contains: Cross-module dependencies, complex call chains, integration issues
"""

# Import all buggy modules to create call graph relationships
from . import security_vulnerabilities
from . import code_quality_issues
from . import lint_errors
from . import runtime_errors
from . import memory_leaks
from . import concurrency_issues
from . import logic_errors
from . import error_handling_issues
from . import data_validation_bugs
from . import api_integration_bugs
from . import database_bugs
from . import file_handling_bugs
from . import authentication_bugs
from . import network_bugs
from . import crypto_bugs
from . import web_security_bugs
from . import performance_bugs
from . import integration_bugs
from . import testing_bugs

class SocietyExpenditureSystem:
    """Main system class that integrates all buggy modules"""
    
    def __init__(self):
        self.db_manager = database_bugs.DatabaseConnectionBugs()
        self.auth_system = authentication_bugs.WeakAuthenticationBugs()
        self.file_handler = file_handling_bugs.FileHandlingBugs()
        self.api_client = api_integration_bugs.APIIntegrationBugs()
        self.crypto_handler = crypto_bugs.WeakCryptographyBugs()
        self.web_security = web_security_bugs.XSSVulnerabilities()
        self.network_client = network_bugs.NetworkConnectionBugs()
        self.performance_monitor = performance_bugs.AlgorithmicComplexityBugs()
    
    def process_user_registration(self, username, password, email, profile_data):
        """Level 1 - Process user registration (integrates multiple buggy modules)"""
        return self._complete_user_registration(username, password, email, profile_data)
    
    def _complete_user_registration(self, username, password, email, profile_data):
        """Level 2 - Complete user registration (simplified call graph)"""
        # Input validation
        validator = data_validation_bugs.InputValidationBugs()
        email_valid = validator.validate_email_address(email)
        
        if not email_valid:
            return {'error': 'invalid_email'}
        
        # Password hashing
        password_hash = self.crypto_handler.encrypt_sensitive_data(password)
        
        # Database operations with SQL injection vulnerability
        query = f"INSERT INTO users (username, password, email) VALUES ('{username}', '{password_hash}', '{email}')"
        db_result = self.db_manager.execute_query(query)
        
        # File operations
        profile_file = f"profile_{username}.json"
        file_result = self.file_handler.write_user_data(profile_file, str(profile_data))
        
        # Authentication session
        session_id = self.auth_system.register_user(username, password, email)
        
        return {
            'user_id': len(db_result) if db_result else 0,
            'session_id': session_id,
            'profile_saved': file_result
        }
    
    def process_expense_submission(self, user_id, expense_data, receipt_file):
        """Level 1 - Process expense submission (integrates multiple modules)"""
        return self._validate_and_store_expense(user_id, expense_data, receipt_file)
    
    def _validate_and_store_expense(self, uid, expense, receipt):
        """Level 2 - Validate and store expense"""
        return self._complete_expense_processing(uid, expense, receipt)
    
    def _complete_expense_processing(self, user_id, expense_data, receipt_file):
        """Level 3 - Complete expense processing (complex call graph)"""
        # Call graph depth 1: Input validation with bugs
        validator = data_validation_bugs.BusinessLogicValidationBugs()
        
        # Call graph depth 2: Logic errors in validation
        logic_checker = logic_errors.LogicErrorGenerator()
        amount_valid = logic_checker.calculate_average_wrong([expense_data.get('amount', 0)])
        
        # Call graph depth 1: File handling for receipt
        receipt_path = self.file_handler.read_user_file(receipt_file)
        
        # Call graph depth 1: Database storage with SQL injection
        expense_query = f"INSERT INTO expenses (user_id, amount, description) VALUES ({user_id}, {expense_data['amount']}, '{expense_data['description']}')"
        
        # Call graph depth 2: Transaction management bugs
        transaction_manager = database_bugs.TransactionManagementBugs()
        db_result = transaction_manager.transfer_funds(user_id, 'expense_account', expense_data['amount'])
        
        # Call graph depth 1: API integration for expense categorization
        category_result = self.api_client.fetch_user_data(f"categories/{expense_data.get('category', 'misc')}")
        
        # Call graph depth 1: Performance issues in processing
        performance_result = self.performance_monitor.inefficient_search(expense_data['description'])
        
        return {
            'expense_id': hash(str(expense_data)),  # Weak ID generation
            'validation_result': amount_valid,
            'receipt_processed': bool(receipt_path),
            'category_data': category_result,
            'performance_impact': len(performance_result) if performance_result else 0
        }
    
    def generate_expense_report(self, user_id, date_range):
        """Level 1 - Generate expense report (integrates multiple modules)"""
        return self._compile_expense_data(user_id, date_range)
    
    def _compile_expense_data(self, uid, dates):
        """Level 2 - Compile expense data"""
        return self._create_comprehensive_report(uid, dates)
    
    def _create_comprehensive_report(self, user_id, date_range):
        """Level 3 - Create comprehensive report (complex call graph)"""
        # Call graph depth 1: Database queries with performance issues
        db_perf = database_bugs.DatabasePerformanceBugs()
        expense_data = db_perf.inefficient_data_retrieval('expenses')
        
        # Call graph depth 1: Memory leaks in data processing
        memory_handler = memory_leaks.MemoryLeakGenerator()
        processed_data = memory_handler.create_memory_leak(len(expense_data) if expense_data else 100)
        
        # Call graph depth 1: Concurrency issues in report generation
        concurrency_handler = concurrency_issues.RaceConditionGenerator()
        concurrent_result = concurrency_handler.start_race_condition(3)
        
        # Call graph depth 1: Runtime errors in calculations
        runtime_handler = runtime_errors.ErrorProneClass()
        
        # Call graph depth 2: Logic errors in report calculations
        try:
            total_amount = runtime_handler.process_list_data(0)  # Will cause IndexError
        except:
            total_amount = 0
        
        # Call graph depth 1: Web security issues in report display
        report_html = self.web_security.process_user_comment(f"Report for user {user_id}")
        
        # Call graph depth 1: Network issues in report delivery
        network_result = self.network_client.create_tcp_connection('report-server', 8080)
        
        # Call graph depth 1: Cryptography issues in report encryption
        encrypted_report = self.crypto_handler.encrypt_sensitive_data(str(expense_data))
        
        return {
            'report_data': expense_data,
            'total_expenses': total_amount,
            'report_html': report_html,
            'encrypted_data': encrypted_report,
            'network_status': bool(network_result),
            'memory_usage': processed_data,
            'concurrency_result': concurrent_result
        }

# Global integration functions with complex call graphs
def initialize_society_system():
    """Global function to initialize society system"""
    return setup_system_components()

def setup_system_components():
    """Level 2 - Setup system components"""
    return configure_all_modules()

def configure_all_modules():
    """Level 3 - Configure all modules (integrates all buggy modules)"""
    # Initialize all buggy components
    system = SocietyExpenditureSystem()
    
    # Call graph depth 1: Security vulnerabilities setup
    security_manager = security_vulnerabilities.DatabaseManager()
    security_manager.connect_database("user_input'; DROP TABLE users; --")
    
    # Call graph depth 1: Code quality issues
    quality_processor = code_quality_issues.DataProcessor()
    quality_result = quality_processor.processData([1, 2, 3])
    
    # Call graph depth 1: Lint errors
    lint_processor = lint_errors.LintErrorClass("test", 25, "test@example.com")
    lint_result = lint_processor.process_user_data("test_input")
    
    # Call graph depth 1: Integration bugs
    integration_handler = integration_bugs.ModuleIntegrationBugs()
    integration_handler.load_external_module("os")
    
    # Call graph depth 1: Testing bugs
    test_handler = testing_bugs.PoorTestCoverage()
    test_result = test_handler.run_incomplete_tests(['test_login', 'test_error_handling'])
    
    return {
        'system': system,
        'security_initialized': True,
        'quality_check': quality_result,
        'lint_check': lint_result,
        'integration_status': True,
        'test_results': test_result
    }

def process_society_transaction(transaction_data):
    """Global function to process society transaction"""
    return handle_transaction_processing(transaction_data)

def handle_transaction_processing(data):
    """Level 2 - Handle transaction processing"""
    return execute_complex_transaction(data)

def execute_complex_transaction(transaction_data):
    """Level 3 - Execute complex transaction (demonstrates deep call graph)"""
    system = SocietyExpenditureSystem()
    
    # Call graph depth 1-4: User registration with nested calls
    user_result = system.process_user_registration(
        transaction_data.get('username'),
        transaction_data.get('password'),
        transaction_data.get('email'),
        transaction_data.get('profile')
    )
    
    # Call graph depth 1-4: Expense processing with nested calls
    expense_result = system.process_expense_submission(
        user_result.get('user_id'),
        transaction_data.get('expense_data'),
        transaction_data.get('receipt_file')
    )
    
    # Call graph depth 1-4: Report generation with nested calls
    report_result = system.generate_expense_report(
        user_result.get('user_id'),
        transaction_data.get('date_range')
    )
    
    return {
        'user_registration': user_result,
        'expense_submission': expense_result,
        'report_generation': report_result,
        'transaction_id': hash(str(transaction_data))
    }
