from controller.actions.IAction import IAction


class RemovePasswordAction(IAction):
    def __init__(self, controller):
        self.controller = controller
        self.key = "remove_password"

    def execute(self, service):
        if not service:
            raise ValueError("Service name cannot be empty.")

        if self.controller.get_service(service) is None:
            raise ValueError(f"Service '{service}' does not exist.")

        self.controller.model.remove_password(service)
