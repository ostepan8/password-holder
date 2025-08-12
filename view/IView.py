class IView:
    def __init__(self, model):
        self.model = model

    def display_password(self, service):
        raise NotImplementedError("This method should be implemented in a subclass")

    def display_all_passwords(self):
        raise NotImplementedError("This method should be implemented in a subclass")
