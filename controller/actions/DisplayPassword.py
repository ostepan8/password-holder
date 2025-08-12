from controller.actions.IAction import IAction


class DisplayPasswordAction(IAction):
    def __init__(self, controller):
        self.controller = controller
        self.key = "show_password"

    def execute(self):
        services = self.controller.model.get_services()
        if len(services) == 0:
            self.controller.view.display_message("No services found.")
            return
        for service in services:
            self.controller.view.display_service(service)
        print("." * 20)
        service = input("Enter service name: ")
        if not service:
            raise ValueError("Service name cannot be empty.")
        self.controller.view.display_service(service)
