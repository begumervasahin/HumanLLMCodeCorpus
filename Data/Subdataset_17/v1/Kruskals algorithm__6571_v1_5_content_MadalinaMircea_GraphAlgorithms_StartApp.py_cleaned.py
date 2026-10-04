
from Repository import Repository
from Controller import Controller
from UI import UI
repo = Repository()
ctrl = Controller(repo)
ui = UI(ctrl)
ui.start()