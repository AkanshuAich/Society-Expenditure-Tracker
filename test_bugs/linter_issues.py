"""
Linter issues for testing
"""

import sys
import os
import json
import re
import datetime  # unused import

# Missing docstrings, inconsistent naming
class userAccount:  # should be UserAccount
    def __init__(self,name,age):  # missing spaces
        self.Name=name  # inconsistent naming
        self.AGE=age
        
    def getName(self):  # should be get_name
        return self.Name
        
    def setAge(self,new_age):  # missing spaces, should be set_age
        self.AGE=new_age
        
    def processAccount(self):
        # Nested calls (depth 1)
        info = self.getAccountInfo()
        return self.validateInfo(info)
    
    def getAccountInfo(self):
        return {'name': self.Name, 'age': self.AGE}
    
    def validateInfo(self, info):
        return info['age'] > 0

def calculate_total(items):
    total=0  # missing spaces
    for item in items:
        if item>0:  # missing spaces
            total+=item  # missing spaces
    return total

def process_user_input(user_input):
    # Long line that exceeds typical line length limits
    result = user_input.strip().lower().replace(' ', '_').replace('-', '_').replace('.', '_').replace(',', '_')
    
    # Nested processing (depth 2)
    cleaned = clean_input(result)
    return format_output(cleaned)

def clean_input(text):
    return sanitize_text(text.strip())

def sanitize_text(text):
    return re.sub(r'[^a-zA-Z0-9_]', '', text)

def format_output(text):
    return text.upper()

# Inconsistent indentation and spacing
class DataValidator:
  def __init__(self):
      self.rules=[]
      
  def add_rule(self,rule):
    self.rules.append(rule)
    
  def validate(self,data):
        # Mixed indentation
      for rule in self.rules:
          if not self.check_rule(rule, data):
            return False
      return True
  
  def check_rule(self, rule, data):
      # Nested validation (depth 1)
      return self.apply_rule(rule, data)
  
  def apply_rule(self, rule, data):
      return True  # simplified

# Unused variables and functions
def unused_function():
    unused_var = "this is never used"
    another_unused = 42
    return None

# Missing return statements
def incomplete_function(x):
    if x > 0:
        print("positive")
    elif x < 0:
        print("negative")
    # missing else case and return

# Bare except clause
def risky_operation():
    try:
        result = 10 / 0
    except:  # should specify exception type
        pass
    
    # Nested error handling (depth 1)
    return handle_error()

def handle_error():
    return "error handled"
