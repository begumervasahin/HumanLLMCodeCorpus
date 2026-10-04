
from Repository import Repository
from Controller import Controller
from UI import UI
def main():
    repository = Repository()
    controller = Controller(repository)
    user_interface = UI(controller)
    user_interface.start()
if __name__ == "__main__":
    main()