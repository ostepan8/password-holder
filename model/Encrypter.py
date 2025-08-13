from cryptography.fernet import Fernet
import base64
import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes


class Encrypter:
    def __init__(self, key, salt_file="salt.bin"):
        self.password = key
        self.salt_file = salt_file

        if os.path.exists(self.salt_file):
            with open(self.salt_file, "rb") as f:
                salt = f.read()
        else:
            salt = os.urandom(16)
            with open(self.salt_file, "wb") as f:
                f.write(salt)

        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        self.key = base64.urlsafe_b64encode(kdf.derive(self.password.encode()))
        self.cipher = Fernet(self.key)

    def encrypt(self, data):
        # Convert data to bytes if it's a string
        if isinstance(data, str):
            data = data.encode()
        # Encrypt the data
        encrypted_data = self.cipher.encrypt(data)
        return encrypted_data

    def decrypt(self, data):
        with open(self.salt_file, "rb") as f:
            salt = f.read()
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(self.password.encode()))
        cipher = Fernet(key)
        decrypted_data = cipher.decrypt(data)
        try:
            return decrypted_data.decode()
        except UnicodeDecodeError:
            return decrypted_data
