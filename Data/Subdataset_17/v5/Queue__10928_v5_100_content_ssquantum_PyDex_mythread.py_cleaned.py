
from PyQt5.QtCore import QThread, pyqtSlot
from PyQt5.QtWidgets import QApplication
enco = 'mbcs'
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
        self.app = QApplication.instance()
        self.stop_flag = False
        self.queue = []
    @pyqtSlot(object)
    def add_item(self, new_item):
        self.queue.append(new_item)
    def process(self, item):
        raise NotImplementedError("The process method should be overridden in subclasses.")
    def run(self):
        while not self.stop_flag:
            self.app.processEvents()
            if self.queue:
                item = self.queue.pop(0)
                self.process(item)
    def check_stop(self):
        return self.stop_flag
    def reset_stop(self):
        self.stop_flag = False
    def close(self):
        reset_slot(self.finished, self.reset_stop)
        self.stop_flag = True