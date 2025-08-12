from controller.actions.RemovePassword import RemovePasswordAction
from controller.actions.GetServices import GetServicesAction
from controller.actions.Exit import ExitAction
from controller.actions.GetService import GetServiceAction
from controller.actions.DisplayPassword import DisplayPasswordAction
from controller.actions.DisplayPasswords import DisplayPasswordsAction
from controller.actions.AddPassword import AddPasswordAction
from controller.actions.ViewEncryptedPasswords import ViewEncryptedPasswords
from controller.ActionsRegistry import ActionsRegistry


class Controller:

    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.is_running = True
        self.actions_registry = ActionsRegistry(self)

    def run(self):
        self.view.display_welcome_message(self.actions_registry.get_action_keys())

        while self.is_running:
            choice = input("Choose an option: ")
            self.actions_registry.execute_action(choice)
