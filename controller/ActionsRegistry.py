from controller.actions.RemovePassword import RemovePasswordAction
from controller.actions.GetServices import GetServicesAction
from controller.actions.Exit import ExitAction
from controller.actions.GetService import GetServiceAction
from controller.actions.DisplayPassword import DisplayPasswordAction
from controller.actions.DisplayPasswords import DisplayPasswordsAction
from controller.actions.AddPassword import AddPasswordAction
from controller.actions.ViewEncryptedPasswords import ViewEncryptedPasswords


class ActionsRegistry:
    def __init__(self, controller):
        self.controller = controller
        self.actions = [
            RemovePasswordAction(controller),
            GetServicesAction(controller),
            ExitAction(controller),
            GetServiceAction(controller),
            DisplayPasswordAction(controller),
            DisplayPasswordsAction(controller),
            AddPasswordAction(controller),
            ViewEncryptedPasswords(controller),
        ]
        self.actions_dict = self.create_actions_dict()

    def get_action(self, key):
        return self.actions_dict.get(key, None)

    def get_all_actions(self):
        return self.actions_dict.values()

    def get_action_keys(self):
        return sorted(self.actions_dict.keys())

    def get_action_by_key(self, key):
        return self.actions_dict.get(key, None)

    def execute_action(self, key):
        action = self.get_action(key)
        if action:
            action.execute()
        else:
            raise ValueError(f"Action with key '{key}' not found.")

    def create_actions_dict(self):
        return {action.key: action for action in self.actions}
