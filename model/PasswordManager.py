from model.Encrypter import Encrypter
import os
import getpass


class PasswordManager:
    def __init__(self, database):
        self.database = database
        if self.database:
            self.load_passwords()
        self.passwords = {}
        self.encryption_key = os.environ.get("ENCRYPTION_KEY")
        if not self.encryption_key:
            self.encryption_key = getpass.getpass("Enter encryption key: ")
        if not self.encryption_key:
            raise RuntimeError("ENCRYPTION_KEY not set")
        self.encrypter = Encrypter(self.encryption_key)

    def load_passwords(self):
        self.database.connect()
        self.passwords = self.database.get_service_to_password_dict()
        self.database.disconnect()

    def add_password(self, service, password):
        self.database.add_password(service, self.encrypter.encrypt(password))
        self.passwords[service] = self.encrypter.encrypt(password)

    def get_password(self, service):
        encrypted_password = self.passwords.get(service, None)
        if encrypted_password:
            return self.encrypter.decrypt(encrypted_password)
        return None

    def remove_password(self, service):
        self.database.remove_password(service)
        self.passwords.pop(service, None)

    def get_passwords(self):
        return {
            service: self.encrypter.decrypt(password)
            for service, password in self.passwords.items()
        }

    def get_services(self):
        return list(self.passwords.keys())

    def get_service(self, service):
        for s in self.passwords.keys():
            if service == s:
                return s
        return None
