
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