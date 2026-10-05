
from Repository import Repository
from Controller import Controller
from UI import UI
def main():
    data_repository = Repository()
    data_controller = Controller(data_repository)
    user_interface = UI(data_controller)
    user_interface.start()
if __name__ == "__main__":
    main()