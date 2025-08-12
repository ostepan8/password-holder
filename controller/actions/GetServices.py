from controller.actions.IAction import IAction


class GetServicesAction(IAction):
    def __init__(self, controller):
        self.controller = controller
        self.key = "get_services"

    def execute(self):
        services = self.controller.model.get_services()
        if len(services) == 0:
            self.controller.view.display_message("No services found.")

        for service in services:
            self.controller.view.display_service(service)
