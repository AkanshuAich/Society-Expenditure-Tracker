"""
Web security bugs module with nested call graphs
Contains: XSS, CSRF, injection attacks, insecure redirects, etc.
"""
import urllib.parse
import html
import re

class XSSVulnerabilities:
    """Class with Cross-Site Scripting vulnerabilities"""
    
    def __init__(self):
        self.user_comments = []
        self.search_results = []
    
    def process_user_comment(self, comment):
        """Level 1 - Process user comment with XSS bugs"""
        return self._sanitize_user_input(comment)
    
    def _sanitize_user_input(self, user_input):
        """Level 2 - Sanitize user input"""
        return self._unsafe_html_processing(user_input)
    
    def _unsafe_html_processing(self, input_data):
        """Level 3 - Unsafe HTML processing (XSS vulnerability)"""
        # Bug: No HTML escaping - allows script injection
        processed_comment = input_data  # Direct use without sanitization
        
        # Bug: Insufficient sanitization
        processed_comment = processed_comment.replace("<script>", "")  # Only exact match
        # Missing: <script>, <img onerror=>, <svg onload=>, etc.
        
        self.user_comments.append(processed_comment)
        return processed_comment
    
    def search_user_data(self, search_term):
        """Level 1 - Search user data with XSS bugs"""
        return self._perform_search(search_term)
    
    def _perform_search(self, query):
        """Level 2 - Perform search"""
        return self._display_search_results(query)
    
    def _display_search_results(self, search_query):
        """Level 3 - Display search results (reflected XSS)"""
        # Bug: Reflects user input without escaping
        results_html = f"<h2>Search results for: {search_query}</h2>"
        
        # Bug: User input directly embedded in HTML
        for comment in self.user_comments:
            if search_query.lower() in comment.lower():
                # Bug: No HTML escaping
                results_html += f"<div>{comment}</div>"
        
        return results_html
    
    def generate_user_profile(self, username, bio):
        """Level 1 - Generate user profile with XSS bugs"""
        return self._create_profile_html(username, bio)
    
    def _create_profile_html(self, user, biography):
        """Level 2 - Create profile HTML"""
        return self._unsafe_profile_generation(user, biography)
    
    def _unsafe_profile_generation(self, username, bio):
        """Level 3 - Unsafe profile generation (stored XSS)"""
        # Bug: Stored XSS - malicious content stored and displayed
        profile_html = f"""
        <div class="profile">
            <h1>Profile: {username}</h1>
            <p>Bio: {bio}</p>
        </div>
        """
        
        # Bug: No content validation or escaping
        return profile_html

class CSRFVulnerabilities:
    """Class with Cross-Site Request Forgery vulnerabilities"""
    
    def __init__(self):
        self.user_sessions = {}
        self.transactions = []
    
    def process_money_transfer(self, from_account, to_account, amount):
        """Level 1 - Process money transfer with CSRF bugs"""
        return self._execute_transfer(from_account, to_account, amount)
    
    def _execute_transfer(self, from_acc, to_acc, transfer_amount):
        """Level 2 - Execute transfer"""
        return self._unsafe_transfer_processing(from_acc, to_acc, transfer_amount)
    
    def _unsafe_transfer_processing(self, from_account, to_account, amount):
        """Level 3 - Unsafe transfer processing (CSRF vulnerability)"""
        # Bug: No CSRF token validation
        # Bug: Accepts GET requests for state-changing operations
        
        transaction = {
            'from': from_account,
            'to': to_account,
            'amount': amount,
            'timestamp': 'now'
        }
        
        # Bug: No verification of request origin
        self.transactions.append(transaction)
        return True
    
    def change_user_password(self, username, new_password):
        """Level 1 - Change user password with CSRF bugs"""
        return self._update_password(username, new_password)
    
    def _update_password(self, user, pwd):
        """Level 2 - Update password"""
        return self._unsafe_password_change(user, pwd)
    
    def _unsafe_password_change(self, username, password):
        """Level 3 - Unsafe password change (CSRF vulnerability)"""
        # Bug: No CSRF protection on sensitive operation
        # Bug: No current password verification
        
        if username in self.user_sessions:
            # Bug: Password change without proper authentication
            self.user_sessions[username]['password'] = password
            return True
        
        return False
    
    def delete_user_account(self, username):
        """Level 1 - Delete user account with CSRF bugs"""
        return self._remove_user_account(username)
    
    def _remove_user_account(self, user):
        """Level 2 - Remove user account"""
        return self._unsafe_account_deletion(user)
    
    def _unsafe_account_deletion(self, username):
        """Level 3 - Unsafe account deletion (CSRF vulnerability)"""
        # Bug: Critical operation without CSRF protection
        if username in self.user_sessions:
            del self.user_sessions[username]
            return True
        
        return False

class InsecureRedirectBugs:
    """Class with insecure redirect vulnerabilities"""
    
    def redirect_after_login(self, redirect_url):
        """Level 1 - Redirect after login with bugs"""
        return self._process_redirect(redirect_url)
    
    def _process_redirect(self, url):
        """Level 2 - Process redirect"""
        return self._unsafe_redirect_handling(url)
    
    def _unsafe_redirect_handling(self, redirect_url):
        """Level 3 - Unsafe redirect handling (open redirect)"""
        # Bug: No URL validation - allows redirect to any site
        if redirect_url:
            # Bug: Direct redirect without validation
            return f"Location: {redirect_url}"  # Dangerous redirect
        
        return "Location: /dashboard"
    
    def handle_logout_redirect(self, next_url):
        """Level 1 - Handle logout redirect with bugs"""
        return self._process_logout_redirect(next_url)
    
    def _process_logout_redirect(self, url):
        """Level 2 - Process logout redirect"""
        return self._validate_redirect_url(url)
    
    def _validate_redirect_url(self, url):
        """Level 3 - Validate redirect URL (insufficient validation)"""
        # Bug: Weak URL validation
        if url and url.startswith('http'):
            # Bug: Allows any HTTP/HTTPS URL
            return url  # Should validate against whitelist
        
        return '/login'

class HTTPHeaderBugs:
    """Class with HTTP header security issues"""
    
    def set_security_headers(self, response):
        """Level 1 - Set security headers with bugs"""
        return self._configure_headers(response)
    
    def _configure_headers(self, resp):
        """Level 2 - Configure headers"""
        return self._unsafe_header_setup(resp)
    
    def _unsafe_header_setup(self, response):
        """Level 3 - Unsafe header setup (missing security headers)"""
        # Bug: Missing critical security headers
        headers = {
            'Content-Type': 'text/html',
            # Missing: X-Frame-Options, X-XSS-Protection, X-Content-Type-Options
            # Missing: Content-Security-Policy, Strict-Transport-Security
        }
        
        # Bug: Allows framing from any origin
        # headers['X-Frame-Options'] = 'DENY'  # Missing!
        
        return headers
    
    def handle_cors_request(self, origin):
        """Level 1 - Handle CORS request with bugs"""
        return self._process_cors(origin)
    
    def _process_cors(self, request_origin):
        """Level 2 - Process CORS"""
        return self._unsafe_cors_handling(request_origin)
    
    def _unsafe_cors_handling(self, origin):
        """Level 3 - Unsafe CORS handling (overly permissive)"""
        # Bug: Allows all origins
        cors_headers = {
            'Access-Control-Allow-Origin': '*',  # Too permissive!
            'Access-Control-Allow-Methods': '*',  # Too permissive!
            'Access-Control-Allow-Headers': '*',  # Too permissive!
            'Access-Control-Allow-Credentials': 'true'  # Dangerous with *
        }
        
        return cors_headers

class SessionManagementBugs:
    """Class with session management security issues"""
    
    def __init__(self):
        self.sessions = {}
    
    def create_user_session(self, username):
        """Level 1 - Create user session with bugs"""
        return self._generate_session(username)
    
    def _generate_session(self, user):
        """Level 2 - Generate session"""
        return self._unsafe_session_creation(user)
    
    def _unsafe_session_creation(self, username):
        """Level 3 - Unsafe session creation (weak session management)"""
        import time
        
        # Bug: Predictable session ID
        session_id = f"{username}_{int(time.time())}"
        
        # Bug: No session expiration
        # Bug: No secure flag for cookies
        # Bug: No HttpOnly flag
        session_data = {
            'username': username,
            'created': time.time(),
            'secure': False,  # Bug: Not secure
            'httponly': False  # Bug: Accessible via JavaScript
        }
        
        self.sessions[session_id] = session_data
        return session_id
    
    def validate_session(self, session_id):
        """Level 1 - Validate session with bugs"""
        return self._check_session(session_id)
    
    def _check_session(self, sid):
        """Level 2 - Check session"""
        return self._unsafe_session_validation(sid)
    
    def _unsafe_session_validation(self, session_id):
        """Level 3 - Unsafe session validation (no timeout check)"""
        # Bug: No session timeout validation
        # Bug: No session fixation protection
        if session_id in self.sessions:
            return True  # Should check expiration
        
        return False

# Global web security utility functions with bugs
def sanitize_html_input(html_content):
    """Global function to sanitize HTML with bugs"""
    return clean_html_content(html_content)

def clean_html_content(content):
    """Level 2 - Clean HTML content"""
    return insufficient_html_sanitization(content)

def insufficient_html_sanitization(html_input):
    """Level 3 - Insufficient HTML sanitization (XSS vulnerability)"""
    # Bug: Insufficient sanitization - only removes obvious scripts
    cleaned = html_input.replace('<script>', '')
    cleaned = cleaned.replace('</script>', '')
    
    # Bug: Doesn't handle other XSS vectors
    # Missing: <img onerror=>, <svg onload=>, javascript: URLs, etc.
    
    return cleaned

def validate_user_input(user_input):
    """Global function to validate user input with bugs"""
    return check_input_safety(user_input)

def check_input_safety(input_data):
    """Level 2 - Check input safety"""
    return weak_input_validation(input_data)

def weak_input_validation(data):
    """Level 3 - Weak input validation (insufficient checks)"""
    # Bug: Only checks for obvious malicious patterns
    dangerous_patterns = ['<script>', 'javascript:', 'onload=']
    
    for pattern in dangerous_patterns:
        if pattern in data.lower():
            return False
    
    # Bug: Doesn't check for many other XSS vectors
    return True  # Passes many malicious inputs
