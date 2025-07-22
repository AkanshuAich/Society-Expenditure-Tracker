"""
API integration and network issues
"""
import requests
import json

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        self.api_key = "hardcoded_api_key_123"  # Security issue
    
    def fetch_user_data(self, user_id):
        # No input validation or error handling
        url = f"{self.base_url}/users/{user_id}"
        
        # Depth 1 nesting
        response = self.make_request(url)
        return self.process_response(response)
    
    def make_request(self, url):
        # No timeout, no retry logic
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        
        # Depth 2 nesting
        return self.send_http_request(url, headers)
    
    def send_http_request(self, url, headers):
        # No exception handling for network errors
        response = requests.get(url, headers=headers)
        return response
    
    def process_response(self, response):
        # No status code checking
        return response.json()  # Crashes if not JSON

class DataSyncer:
    def __init__(self):
        self.endpoints = []
        self.failed_requests = []
    
    def sync_data(self, data_list):
        # No rate limiting
        results = []
        for data in data_list:
            # Depth 1 nesting
            result = self.upload_data(data)
            results.append(result)
        return results
    
    def upload_data(self, data):
        # Depth 2 nesting with poor error handling
        try:
            return self.post_to_api(data)
        except:
            # Swallows all exceptions
            return None
    
    def post_to_api(self, data):
        # Hardcoded endpoint
        url = "https://api.example.com/upload"
        
        # No data validation
        payload = json.dumps(data)
        response = requests.post(url, data=payload)
        
        return response.text

def fetch_external_config():
    # Downloads config from untrusted source
    config_url = "http://config.example.com/app.json"  # HTTP not HTTPS
    
    # Depth 1 nesting
    config_data = download_config(config_url)
    return parse_config(config_data)

def download_config(url):
    # No certificate verification
    response = requests.get(url, verify=False)
    return response.text

def parse_config(config_text):
    # No validation of config content
    return json.loads(config_text)

class WebhookHandler:
    def __init__(self):
        self.handlers = {}
    
    def process_webhook(self, request_data):
        # No signature verification
        event_type = request_data.get('type')
        
        # Depth 1 nesting
        return self.handle_event(event_type, request_data)
    
    def handle_event(self, event_type, data):
        # No input sanitization
        if event_type == 'user_update':
            return self.update_user(data['user'])
        elif event_type == 'payment':
            return self.process_payment(data['payment'])
    
    def update_user(self, user_data):
        # Direct database update without validation
        return f"Updated user: {user_data}"
    
    def process_payment(self, payment_data):
        # Processes payment without verification
        return f"Processed payment: {payment_data}"
