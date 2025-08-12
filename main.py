from model.Model import Model
from view.TextualView import TextualView
from controller.Controller import Controller
from model.PasswordDatabase import PasswordDatabase


def main():
    database = PasswordDatabase("passwords.db")
    model = Model(database)
    view = TextualView(model)
    controller = Controller(model, view)
    controller.run()


if __name__ == "__main__":
    main()
