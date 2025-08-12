from model.PasswordManager import PasswordManager


class Model:
    def __init__(self, database):
        self.password_manager = PasswordManager(database)

    def add_password(self, service, password):
        self.password_manager.add_password(service, password)

    def get_password(self, service):
        return self.password_manager.get_password(service)

    def remove_password(self, service):
        self.password_manager.remove_password(service)

    def get_passwords(self):
        return self.password_manager.get_passwords()

    def get_services(self):
        return self.password_manager.get_services()

    def get_service(self, service):
        return self.password_manager.get_service(service)

    def view_encrypted_passwords(self):
        return self.password_manager.passwords
