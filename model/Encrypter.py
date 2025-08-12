from cryptography.fernet import Fernet
import base64
import hashlib


class Encrypter:
    def __init__(self, key):
        # Generate a Fernet key from the provided password/key
        key_bytes = key.encode()
        key_hash = hashlib.sha256(key_bytes).digest()
        # Fernet requires a 32-byte key encoded in base64
        self.key = base64.urlsafe_b64encode(key_hash)
        self.cipher = Fernet(self.key)

    def encrypt(self, data):
        # Convert data to bytes if it's a string
        if isinstance(data, str):
            data = data.encode()
        # Encrypt the data
        encrypted_data = self.cipher.encrypt(data)
        return encrypted_data

    def decrypt(self, data):
        # Decrypt the data
        decrypted_data = self.cipher.decrypt(data)
        # Try to decode to string if possible
        try:
            return decrypted_data.decode()
        except UnicodeDecodeError:
            return decrypted_data
