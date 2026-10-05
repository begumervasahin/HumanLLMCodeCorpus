class Repository:
    def __init__(self):
        pass
class Controller:
    def __init__(self, repository):
        self.repository = repository
        pass
class UI:
    def __init__(self, controller):
        self.controller = controller
        pass
    def start(self):
        pass
def main():
    repository = Repository()
    controller = Controller(repository)
    user_interface = UI(controller)
    user_interface.start()
if __name__ == "__main__":
    main()