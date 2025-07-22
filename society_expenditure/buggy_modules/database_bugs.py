"""
Database bugs module with nested call graphs
Contains: SQL injection, connection leaks, transaction issues, etc.
"""
import sqlite3
import mysql.connector
import psycopg2
import time

class DatabaseConnectionBugs:
    """Class with database connection issues"""
    
    def __init__(self):
        self.connection = None
        self.cursor = None
    
    def connect_to_database(self, db_name):
        """Level 1 - Connect to database with bugs"""
        return self._establish_connection(db_name)
    
    def _establish_connection(self, database):
        """Level 2 - Establish connection"""
        return self._create_db_connection(database)
    
    def _create_db_connection(self, db_name):
        """Level 3 - Create database connection (connection leak)"""
        try:
            # Bug: Connection never closed properly
            self.connection = sqlite3.connect(db_name)
            self.cursor = self.connection.cursor()
            return True
        except sqlite3.Error:
            # Bug: Doesn't handle connection errors properly
            return False
    
    def execute_query(self, query, params=None):
        """Level 1 - Execute query with bugs"""
        return self._run_sql_query(query, params)
    
    def _run_sql_query(self, sql, parameters):
        """Level 2 - Run SQL query"""
        return self._unsafe_query_execution(sql, parameters)
    
    def _unsafe_query_execution(self, query, params):
        """Level 3 - Unsafe query execution (SQL injection)"""
        try:
            if params:
                # Bug: String formatting instead of parameterized queries
                formatted_query = query.format(*params)  # SQL injection risk
                self.cursor.execute(formatted_query)
            else:
                self.cursor.execute(query)
            
            return self.cursor.fetchall()
        except sqlite3.Error:
            # Bug: Swallows database errors
            return []
    
    def batch_insert_data(self, table, data_list):
        """Level 1 - Batch insert with bugs"""
        return self._prepare_batch_insert(table, data_list)
    
    def _prepare_batch_insert(self, table_name, records):
        """Level 2 - Prepare batch insert"""
        return self._execute_batch_insert(table_name, records)
    
    def _execute_batch_insert(self, table, data):
        """Level 3 - Execute batch insert (transaction bugs)"""
        # Bug: No transaction management
        for record in data:
            try:
                # Bug: SQL injection vulnerability
                query = f"INSERT INTO {table} VALUES ({','.join(map(str, record))})"
                self.cursor.execute(query)
                # Bug: No commit after each insert (inefficient)
                self.connection.commit()
            except sqlite3.Error:
                # Bug: Continues on error without rollback
                continue
        
        return len(data)

class SQLInjectionVulnerabilities:
    """Class with SQL injection vulnerabilities"""
    
    def __init__(self):
        self.db_connection = sqlite3.connect(':memory:')
        self.cursor = self.db_connection.cursor()
    
    def search_users(self, username):
        """Level 1 - Search users with SQL injection"""
        return self._find_user_records(username)
    
    def _find_user_records(self, user_name):
        """Level 2 - Find user records"""
        return self._query_user_table(user_name)
    
    def _query_user_table(self, username):
        """Level 3 - Query user table (SQL injection vulnerable)"""
        # Bug: Direct string concatenation - SQL injection
        query = f"SELECT * FROM users WHERE username = '{username}'"
        
        try:
            self.cursor.execute(query)  # Vulnerable to SQL injection
            return self.cursor.fetchall()
        except sqlite3.Error:
            return []
    
    def update_user_profile(self, user_id, field, value):
        """Level 1 - Update user profile with injection risk"""
        return self._modify_user_data(user_id, field, value)
    
    def _modify_user_data(self, uid, column, new_value):
        """Level 2 - Modify user data"""
        return self._execute_update_query(uid, column, new_value)
    
    def _execute_update_query(self, user_id, field_name, value):
        """Level 3 - Execute update query (SQL injection)"""
        # Bug: Dynamic query construction - SQL injection
        query = f"UPDATE users SET {field_name} = '{value}' WHERE id = {user_id}"
        
        try:
            self.cursor.execute(query)  # Vulnerable to SQL injection
            self.db_connection.commit()
            return True
        except sqlite3.Error:
            return False
    
    def delete_user_records(self, condition):
        """Level 1 - Delete user records with injection risk"""
        return self._remove_user_data(condition)
    
    def _remove_user_data(self, where_clause):
        """Level 2 - Remove user data"""
        return self._execute_delete_query(where_clause)
    
    def _execute_delete_query(self, condition):
        """Level 3 - Execute delete query (SQL injection)"""
        # Bug: Direct condition injection - very dangerous
        query = f"DELETE FROM users WHERE {condition}"
        
        try:
            self.cursor.execute(query)  # Extremely vulnerable
            self.db_connection.commit()
            return self.cursor.rowcount
        except sqlite3.Error:
            return 0

class TransactionManagementBugs:
    """Class with transaction management issues"""
    
    def __init__(self):
        self.connection = sqlite3.connect(':memory:')
        self.cursor = self.connection.cursor()
    
    def transfer_funds(self, from_account, to_account, amount):
        """Level 1 - Transfer funds with transaction bugs"""
        return self._process_money_transfer(from_account, to_account, amount)
    
    def _process_money_transfer(self, from_acc, to_acc, transfer_amount):
        """Level 2 - Process money transfer"""
        return self._execute_fund_transfer(from_acc, to_acc, transfer_amount)
    
    def _execute_fund_transfer(self, from_account, to_account, amount):
        """Level 3 - Execute fund transfer (transaction bugs)"""
        try:
            # Bug: No transaction begin
            # Debit from source account
            debit_query = f"UPDATE accounts SET balance = balance - {amount} WHERE id = {from_account}"
            self.cursor.execute(debit_query)
            
            # Bug: No error checking between operations
            # Credit to destination account
            credit_query = f"UPDATE accounts SET balance = balance + {amount} WHERE id = {to_account}"
            self.cursor.execute(credit_query)
            
            # Bug: Commits without checking if both operations succeeded
            self.connection.commit()
            return True
        except sqlite3.Error:
            # Bug: No rollback on error
            return False
    
    def batch_update_inventory(self, updates):
        """Level 1 - Batch update inventory with transaction issues"""
        return self._process_inventory_updates(updates)
    
    def _process_inventory_updates(self, update_list):
        """Level 2 - Process inventory updates"""
        return self._execute_inventory_batch(update_list)
    
    def _execute_inventory_batch(self, updates):
        """Level 3 - Execute inventory batch (transaction bugs)"""
        success_count = 0
        
        # Bug: No transaction wrapping for batch operation
        for update in updates:
            try:
                query = f"UPDATE inventory SET quantity = {update['quantity']} WHERE product_id = {update['id']}"
                self.cursor.execute(query)
                self.connection.commit()  # Bug: Commits after each update
                success_count += 1
            except sqlite3.Error:
                # Bug: Continues processing even after errors
                continue
        
        return success_count

class DatabasePerformanceBugs:
    """Class with database performance issues"""
    
    def __init__(self):
        self.connection = sqlite3.connect(':memory:')
        self.cursor = self.connection.cursor()
    
    def inefficient_data_retrieval(self, table_name):
        """Level 1 - Inefficient data retrieval"""
        return self._fetch_all_data(table_name)
    
    def _fetch_all_data(self, table):
        """Level 2 - Fetch all data"""
        return self._select_without_limits(table)
    
    def _select_without_limits(self, table_name):
        """Level 3 - Select without limits (performance bug)"""
        # Bug: No LIMIT clause - can return millions of rows
        query = f"SELECT * FROM {table_name}"
        
        try:
            self.cursor.execute(query)
            # Bug: fetchall() loads everything into memory
            return self.cursor.fetchall()
        except sqlite3.Error:
            return []
    
    def search_without_indexes(self, table, search_term):
        """Level 1 - Search without indexes"""
        return self._perform_full_table_scan(table, search_term)
    
    def _perform_full_table_scan(self, table_name, term):
        """Level 2 - Perform full table scan"""
        return self._execute_inefficient_search(table_name, term)
    
    def _execute_inefficient_search(self, table, search_value):
        """Level 3 - Execute inefficient search (performance bug)"""
        # Bug: LIKE with leading wildcard prevents index usage
        query = f"SELECT * FROM {table} WHERE name LIKE '%{search_value}%'"
        
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except sqlite3.Error:
            return []
    
    def n_plus_one_query_problem(self, user_ids):
        """Level 1 - N+1 query problem"""
        return self._fetch_user_details(user_ids)
    
    def _fetch_user_details(self, ids):
        """Level 2 - Fetch user details"""
        return self._individual_user_queries(ids)
    
    def _individual_user_queries(self, user_ids):
        """Level 3 - Individual user queries (N+1 problem)"""
        results = []
        
        # Bug: N+1 query problem - should use JOIN or IN clause
        for user_id in user_ids:
            query = f"SELECT * FROM users WHERE id = {user_id}"
            try:
                self.cursor.execute(query)
                user_data = self.cursor.fetchone()
                
                # Another query for each user (making it worse)
                profile_query = f"SELECT * FROM profiles WHERE user_id = {user_id}"
                self.cursor.execute(profile_query)
                profile_data = self.cursor.fetchone()
                
                results.append({'user': user_data, 'profile': profile_data})
            except sqlite3.Error:
                continue
        
        return results

# Global database utility functions with bugs
def execute_raw_query(connection, query, params=None):
    """Global function to execute raw queries with bugs"""
    return run_database_query(connection, query, params)

def run_database_query(db_conn, sql, parameters):
    """Level 2 - Run database query"""
    return unsafe_query_execution(db_conn, sql, parameters)

def unsafe_query_execution(connection, query, params):
    """Level 3 - Unsafe query execution (multiple bugs)"""
    cursor = connection.cursor()
    
    try:
        if params:
            # Bug: String formatting instead of parameterized queries
            formatted_query = query % params  # SQL injection risk
            cursor.execute(formatted_query)
        else:
            cursor.execute(query)
        
        # Bug: No proper result handling
        return cursor.fetchall()
    except Exception:
        # Bug: Swallows all database errors
        return []
    finally:
        # Bug: Cursor not closed properly
        pass
