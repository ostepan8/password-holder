class ViewEncryptedPasswords:
    def __init__(self, controller):
        self.controller = controller
        self.key = "view_encrypted_passwords"

    def execute(self):
        encrypted_passwords = self.controller.model.view_encrypted_passwords()
        self.controller.view.display_encrypted_passwords(encrypted_passwords)
