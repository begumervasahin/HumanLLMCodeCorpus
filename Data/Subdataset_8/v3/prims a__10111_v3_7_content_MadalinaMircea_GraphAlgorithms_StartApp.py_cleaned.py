
class Repository:
    def __init__(self):
        pass
class Controller:
    def __init__(self, repository):
        self.repository = repository
class UI:
    def __init__(self, controller):
        self.controller = controller
    def start(self):
        print("UI started...")
from repository import Repository
from controller import Controller
from ui import UI
def main():
    repository = Repository()
    controller = Controller(repository)
    user_interface = UI(controller)
    user_interface.start()
if __name__ == "__main__":
    main()