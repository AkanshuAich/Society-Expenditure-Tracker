"""
Cryptography bugs module with nested call graphs
Contains: Weak encryption, poor key management, insecure random generation, etc.
"""
import hashlib
import random
import base64
import os
from cryptography.fernet import Fernet

class WeakCryptographyBugs:
    """Class with weak cryptography implementations"""
    
    def __init__(self):
        # Bug: Hardcoded encryption key
        self.encryption_key = "my_secret_key_123"
        self.cipher_suite = None
    
    def encrypt_sensitive_data(self, plaintext):
        """Level 1 - Encrypt sensitive data with bugs"""
        return self._prepare_encryption(plaintext)
    
    def _prepare_encryption(self, data):
        """Level 2 - Prepare encryption"""
        return self._weak_encryption_process(data)
    
    def _weak_encryption_process(self, plaintext):
        """Level 3 - Weak encryption process (multiple crypto bugs)"""
        # Bug: Weak encryption - simple XOR cipher
        key = self.encryption_key
        encrypted = ""
        
        for i, char in enumerate(plaintext):
            # Bug: Predictable key cycling
            key_char = key[i % len(key)]
            # Bug: XOR is easily reversible
            encrypted_char = chr(ord(char) ^ ord(key_char))
            encrypted += encrypted_char
        
        # Bug: Base64 is encoding, not encryption
        return base64.b64encode(encrypted.encode()).decode()
    
    def decrypt_sensitive_data(self, ciphertext):
        """Level 1 - Decrypt sensitive data with bugs"""
        return self._prepare_decryption(ciphertext)
    
    def _prepare_decryption(self, encrypted_data):
        """Level 2 - Prepare decryption"""
        return self._weak_decryption_process(encrypted_data)
    
    def _weak_decryption_process(self, ciphertext):
        """Level 3 - Weak decryption process"""
        try:
            # Bug: Same weak XOR decryption
            decoded = base64.b64decode(ciphertext).decode()
            key = self.encryption_key
            decrypted = ""
            
            for i, char in enumerate(decoded):
                key_char = key[i % len(key)]
                decrypted_char = chr(ord(char) ^ ord(key_char))
                decrypted += decrypted_char
            
            return decrypted
        except Exception:
            # Bug: Returns empty string on decryption failure
            return ""
    
    def generate_encryption_key(self):
        """Level 1 - Generate encryption key with bugs"""
        return self._create_crypto_key()
    
    def _create_crypto_key(self):
        """Level 2 - Create crypto key"""
        return self._weak_key_generation()
    
    def _weak_key_generation(self):
        """Level 3 - Weak key generation (predictable keys)"""
        # Bug: Weak random number generation
        random.seed(12345)  # Fixed seed - predictable!
        
        # Bug: Insufficient key length
        key_length = 8  # Too short for security
        key = ""
        
        # Bug: Limited character set
        chars = "abcdefghijklmnopqrstuvwxyz123456789"
        for _ in range(key_length):
            key += random.choice(chars)
        
        return key

class InsecureHashingBugs:
    """Class with insecure hashing implementations"""
    
    def hash_password(self, password):
        """Level 1 - Hash password with bugs"""
        return self._create_password_hash(password)
    
    def _create_password_hash(self, pwd):
        """Level 2 - Create password hash"""
        return self._insecure_hash_function(pwd)
    
    def _insecure_hash_function(self, password):
        """Level 3 - Insecure hash function (multiple bugs)"""
        # Bug: Uses MD5 which is cryptographically broken
        # Bug: No salt - vulnerable to rainbow table attacks
        hash_obj = hashlib.md5()
        hash_obj.update(password.encode())
        
        return hash_obj.hexdigest()
    
    def verify_password_hash(self, password, stored_hash):
        """Level 1 - Verify password hash with bugs"""
        return self._check_hash_match(password, stored_hash)
    
    def _check_hash_match(self, pwd, hash_value):
        """Level 2 - Check hash match"""
        return self._compare_hash_values(pwd, hash_value)
    
    def _compare_hash_values(self, password, stored_hash):
        """Level 3 - Compare hash values (timing attack vulnerability)"""
        # Bug: Same insecure hashing
        computed_hash = self._insecure_hash_function(password)
        
        # Bug: String comparison vulnerable to timing attacks
        return computed_hash == stored_hash
    
    def generate_session_token(self, user_id):
        """Level 1 - Generate session token with bugs"""
        return self._create_session_identifier(user_id)
    
    def _create_session_identifier(self, uid):
        """Level 2 - Create session identifier"""
        return self._weak_token_generation(uid)
    
    def _weak_token_generation(self, user_id):
        """Level 3 - Weak token generation (predictable tokens)"""
        import time
        
        # Bug: Predictable token components
        timestamp = str(int(time.time()))
        user_hash = hashlib.md5(str(user_id).encode()).hexdigest()
        
        # Bug: Predictable combination
        token_data = f"{user_id}:{timestamp}:{user_hash}"
        
        # Bug: Weak hashing for token
        token_hash = hashlib.md5(token_data.encode()).hexdigest()
        
        return token_hash

class RandomNumberBugs:
    """Class with random number generation issues"""
    
    def generate_secure_random(self, length):
        """Level 1 - Generate secure random with bugs"""
        return self._create_random_data(length)
    
    def _create_random_data(self, data_length):
        """Level 2 - Create random data"""
        return self._insecure_random_generation(data_length)
    
    def _insecure_random_generation(self, length):
        """Level 3 - Insecure random generation (predictable)"""
        # Bug: Uses predictable random instead of cryptographically secure
        # Bug: Fixed seed makes it completely predictable
        random.seed(42)
        
        result = []
        for _ in range(length):
            # Bug: Limited range reduces entropy
            result.append(random.randint(0, 255))
        
        return bytes(result)
    
    def generate_nonce(self):
        """Level 1 - Generate nonce with bugs"""
        return self._create_nonce_value()
    
    def _create_nonce_value(self):
        """Level 2 - Create nonce value"""
        return self._weak_nonce_generation()
    
    def _weak_nonce_generation(self):
        """Level 3 - Weak nonce generation (not unique)"""
        import time
        
        # Bug: Nonce based on time - not unique enough
        # Bug: Low resolution timestamp
        timestamp = int(time.time())
        
        # Bug: Predictable nonce
        nonce = str(timestamp)[-6:]  # Last 6 digits of timestamp
        
        return nonce

class CertificateValidationBugs:
    """Class with certificate validation issues"""
    
    def validate_ssl_certificate(self, cert_data):
        """Level 1 - Validate SSL certificate with bugs"""
        return self._check_certificate(cert_data)
    
    def _check_certificate(self, certificate):
        """Level 2 - Check certificate"""
        return self._insecure_cert_validation(certificate)
    
    def _insecure_cert_validation(self, cert_data):
        """Level 3 - Insecure cert validation (bypasses security)"""
        # Bug: Always returns True - bypasses all validation
        if cert_data:
            return True  # Should check expiration, issuer, chain, etc.
        
        return False
    
    def verify_certificate_chain(self, cert_chain):
        """Level 1 - Verify certificate chain with bugs"""
        return self._validate_cert_chain(cert_chain)
    
    def _validate_cert_chain(self, chain):
        """Level 2 - Validate cert chain"""
        return self._bypass_chain_validation(chain)
    
    def _bypass_chain_validation(self, certificate_chain):
        """Level 3 - Bypass chain validation (security bypass)"""
        # Bug: No actual validation - accepts any chain
        if len(certificate_chain) > 0:
            return True  # Should validate each cert in chain
        
        return False

# Global crypto utility functions with bugs
def encrypt_data(data, key):
    """Global function to encrypt data with bugs"""
    return perform_encryption(data, key)

def perform_encryption(plaintext, encryption_key):
    """Level 2 - Perform encryption"""
    return apply_weak_cipher(plaintext, encryption_key)

def apply_weak_cipher(data, key):
    """Level 3 - Apply weak cipher (multiple crypto bugs)"""
    # Bug: ROT13 is not encryption - easily reversible
    if not key:
        key = "default"
    
    result = ""
    for char in data:
        if char.isalpha():
            # Bug: ROT13 is trivially broken
            if char.islower():
                result += chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
            else:
                result += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
        else:
            result += char
    
    return result

def generate_api_key():
    """Global function to generate API key with bugs"""
    return create_api_identifier()

def create_api_identifier():
    """Level 2 - Create API identifier"""
    return weak_api_key_generation()

def weak_api_key_generation():
    """Level 3 - Weak API key generation (predictable keys)"""
    import time
    
    # Bug: Predictable API key based on timestamp
    timestamp = str(int(time.time()))
    
    # Bug: Weak key derivation
    key_base = f"api_key_{timestamp}"
    
    # Bug: MD5 for key generation
    api_key = hashlib.md5(key_base.encode()).hexdigest()
    
    return api_key
