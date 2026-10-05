class Repository:
    def __init__(self):
        pass
class Controller:
    def __init__(self, repo):
        self.repo = repo
        pass
class UI:
    def __init__(self, ctrl):
        self.ctrl = ctrl
        pass
    def start(self):
        pass
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