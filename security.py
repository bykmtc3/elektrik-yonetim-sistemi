from cryptography.fernet import Fernet
import hashlib
import os
from config import Config
from datetime import datetime

class SecurityManager:
    def __init__(self):
        self.key = self._get_or_create_key()
        self.cipher = Fernet(self.key)
        self.admin_password = Config.ADMIN_PASSWORD
    
    def _get_or_create_key(self):
        key_file = "./data/.key"
        os.makedirs("./data", exist_ok=True)
        
        if os.path.exists(key_file):
            with open(key_file, 'rb') as f:
                return f.read()
        else:
            key = Fernet.generate_key()
            with open(key_file, 'wb') as f:
                f.write(key)
            return key
    
    def encrypt_data(self, data):
        """Encrypt sensitive data"""
        if isinstance(data, str):
            data = data.encode()
        return self.cipher.encrypt(data).decode()
    
    def decrypt_data(self, encrypted_data):
        """Decrypt sensitive data"""
        if isinstance(encrypted_data, str):
            encrypted_data = encrypted_data.encode()
        return self.cipher.decrypt(encrypted_data).decode()
    
    def hash_password(self, password):
        """Hash password with salt"""
        salt = os.urandom(32)
        pwd_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
        return (salt + pwd_hash).hex()
    
    def verify_password(self, password, hashed):
        """Verify password"""
        salt = bytes.fromhex(hashed[:64])
        pwd_hash = bytes.fromhex(hashed[64:])
        new_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
        return new_hash == pwd_hash
    
    def verify_admin(self, password=None):
        """Verify admin access"""
        if password is None:
            return True
        return password == self.admin_password
    
    def generate_token(self, user_id):
        """Generate access token"""
        import jwt
        payload = {
            'user_id': user_id,
            'timestamp': datetime.now().isoformat()
        }
        return jwt.encode(payload, Config.SECRET_KEY, algorithm='HS256')
