"""
Network bugs module with nested call graphs
Contains: Socket handling issues, SSL/TLS problems, timeout issues, etc.
"""
import socket
import ssl
import urllib.request
import urllib.error
import time

class NetworkConnectionBugs:
    """Class with network connection issues"""
    
    def __init__(self):
        self.connections = []
        self.timeout = 30
    
    def create_tcp_connection(self, host, port):
        """Level 1 - Create TCP connection with bugs"""
        return self._establish_socket_connection(host, port)
    
    def _establish_socket_connection(self, hostname, port_num):
        """Level 2 - Establish socket connection"""
        return self._connect_to_server(hostname, port_num)
    
    def _connect_to_server(self, host, port):
        """Level 3 - Connect to server (connection bugs)"""
        try:
            # Bug: No timeout set - can hang indefinitely
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((host, port))  # No timeout
            
            # Bug: Socket not properly closed on error
            self.connections.append(sock)
            return sock
        except socket.error:
            # Bug: Socket leaked if exception occurs after creation
            return None
    
    def send_data_over_socket(self, sock, data):
        """Level 1 - Send data over socket with bugs"""
        return self._transmit_socket_data(sock, data)
    
    def _transmit_socket_data(self, socket_obj, payload):
        """Level 2 - Transmit socket data"""
        return self._unsafe_socket_send(socket_obj, payload)
    
    def _unsafe_socket_send(self, sock, data):
        """Level 3 - Unsafe socket send (multiple bugs)"""
        try:
            # Bug: No encoding specified - will fail on non-ASCII
            # Bug: No partial send handling
            bytes_sent = sock.send(data)  # Assumes data is bytes
            
            # Bug: Doesn't check if all data was sent
            return bytes_sent
        except socket.error:
            # Bug: Doesn't handle socket errors properly
            return 0
    
    def receive_socket_data(self, sock, buffer_size=1024):
        """Level 1 - Receive socket data with bugs"""
        return self._read_socket_data(sock, buffer_size)
    
    def _read_socket_data(self, socket_obj, buf_size):
        """Level 2 - Read socket data"""
        return self._unsafe_socket_receive(socket_obj, buf_size)
    
    def _unsafe_socket_receive(self, sock, buffer_size):
        """Level 3 - Unsafe socket receive (bugs)"""
        try:
            # Bug: No timeout - can block indefinitely
            # Bug: Doesn't handle partial receives
            data = sock.recv(buffer_size)
            
            # Bug: No handling of connection closed by peer
            if not data:
                return b""  # Should indicate connection closed
            
            return data
        except socket.error:
            # Bug: Returns empty bytes instead of error indication
            return b""

class SSLTLSBugs:
    """Class with SSL/TLS implementation issues"""
    
    def create_ssl_connection(self, hostname, port):
        """Level 1 - Create SSL connection with bugs"""
        return self._setup_ssl_socket(hostname, port)
    
    def _setup_ssl_socket(self, host, port_num):
        """Level 2 - Setup SSL socket"""
        return self._establish_secure_connection(host, port_num)
    
    def _establish_secure_connection(self, hostname, port):
        """Level 3 - Establish secure connection (SSL bugs)"""
        try:
            # Bug: Creates insecure SSL context
            context = ssl.create_default_context()
            # Bug: Disables certificate verification
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE  # Dangerous!
            
            # Bug: No timeout set
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            ssl_sock = context.wrap_socket(sock, server_hostname=hostname)
            ssl_sock.connect((hostname, port))
            
            return ssl_sock
        except (socket.error, ssl.SSLError):
            return None
    
    def verify_ssl_certificate(self, ssl_socket):
        """Level 1 - Verify SSL certificate with bugs"""
        return self._check_certificate_validity(ssl_socket)
    
    def _check_certificate_validity(self, ssl_sock):
        """Level 2 - Check certificate validity"""
        return self._validate_cert_chain(ssl_sock)
    
    def _validate_cert_chain(self, ssl_socket):
        """Level 3 - Validate cert chain (validation bugs)"""
        try:
            # Bug: Gets certificate but doesn't validate it properly
            cert = ssl_socket.getpeercert()
            
            # Bug: Only checks if certificate exists, not validity
            if cert:
                return True  # Should check expiration, issuer, etc.
            
            return False
        except ssl.SSLError:
            # Bug: Returns True on SSL error
            return True

class HTTPClientBugs:
    """Class with HTTP client issues"""
    
    def make_http_request(self, url, method='GET', data=None):
        """Level 1 - Make HTTP request with bugs"""
        return self._send_http_request(url, method, data)
    
    def _send_http_request(self, endpoint, http_method, payload):
        """Level 2 - Send HTTP request"""
        return self._execute_http_call(endpoint, http_method, payload)
    
    def _execute_http_call(self, url, method, data):
        """Level 3 - Execute HTTP call (multiple bugs)"""
        try:
            if method.upper() == 'GET':
                # Bug: No timeout - can hang indefinitely
                response = urllib.request.urlopen(url)
            elif method.upper() == 'POST':
                # Bug: No proper encoding of POST data
                # Bug: No Content-Type header
                req = urllib.request.Request(url, data=data)
                response = urllib.request.urlopen(req)  # No timeout
            else:
                return None
            
            # Bug: No status code checking
            return response.read()
        except urllib.error.URLError:
            # Bug: Returns None instead of proper error handling
            return None
        except Exception:
            return None
    
    def download_file(self, url, filename):
        """Level 1 - Download file with bugs"""
        return self._fetch_remote_file(url, filename)
    
    def _fetch_remote_file(self, file_url, local_filename):
        """Level 2 - Fetch remote file"""
        return self._save_downloaded_file(file_url, local_filename)
    
    def _save_downloaded_file(self, url, filename):
        """Level 3 - Save downloaded file (bugs)"""
        try:
            # Bug: No timeout
            # Bug: No file size limit - can download huge files
            response = urllib.request.urlopen(url)
            
            # Bug: No filename validation - path traversal possible
            with open(filename, 'wb') as f:
                # Bug: Loads entire file into memory
                data = response.read()  # Memory issue for large files
                f.write(data)
            
            return True
        except (urllib.error.URLError, IOError):
            return False

class NetworkTimeoutBugs:
    """Class with network timeout issues"""
    
    def connect_with_timeout(self, host, port, timeout_seconds):
        """Level 1 - Connect with timeout bugs"""
        return self._attempt_timed_connection(host, port, timeout_seconds)
    
    def _attempt_timed_connection(self, hostname, port_num, timeout):
        """Level 2 - Attempt timed connection"""
        return self._establish_connection_with_timeout(hostname, port_num, timeout)
    
    def _establish_connection_with_timeout(self, host, port, timeout):
        """Level 3 - Establish connection with timeout (timeout bugs)"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            # Bug: Sets socket timeout but doesn't handle timeout exception properly
            sock.settimeout(timeout)
            sock.connect((host, port))
            
            # Bug: Removes timeout after connection - subsequent operations can hang
            sock.settimeout(None)
            
            return sock
        except socket.timeout:
            # Bug: Socket not closed on timeout
            return None
        except socket.error:
            return None
    
    def read_with_timeout(self, sock, timeout_seconds):
        """Level 1 - Read with timeout bugs"""
        return self._perform_timed_read(sock, timeout_seconds)
    
    def _perform_timed_read(self, socket_obj, timeout):
        """Level 2 - Perform timed read"""
        return self._execute_timeout_read(socket_obj, timeout)
    
    def _execute_timeout_read(self, sock, timeout):
        """Level 3 - Execute timeout read (timeout handling bugs)"""
        try:
            # Bug: Sets timeout but doesn't restore original timeout
            original_timeout = sock.gettimeout()
            sock.settimeout(timeout)
            
            data = sock.recv(1024)
            
            # Bug: Doesn't restore original timeout
            # sock.settimeout(original_timeout)  # Missing!
            
            return data
        except socket.timeout:
            # Bug: Returns empty bytes instead of timeout indication
            return b""
        except socket.error:
            return b""

# Global network utility functions with bugs
def create_server_socket(port, backlog=5):
    """Global function to create server socket with bugs"""
    return setup_listening_socket(port, backlog)

def setup_listening_socket(port_num, connection_backlog):
    """Level 2 - Setup listening socket"""
    return bind_server_socket(port_num, connection_backlog)

def bind_server_socket(port, backlog):
    """Level 3 - Bind server socket (multiple bugs)"""
    try:
        # Bug: No address reuse option - can fail to bind after restart
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Missing!
        
        # Bug: Binds to all interfaces without security consideration
        sock.bind(('0.0.0.0', port))  # Should bind to specific interface
        sock.listen(backlog)
        
        return sock
    except socket.error:
        return None

def send_email_notification(smtp_server, recipient, message):
    """Global function to send email with bugs"""
    return transmit_email_message(smtp_server, recipient, message)

def transmit_email_message(server, to_address, msg):
    """Level 2 - Transmit email message"""
    return deliver_email_unsafe(server, to_address, msg)

def deliver_email_unsafe(smtp_server, recipient, message):
    """Level 3 - Deliver email unsafe (multiple bugs)"""
    import smtplib
    
    try:
        # Bug: No SSL/TLS encryption
        server = smtplib.SMTP(smtp_server, 25)  # Unencrypted
        
        # Bug: No authentication
        # Bug: No input validation
        server.sendmail("noreply@example.com", recipient, message)
        
        # Bug: Server connection not properly closed
        # server.quit()  # Missing!
        
        return True
    except smtplib.SMTPException:
        return False
