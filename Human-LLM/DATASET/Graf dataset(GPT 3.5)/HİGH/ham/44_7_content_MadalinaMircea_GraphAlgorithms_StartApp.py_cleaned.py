'''
Created on Mar 29, 2017
@author: Madalina
'''
from Repository import Repository
from Controller import Controller
from UI import UI
b1 = Repository()
b2 = Controller(b1)
b3 = UI(b2)
b3.start()