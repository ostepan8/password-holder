from controller.actions.IAction import IAction


class GetServiceAction(IAction):
    def __init__(self, controller):
        self.controller = controller
        self.key = "get_service"

    def execute(
        self,
    ):
        services = self.controller.model.get_services()
        if len(services) == 0:
            self.controller.view.display_message("No services found.")
            return
        for service in services:
            self.controller.view.display_service(service)
        service = input("Enter service name: ")
        service_data = self.controller.model.get_service(service)
        if service_data is None:
            raise ValueError(f"Service '{service}' does not exist.")

        self.controller.view.display_service(service_data)
