class TextualView:
    def __init__(self, model):
        self.model = model

    def display_password(self, service):
        password = self.model.get_password(service)
        if password:
            print(f"Password for {service}: {password}")
        else:
            print(f"No password found for {service}")

    def display_all_passwords(self):
        passwords = self.model.get_passwords()
        if passwords:
            for service, password in passwords.items():
                print(f"{service}: {password}")
        else:
            print("No passwords stored.")

    def display_service(self, service):
        if self.model.get_service(service):
            print(f"Service: {service} exists.")
        else:
            print(f"Service: {service} does not exist.")

    def display_welcome_message(self, actions):
        print("\nWelcome to the Password Manager")
        print("Available actions:")
        for action in actions:
            print(f"- {action}")
        print("Please choose an action by typing its name.")

    def display_message(self, message):
        print(message)

    def display_encrypted_passwords(self, encrypted_passwords):
        if encrypted_passwords:
            for service, enc_password in encrypted_passwords.items():
                print(f"{service}: {enc_password}")
        else:
            print("No encrypted passwords stored.")
