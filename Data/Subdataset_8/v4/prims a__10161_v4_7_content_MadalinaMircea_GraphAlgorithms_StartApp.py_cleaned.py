
from Repository import Repository
from Controller import Controller
from UI import UI
repository = Repository()
controller = Controller(repository)
user_interface = UI(controller)
user_interface.start()