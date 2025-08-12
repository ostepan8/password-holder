from controller.actions.IAction import IAction


class DisplayPasswordsAction(IAction):
    def __init__(self, controller):
        self.controller = controller
        self.key = "view_passwords"

    def execute(self):
        services = self.controller.model.get_services()
        if len(services) == 0:
            self.controller.view.display_message("No services found.")
        for service in services:
            self.controller.view.display_service(service)
