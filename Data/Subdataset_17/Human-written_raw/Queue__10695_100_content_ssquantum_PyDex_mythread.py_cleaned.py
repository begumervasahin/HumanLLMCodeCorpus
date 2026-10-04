
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QApplication
enco = 'mbcs'
def reset_slot(signal, slot, reconnect=True):
    while True:
        try: signal.disconnect(slot)
        except TypeError: break
    if reconnect: signal.connect(slot)
class PyDexThread(QThread):
    stop  = False
    queue = []
    def __init__(self):
        super().__init__()
        self.app = QApplication.instance()
    @pyqtSlot(object)
    def add_item(self, new_item, *args, **kwargs):
        self.queue.append(new_item)
    def process(self, item, *args, **kwargs):
        raise NotImplementedError
    def run(self, *args, **kwargs):
        while True:
            self.app.processEvents()
            if self.check_stop():
                break
            elif len(self.queue):
                self.process(self.queue.pop(0), *args, **kwargs)
    def check_stop(self):
        return self.stop
    def reset_stop(self):
        self.stop = False
    def close(self):
        reset_slot(self.finished, self.reset_stop)
        self.stop = True