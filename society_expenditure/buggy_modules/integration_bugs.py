"""
Integration bugs module with nested call graphs
Contains: Module integration issues, dependency problems, configuration bugs, etc.
"""
import sys
import os
import importlib

class ModuleIntegrationBugs:
    """Class with module integration issues"""
    
    def __init__(self):
        self.loaded_modules = {}
        self.dependencies = []
    
    def load_external_module(self, module_name):
        """Level 1 - Load external module with bugs"""
        return self._import_module_unsafe(module_name)
    
    def _import_module_unsafe(self, mod_name):
        """Level 2 - Import module unsafe"""
        return self._dynamic_import_with_issues(mod_name)
    
    def _dynamic_import_with_issues(self, module_name):
        """Level 3 - Dynamic import with security and error issues"""
        try:
            # Bug: No validation of module name - code injection possible
            # Bug: Uses eval for dynamic import
            module = eval(f"__import__('{module_name}')")  # Dangerous!
            
            self.loaded_modules[module_name] = module
            return module
        except Exception:
            # Bug: Swallows all import errors
            return None
    
    def call_external_function(self, module_name, function_name, *args):
        """Level 1 - Call external function with bugs"""
        return self._invoke_external_method(module_name, function_name, *args)
    
    def _invoke_external_method(self, mod, func, *arguments):
        """Level 2 - Invoke external method"""
        return self._unsafe_function_call(mod, func, *arguments)
    
    def _unsafe_function_call(self, module_name, function_name, *args):
        """Level 3 - Unsafe function call (multiple issues)"""
        if module_name not in self.loaded_modules:
            return None
        
        module = self.loaded_modules[module_name]
        
        try:
            # Bug: No validation of function name - attribute injection
            # Bug: Uses getattr without validation
            func = getattr(module, function_name)  # Can access private methods
            
            # Bug: No argument validation
            return func(*args)  # Can pass malicious arguments
        except AttributeError:
            # Bug: Returns None instead of proper error
            return None
        except Exception:
            # Bug: Swallows all exceptions
            return None

class ConfigurationBugs:
    """Class with configuration management issues"""
    
    def __init__(self):
        self.config = {}
        self.config_file = "config.json"
    
    def load_configuration(self, config_path=None):
        """Level 1 - Load configuration with bugs"""
        return self._read_config_file(config_path)
    
    def _read_config_file(self, file_path):
        """Level 2 - Read config file"""
        return self._parse_config_unsafe(file_path)
    
    def _parse_config_unsafe(self, config_path):
        """Level 3 - Parse config unsafe (multiple security issues)"""
        import json
        
        if not config_path:
            config_path = self.config_file
        
        try:
            # Bug: No path validation - path traversal possible
            with open(config_path, 'r') as f:
                config_data = f.read()
            
            # Bug: Uses eval instead of json.loads - code execution!
            self.config = eval(config_data)  # Extremely dangerous!
            
            return self.config
        except Exception:
            # Bug: Returns empty dict on any error
            return {}
    
    def get_config_value(self, key, default=None):
        """Level 1 - Get config value with bugs"""
        return self._retrieve_config_setting(key, default)
    
    def _retrieve_config_setting(self, setting_key, default_value):
        """Level 2 - Retrieve config setting"""
        return self._unsafe_config_access(setting_key, default_value)
    
    def _unsafe_config_access(self, key, default):
        """Level 3 - Unsafe config access (injection vulnerability)"""
        try:
            # Bug: Uses eval for key access - code injection
            value = eval(f"self.config['{key}']")  # Dangerous!
            return value
        except:
            # Bug: Returns default without proper error handling
            return default
    
    def update_config_value(self, key, value):
        """Level 1 - Update config value with bugs"""
        return self._modify_config_setting(key, value)
    
    def _modify_config_setting(self, setting_key, new_value):
        """Level 2 - Modify config setting"""
        return self._unsafe_config_update(setting_key, new_value)
    
    def _unsafe_config_update(self, key, value):
        """Level 3 - Unsafe config update (injection vulnerability)"""
        try:
            # Bug: Uses exec for dynamic assignment - code execution!
            exec(f"self.config['{key}'] = {repr(value)}")  # Dangerous!
            return True
        except:
            return False

class DependencyManagementBugs:
    """Class with dependency management issues"""
    
    def __init__(self):
        self.dependencies = []
        self.version_conflicts = []
    
    def install_dependency(self, package_name, version=None):
        """Level 1 - Install dependency with bugs"""
        return self._add_package_dependency(package_name, version)
    
    def _add_package_dependency(self, pkg_name, pkg_version):
        """Level 2 - Add package dependency"""
        return self._unsafe_dependency_installation(pkg_name, pkg_version)
    
    def _unsafe_dependency_installation(self, package, version):
        """Level 3 - Unsafe dependency installation (security issues)"""
        import subprocess
        
        # Bug: No package name validation - command injection
        if version:
            # Bug: Direct string interpolation in shell command
            command = f"pip install {package}=={version}"  # Command injection!
        else:
            command = f"pip install {package}"  # Command injection!
        
        try:
            # Bug: Uses shell=True with user input - dangerous!
            result = subprocess.run(command, shell=True, capture_output=True)
            
            if result.returncode == 0:
                self.dependencies.append({'name': package, 'version': version})
                return True
            else:
                return False
        except Exception:
            return False
    
    def check_version_compatibility(self, package1, package2):
        """Level 1 - Check version compatibility with bugs"""
        return self._validate_package_versions(package1, package2)
    
    def _validate_package_versions(self, pkg1, pkg2):
        """Level 2 - Validate package versions"""
        return self._insufficient_version_checking(pkg1, pkg2)
    
    def _insufficient_version_checking(self, package1, package2):
        """Level 3 - Insufficient version checking (always returns True)"""
        # Bug: No actual version compatibility checking
        # Bug: Always returns True regardless of conflicts
        return True  # Should check for actual version conflicts

class EnvironmentBugs:
    """Class with environment configuration issues"""
    
    def setup_environment(self, env_vars):
        """Level 1 - Setup environment with bugs"""
        return self._configure_environment(env_vars)
    
    def _configure_environment(self, variables):
        """Level 2 - Configure environment"""
        return self._unsafe_env_setup(variables)
    
    def _unsafe_env_setup(self, env_variables):
        """Level 3 - Unsafe environment setup (security issues)"""
        for key, value in env_variables.items():
            # Bug: No validation of environment variable names/values
            # Bug: Can overwrite critical system environment variables
            os.environ[key] = str(value)  # Can break system
        
        return True
    
    def get_environment_variable(self, var_name):
        """Level 1 - Get environment variable with bugs"""
        return self._retrieve_env_var(var_name)
    
    def _retrieve_env_var(self, variable_name):
        """Level 2 - Retrieve env var"""
        return self._unsafe_env_access(variable_name)
    
    def _unsafe_env_access(self, var_name):
        """Level 3 - Unsafe environment access (injection vulnerability)"""
        try:
            # Bug: Uses eval for environment variable access
            value = eval(f"os.environ.get('{var_name}')")  # Code injection!
            return value
        except:
            return None

# Global integration utility functions with bugs
def initialize_application_modules():
    """Global function to initialize application modules with bugs"""
    return setup_module_system()

def setup_module_system():
    """Level 2 - Setup module system"""
    return load_all_modules_unsafe()

def load_all_modules_unsafe():
    """Level 3 - Load all modules unsafe (security issues)"""
    import glob
    
    # Bug: Loads all Python files without validation
    module_files = glob.glob("*.py")
    
    loaded_modules = []
    for module_file in module_files:
        try:
            module_name = module_file[:-3]  # Remove .py extension
            
            # Bug: Uses exec to load modules - code execution risk
            with open(module_file, 'r') as f:
                module_code = f.read()
            
            # Bug: Executes arbitrary Python code
            exec(module_code)  # Extremely dangerous!
            
            loaded_modules.append(module_name)
        except Exception:
            continue
    
    return loaded_modules

def configure_application_settings(settings_dict):
    """Global function to configure application settings with bugs"""
    return apply_configuration_settings(settings_dict)

def apply_configuration_settings(settings):
    """Level 2 - Apply configuration settings"""
    return unsafe_settings_application(settings)

def unsafe_settings_application(config_settings):
    """Level 3 - Unsafe settings application (code execution)"""
    for setting_name, setting_value in config_settings.items():
        try:
            # Bug: Uses exec for dynamic configuration - code execution!
            exec(f"{setting_name} = {repr(setting_value)}")  # Dangerous!
        except:
            continue
    
    return True
