class Controller:
    def hamiltonian(self):
        pass
class UI:
    def __init__(self, ctrl):
        self._ctrl = ctrl
    def start(self):
        stack = self._ctrl.hamiltonian()
        if stack is False:
            print("There are no Hamiltonian cycles.")
        else:
            print("Hamiltonian cycle found:", stack)
if __name__ == "__main__":
    controller = Controller()
    ui = UI(controller)
    ui.start()