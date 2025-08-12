from controller.actions.IAction import IAction


class ExitAction(IAction):
    def __init__(self, controller):
        self.controller = controller
        self.key = "exit"

    def execute(self):
        self.controller.is_running = False
