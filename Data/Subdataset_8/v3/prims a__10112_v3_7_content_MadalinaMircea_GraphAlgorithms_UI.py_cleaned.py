class Controller:
    def find_hamiltonian_cycle(self):
        pass
class UI:
    def __init__(self, controller):
        self.controller = controller
    def start(self):
        stack = self.controller.find_hamiltonian_cycle()
        if stack is False:
            print("No Hamiltonian cycles found.")
        else:
            print("Hamiltonian cycle found:", stack)
if __name__ == "__main__":
    controller = Controller()
    ui = UI(controller)
    ui.start()