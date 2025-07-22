"""
API integration bugs module with nested call graphs
Contains: HTTP request issues, JSON parsing errors, timeout problems, etc.
"""
import requests
import json
import time
import urllib.parse

class APIIntegrationBugs:
    """Class with API integration issues"""
    
    def __init__(self):
        self.base_url = "http://api.example.com"
        self.api_key = "hardcoded_api_key_123"  # Security issue
        self.timeout = 30
    
    def fetch_user_data(self, user_id):
        """Level 1 - Fetch user data with API bugs"""
        return self._make_user_request(user_id)
    
    def _make_user_request(self, uid):
        """Level 2 - Make user request"""
        return self._execute_api_call(uid)
    
    def _execute_api_call(self, user_id):
        """Level 3 - Execute API call (multiple bugs)"""
        # Bug: No input validation
        url = f"{self.base_url}/users/{user_id}"  # Vulnerable to injection
        
        # Bug: No timeout handling
        try:
            response = requests.get(url)  # No timeout specified
            # Bug: No status code checking
            data = response.json()  # Will fail if not JSON
            return data
        except requests.RequestException:
            # Bug: Returns None instead of proper error handling
            return None
    
    def post_user_data(self, user_data):
        """Level 1 - Post user data with bugs"""
        return self._prepare_post_request(user_data)
    
    def _prepare_post_request(self, data):
        """Level 2 - Prepare POST request"""
        return self._send_post_data(data)
    
    def _send_post_data(self, payload):
        """Level 3 - Send POST data (bugs)"""
        url = f"{self.base_url}/users"
        
        # Bug: No data validation before sending
        # Bug: Hardcoded headers
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}'  # Hardcoded key
        }
        
        try:
            # Bug: No proper JSON serialization check
            response = requests.post(url, data=json.dumps(payload), headers=headers)
            # Bug: No response validation
            return response.json()
        except (requests.RequestException, json.JSONDecodeError):
            # Bug: Swallows all exceptions
            return {}

class HTTPErrorHandlingBugs:
    """Class with HTTP error handling issues"""
    
    def handle_api_responses(self, endpoint):
        """Level 1 - Handle API responses with bugs"""
        return self._process_response(endpoint)
    
    def _process_response(self, url):
        """Level 2 - Process response"""
        return self._check_response_status(url)
    
    def _check_response_status(self, endpoint):
        """Level 3 - Check response status (poor error handling)"""
        try:
            response = requests.get(endpoint)
            
            # Bug: Doesn't check status codes properly
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 404:
                return {}  # Bug: Should indicate error
            elif response.status_code == 500:
                return {}  # Bug: Should indicate server error
            else:
                return {}  # Bug: Ignores all other status codes
                
        except requests.ConnectionError:
            # Bug: Returns empty dict instead of error indication
            return {}
        except requests.Timeout:
            # Bug: Returns empty dict for timeout
            return {}
        except Exception:
            # Bug: Catches all exceptions and hides them
            return {}
    
    def retry_failed_requests(self, url, max_retries=3):
        """Level 1 - Retry failed requests with bugs"""
        return self._attempt_retry(url, max_retries)
    
    def _attempt_retry(self, endpoint, retries):
        """Level 2 - Attempt retry"""
        return self._execute_with_retry(endpoint, retries)
    
    def _execute_with_retry(self, url, max_attempts):
        """Level 3 - Execute with retry (buggy implementation)"""
        for attempt in range(max_attempts + 1):  # Bug: off-by-one error
            try:
                response = requests.get(url, timeout=5)
                if response.status_code == 200:
                    return response.json()
                # Bug: Retries even for 4xx errors (client errors)
                elif response.status_code >= 400:
                    continue  # Should not retry client errors
            except requests.RequestException:
                # Bug: No exponential backoff
                time.sleep(1)  # Fixed delay
                continue
        
        # Bug: Returns None instead of proper error
        return None

class JSONProcessingBugs:
    """Class with JSON processing issues"""
    
    def parse_api_response(self, response_text):
        """Level 1 - Parse API response with bugs"""
        return self._decode_json(response_text)
    
    def _decode_json(self, json_str):
        """Level 2 - Decode JSON"""
        return self._unsafe_json_parsing(json_str)
    
    def _unsafe_json_parsing(self, data):
        """Level 3 - Unsafe JSON parsing"""
        try:
            # Bug: No validation of JSON structure
            parsed = json.loads(data)
            return parsed
        except json.JSONDecodeError:
            # Bug: Returns empty dict instead of error
            return {}
        except Exception:
            # Bug: Catches all exceptions
            return {}
    
    def serialize_request_data(self, data):
        """Level 1 - Serialize request data with bugs"""
        return self._convert_to_json(data)
    
    def _convert_to_json(self, payload):
        """Level 2 - Convert to JSON"""
        return self._json_serialization(payload)
    
    def _json_serialization(self, data):
        """Level 3 - JSON serialization (bugs)"""
        try:
            # Bug: No handling of non-serializable objects
            json_str = json.dumps(data)
            return json_str
        except TypeError:
            # Bug: Returns empty string instead of error
            return ""
        except Exception:
            # Bug: Catches all exceptions
            return ""

class AuthenticationBugs:
    """Class with authentication issues"""
    
    def __init__(self):
        self.token = None
        self.refresh_token = None
    
    def authenticate_user(self, username, password):
        """Level 1 - Authenticate user with bugs"""
        return self._login_user(username, password)
    
    def _login_user(self, user, pwd):
        """Level 2 - Login user"""
        return self._send_auth_request(user, pwd)
    
    def _send_auth_request(self, username, password):
        """Level 3 - Send auth request (security bugs)"""
        # Bug: Sends credentials in URL (GET request)
        url = f"http://api.example.com/login?username={username}&password={password}"
        
        try:
            # Bug: No HTTPS enforcement
            response = requests.get(url)  # Should be POST with HTTPS
            
            if response.status_code == 200:
                auth_data = response.json()
                # Bug: Stores token in plain text
                self.token = auth_data.get('token')
                return True
            else:
                return False
        except Exception:
            return False
    
    def refresh_authentication(self):
        """Level 1 - Refresh authentication with bugs"""
        return self._renew_token()
    
    def _renew_token(self):
        """Level 2 - Renew token"""
        return self._token_refresh_request()
    
    def _token_refresh_request(self):
        """Level 3 - Token refresh request (bugs)"""
        if not self.refresh_token:
            return False
        
        # Bug: No token expiration checking
        headers = {'Authorization': f'Bearer {self.token}'}
        
        try:
            response = requests.post(
                'http://api.example.com/refresh',  # Bug: No HTTPS
                headers=headers
            )
            
            # Bug: No proper response validation
            if response.status_code == 200:
                new_token = response.json().get('token')
                self.token = new_token
                return True
            
            return False
        except Exception:
            return False

class RateLimitingBugs:
    """Class with rate limiting issues"""
    
    def __init__(self):
        self.request_count = 0
        self.last_request_time = 0
    
    def make_rate_limited_request(self, url):
        """Level 1 - Make rate limited request with bugs"""
        return self._check_rate_limit(url)
    
    def _check_rate_limit(self, endpoint):
        """Level 2 - Check rate limit"""
        return self._execute_rate_limited_call(endpoint)
    
    def _execute_rate_limited_call(self, url):
        """Level 3 - Execute rate limited call (bugs)"""
        current_time = time.time()
        
        # Bug: Poor rate limiting logic
        if current_time - self.last_request_time < 1:  # 1 second limit
            # Bug: No proper waiting mechanism
            return None  # Should wait or queue request
        
        self.request_count += 1
        self.last_request_time = current_time
        
        try:
            response = requests.get(url)
            
            # Bug: Doesn't handle 429 (Too Many Requests) status
            if response.status_code == 429:
                return None  # Should implement backoff
            
            return response.json()
        except Exception:
            return None

# Global API utility functions with bugs
def make_api_request(method, url, data=None):
    """Global API request function with bugs"""
    return execute_http_request(method, url, data)

def execute_http_request(http_method, endpoint, payload):
    """Level 2 - Execute HTTP request"""
    return send_http_request(http_method, endpoint, payload)

def send_http_request(method, url, data):
    """Level 3 - Send HTTP request (multiple bugs)"""
    # Bug: No input validation
    # Bug: No timeout
    # Bug: No proper error handling
    
    try:
        if method.upper() == 'GET':
            response = requests.get(url)
        elif method.upper() == 'POST':
            response = requests.post(url, json=data)
        elif method.upper() == 'PUT':
            response = requests.put(url, json=data)
        else:
            # Bug: Returns None for unsupported methods
            return None
        
        # Bug: No status code checking
        return response.json()
    except Exception:
        # Bug: Swallows all exceptions
        return None
