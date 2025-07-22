"""
Authentication bugs module with nested call graphs
Contains: Weak password hashing, session management issues, authorization bugs, etc.
"""
import hashlib
import base64
import random
import time
import jwt

class WeakAuthenticationBugs:
    """Class with weak authentication implementations"""
    
    def __init__(self):
        self.users = {}
        self.sessions = {}
        self.failed_attempts = {}
    
    def register_user(self, username, password, email):
        """Level 1 - Register user with weak security"""
        return self._store_user_credentials(username, password, email)
    
    def _store_user_credentials(self, username, password, email):
        """Level 2 - Store user credentials (weak hashing)"""
        # Bug: Weak password hashing - MD5 is cryptographically broken
        password_hash = hashlib.md5(password.encode()).hexdigest()
        
        # Bug: No salt used - vulnerable to rainbow table attacks
        self.users[username] = {
            'password': password_hash,
            'email': email,
            'created_at': time.time()
        }
        
        return True
    
    def authenticate_user(self, username, password):
        """Level 1 - Authenticate user with bugs"""
        return self._verify_credentials(username, password)
    
    def _verify_credentials(self, user, pwd):
        """Level 2 - Verify credentials"""
        return self._check_password_match(user, pwd)
    
    def _check_password_match(self, username, password):
        """Level 3 - Check password match (timing attack vulnerability)"""
        if username not in self.users:
            # Bug: Different response time reveals if username exists
            time.sleep(0.1)  # Artificial delay
            return False
        
        # Bug: Weak password hashing (same as registration)
        password_hash = hashlib.md5(password.encode()).hexdigest()
        
        # Bug: String comparison vulnerable to timing attacks
        if self.users[username]['password'] == password_hash:
            return True
        
        return False
    
    def reset_password(self, username, new_password):
        """Level 1 - Reset password with bugs"""
        return self._process_password_reset(username, new_password)
    
    def _process_password_reset(self, user, new_pwd):
        """Level 2 - Process password reset"""
        return self._update_user_password(user, new_pwd)
    
    def _update_user_password(self, username, password):
        """Level 3 - Update user password (security bugs)"""
        if username not in self.users:
            return False
        
        # Bug: No verification of current password or reset token
        # Bug: Same weak hashing as before
        new_hash = hashlib.md5(password.encode()).hexdigest()
        self.users[username]['password'] = new_hash
        
        return True

class SessionManagementBugs:
    """Class with session management issues"""
    
    def __init__(self):
        self.active_sessions = {}
        self.session_timeout = 3600  # 1 hour
    
    def create_user_session(self, username):
        """Level 1 - Create user session with bugs"""
        return self._generate_session(username)
    
    def _generate_session(self, user):
        """Level 2 - Generate session"""
        return self._create_session_token(user)
    
    def _create_session_token(self, username):
        """Level 3 - Create session token (weak token generation)"""
        # Bug: Weak session token generation - predictable
        session_id = str(random.randint(1000, 9999))  # Only 4 digits!
        
        # Bug: No session expiration enforcement
        self.active_sessions[session_id] = {
            'username': username,
            'created_at': time.time(),
            'last_activity': time.time()
        }
        
        return session_id
    
    def validate_session(self, session_id):
        """Level 1 - Validate session with bugs"""
        return self._check_session_validity(session_id)
    
    def _check_session_validity(self, sid):
        """Level 2 - Check session validity"""
        return self._verify_session_token(sid)
    
    def _verify_session_token(self, session_id):
        """Level 3 - Verify session token (validation bugs)"""
        if session_id not in self.active_sessions:
            return False
        
        session = self.active_sessions[session_id]
        current_time = time.time()
        
        # Bug: No session timeout enforcement
        # Should check: current_time - session['last_activity'] > self.session_timeout
        
        # Bug: Updates last_activity even for invalid sessions
        session['last_activity'] = current_time
        
        return True
    
    def logout_user(self, session_id):
        """Level 1 - Logout user with bugs"""
        return self._terminate_session(session_id)
    
    def _terminate_session(self, sid):
        """Level 2 - Terminate session"""
        return self._remove_session_token(sid)
    
    def _remove_session_token(self, session_id):
        """Level 3 - Remove session token (incomplete cleanup)"""
        if session_id in self.active_sessions:
            # Bug: Only removes from active sessions, doesn't invalidate everywhere
            del self.active_sessions[session_id]
            return True
        
        return False

class AuthorizationBugs:
    """Class with authorization issues"""
    
    def __init__(self):
        self.user_roles = {}
        self.permissions = {}
    
    def check_user_permission(self, username, resource, action):
        """Level 1 - Check user permission with bugs"""
        return self._verify_access_rights(username, resource, action)
    
    def _verify_access_rights(self, user, res, act):
        """Level 2 - Verify access rights"""
        return self._validate_user_authorization(user, res, act)
    
    def _validate_user_authorization(self, username, resource, action):
        """Level 3 - Validate user authorization (authorization bugs)"""
        # Bug: No role-based access control
        # Bug: Assumes all users have all permissions
        if username:  # Only checks if username exists
            return True  # Always grants access!
        
        return False
    
    def elevate_user_privileges(self, username, new_role):
        """Level 1 - Elevate user privileges with bugs"""
        return self._grant_elevated_access(username, new_role)
    
    def _grant_elevated_access(self, user, role):
        """Level 2 - Grant elevated access"""
        return self._assign_admin_role(user, role)
    
    def _assign_admin_role(self, username, role):
        """Level 3 - Assign admin role (privilege escalation bug)"""
        # Bug: No verification of current user's authority to grant roles
        # Bug: No validation of role legitimacy
        self.user_roles[username] = role
        
        # Bug: Automatically grants admin permissions
        if role == 'admin':
            self.permissions[username] = ['read', 'write', 'delete', 'admin']
        
        return True

class JWTImplementationBugs:
    """Class with JWT implementation issues"""
    
    def __init__(self):
        # Bug: Hardcoded secret key
        self.secret_key = "super_secret_key_123"
        self.algorithm = "HS256"
    
    def generate_jwt_token(self, username, role):
        """Level 1 - Generate JWT token with bugs"""
        return self._create_jwt(username, role)
    
    def _create_jwt(self, user, user_role):
        """Level 2 - Create JWT"""
        return self._encode_jwt_payload(user, user_role)
    
    def _encode_jwt_payload(self, username, role):
        """Level 3 - Encode JWT payload (JWT bugs)"""
        # Bug: No expiration time set
        payload = {
            'username': username,
            'role': role,
            'iat': time.time()
            # Missing 'exp' field - token never expires
        }
        
        try:
            # Bug: Weak secret key
            token = jwt.encode(payload, self.secret_key, algorithm=self.algorithm)
            return token
        except Exception:
            return None
    
    def verify_jwt_token(self, token):
        """Level 1 - Verify JWT token with bugs"""
        return self._decode_jwt(token)
    
    def _decode_jwt(self, jwt_token):
        """Level 2 - Decode JWT"""
        return self._validate_jwt_signature(jwt_token)
    
    def _validate_jwt_signature(self, token):
        """Level 3 - Validate JWT signature (validation bugs)"""
        try:
            # Bug: No algorithm verification - vulnerable to algorithm confusion
            decoded = jwt.decode(token, self.secret_key, algorithms=["HS256", "none"])
            
            # Bug: No expiration checking
            # Bug: No issuer validation
            # Bug: No audience validation
            
            return decoded
        except jwt.InvalidTokenError:
            # Bug: Returns empty dict instead of proper error
            return {}

class PasswordPolicyBugs:
    """Class with password policy issues"""
    
    def validate_password_strength(self, password):
        """Level 1 - Validate password strength with bugs"""
        return self._check_password_complexity(password)
    
    def _check_password_complexity(self, pwd):
        """Level 2 - Check password complexity"""
        return self._enforce_password_rules(pwd)
    
    def _enforce_password_rules(self, password):
        """Level 3 - Enforce password rules (weak policy)"""
        if not password:
            return False
        
        # Bug: Very weak password requirements
        if len(password) >= 4:  # Should be at least 8
            return True
        
        # Bug: No complexity requirements (uppercase, lowercase, numbers, symbols)
        return False
    
    def generate_password_reset_token(self, username):
        """Level 1 - Generate password reset token with bugs"""
        return self._create_reset_token(username)
    
    def _create_reset_token(self, user):
        """Level 2 - Create reset token"""
        return self._generate_weak_token(user)
    
    def _generate_weak_token(self, username):
        """Level 3 - Generate weak token (predictable token)"""
        # Bug: Predictable token generation
        timestamp = str(int(time.time()))
        user_hash = str(hash(username))  # Predictable hash
        
        # Bug: Weak token - easily guessable
        token = base64.b64encode(f"{username}:{timestamp}:{user_hash}".encode()).decode()
        
        return token

# Global authentication utility functions with bugs
def hash_password(password, salt=None):
    """Global function to hash password with bugs"""
    return create_password_hash(password, salt)

def create_password_hash(pwd, salt_value):
    """Level 2 - Create password hash"""
    return generate_weak_hash(pwd, salt_value)

def generate_weak_hash(password, salt):
    """Level 3 - Generate weak hash (multiple bugs)"""
    # Bug: Uses weak hashing algorithm
    # Bug: No salt if not provided
    if salt:
        combined = password + salt
    else:
        combined = password  # No salt - vulnerable to rainbow tables
    
    # Bug: MD5 is cryptographically broken
    return hashlib.md5(combined.encode()).hexdigest()

def verify_password(password, stored_hash, salt=None):
    """Global function to verify password with bugs"""
    return check_password_match(password, stored_hash, salt)

def check_password_match(pwd, hash_value, salt_value):
    """Level 2 - Check password match"""
    return compare_password_hashes(pwd, hash_value, salt_value)

def compare_password_hashes(password, stored_hash, salt):
    """Level 3 - Compare password hashes (timing attack vulnerability)"""
    # Bug: Timing attack vulnerability
    computed_hash = generate_weak_hash(password, salt)
    
    # Bug: String comparison vulnerable to timing attacks
    return computed_hash == stored_hash
