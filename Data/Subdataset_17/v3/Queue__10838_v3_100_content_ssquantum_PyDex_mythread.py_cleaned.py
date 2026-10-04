
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QApplication
import sys
import time
def reset_slot(signal, slot, reconnect=True):
    while True:
        try:
            signal.disconnect(slot)
        except TypeError:
            break
    if reconnect:
        signal.connect(slot)
class PyDexThread(QThread):
    def __init__(self):
        super().__init__()
        self.stop = False
        self.queue = []
        self.app = QApplication.instance()
    @pyqtSlot(object)
    def add_item(self, new_item):
        self.queue.append(new_item)
    def process(self, item):
        raise NotImplementedError("Subclasses should implement this method")
    def run(self):
        while not self.check_stop():
            self.app.processEvents()
            if self.queue:
                self.process(self.queue.pop(0))
    def check_stop(self):
        return self.stop
    def reset_stop(self):
        self.stop = False
    def close(self):
        reset_slot(self.finished, self.reset_stop)
        self.stop = True
class ExampleThread(PyDexThread):
    def process(self, item):
        print(f"Processing item: {item}")
def main():
    app = QApplication(sys.argv)
    thread = ExampleThread()
    thread.start()
    thread.add_item("Item 1")
    thread.add_item("Item 2")
    time.sleep(5)
    thread.close()
    thread.wait()
    print("Thread stopped.")
if __name__ == "__main__":
    main()