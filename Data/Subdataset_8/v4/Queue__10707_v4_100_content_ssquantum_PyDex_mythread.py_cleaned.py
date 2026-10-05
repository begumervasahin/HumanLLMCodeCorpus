from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QApplication
DEFAULT_ENCODING = 'mbcs'
class PyDexThread(QThread):
    stop_signal = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.app = QApplication.instance()
        self.queue = []
    @pyqtSlot(object)
    def add_item(self, new_item, *args, **kwargs):
        self.queue.append(new_item)
    def process(self, item, *args, **kwargs):
        raise NotImplementedError
    def run(self, *args, **kwargs):
        while True:
            self.app.processEvents()
            if self.should_stop():
                break
            elif self.queue:
                self.process(self.queue.pop(0), *args, **kwargs)
    def should_stop(self):
        return self.stop_signal
    def reset_stop(self):
        self.stop_signal = False
    def close(self):
        self.stop_signal.emit()
        self.stop_signal.connect(self.reset_stop)
def reset_slot(signal, slot, reconnect=True):
    while True:
        try:
            signal.disconnect(slot)
        except TypeError:
            break
    if reconnect:
        signal.connect(slot)