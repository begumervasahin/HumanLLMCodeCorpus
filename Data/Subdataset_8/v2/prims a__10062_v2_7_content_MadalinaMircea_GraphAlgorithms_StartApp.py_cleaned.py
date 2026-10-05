
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
from Repository import Repository
from Controller import Controller
from UI import UI
def main():
    repo = Repository()
    ctrl = Controller(repo)
    ui = UI(ctrl)
    ui.start()
if __name__ == "__main__":
    main()