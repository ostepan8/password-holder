import getpass
from controller.actions.IAction import IAction


class AddPasswordAction(IAction):
    def __init__(self, controller):
        self.controller = controller
        self.key = "add_password"

    def execute(self):
        service = input("Enter service name: ")
        password = getpass.getpass("Enter password: ")
        self.controller.model.add_password(service, password)
        self.controller.view.display_message(f"Password for {service} added.")
