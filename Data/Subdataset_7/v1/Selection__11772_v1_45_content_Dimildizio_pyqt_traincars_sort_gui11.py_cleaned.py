from PyQt4 import QtGui, QtCore
import sys
import os
from cars_coal import *
class class1(QtGui.QMainWindow):
    def fonk1(self):
        super().fonk25()
        self.b1 = {'Show': [self.go_train, 'Show the whole b17'],
                        'Cars': [self.go_cars, 'Manipulate cars'],
                        'Arrange': [self.go_sort, 'Sort cars in order'],
                        'Destroy': [self.boom, 'Boom!'],
                        'Exit': [self.close_me, 'Close the application']}
        self.b2 = 'Train'
        self.setWindowIcon(QtGui.QIcon('pics\\bullet_train.ico'))
        self.b3 = 'pics\\trainsteam.jpg'
        self.setGeometry(500, 150, 260, 450)
        self.setWindowTitle('Trains')
        self.setMaximumSize(300, 450)
        self.b4 = QtGui.QApplication.setStyle(QtGui.QStyleFactory.create('Plastique'))
        self.statusBar()
        b5 = QtGui.QAction('&Exit me', self)
        b5.setShortcut('Ctrl+Q')
        b5.setStatusTip('Leave the App')
        b5.triggered.connect(self.close_me)
        b6 = self.menuBar()
        b7 = b6.addMenu('&File')
        b7.addAction(b5)
        b7.addSeparator()
        self.fonk26()
    def fonk2(self):
        b8 = QtGui.QVBoxLayout()
        b9 = QtGui.QLabel(self.b2)
        b10 = QtGui.QFont('Times', 14)
        b10.setBold(1)
        b9.setFont(b10)
        b9.setAlignment(QtCore.Qt.AlignCenter)
        b8.addWidget(b9)
        b11 = QtGui.QLabel()
        b11.setMinimumSize(QtCore.QSize(100, 50))
        b11.setSizeIncrement(QtCore.QSize(1, 1))
        b11.setBaseSize(QtCore.QSize(300, 200))
        b11.setPixmap(QtGui.QPixmap(self.b3))
        b11.setScaledContents(True)
        b8.addWidget(b11)
        for key, value in self.b1.b23():
            b12 = QtGui.QPushButton(key)
            b12.clicked.connect(value[0])
            b12.setStatusTip(value[1])
            b8.addWidget(b12)
        b13 = QtGui.QWidget()
        b13.setLayout(b8)
        self.setCentralWidget(b13)
        self.show()
    def fonk3(self):
        self.close()
        self.b14 = class4()
    def fonk4(self):
        self.close()
        self.b14 = class6()
    def fonk5(self):
        self.close()
        self.b14 = class1()
    def fonk6(self):
        self.close()
        self.b14 = class3()
    def fonk7(self):
        self.close()
        self.b14 = class2()
    def fonk8(self, icon, title, b25):
        b15 = QtGui.QMessageBox(icon, title, b25, b1=QtGui.QMessageBox.Ok)
        return b15.exec_()
    def fonk9(self):
        b15 = QtGui.QMessageBox()
        b15.setText('Are you sure you want to exit?')
        b15.setWindowTitle('Exit')
        b15.setIcon(QtGui.QMessageBox.Information)
        b15.addButton(QtGui.QPushButton('Yes'), QtGui.QMessageBox.YesRole)
        b15.addButton(QtGui.QPushButton('No'), QtGui.QMessageBox.NoRole)
        b16 = b15.exec_()
        if not b16:
            sys.exit()
    def fonk10(self):
        self.fonk8(QtGui.QMessageBox.Information, 'Boom!', 'Your b17 has been destroyed')
        Depot.b17 = False
        self.fonk7()
class class2(class1):
    def fonk11(self):
        super().fonk25()
        self.b1 = {'Generate': [self.get_train, 'Generate a b17'],
                        'Exit': [self.close_me, 'Close the application']}
        self.b2 = 'Welcome to the b17 manager!\nDo you wish to create a b17?'
        self.b3 = 'pics\\facttrain.jpg'
        self.fonk26()
    def fonk12(self):
        num, b18 = QtGui.QInputDialog.getInt(self, 'Generating b17', 'How many cars?')
        if b18:
            if num > 5000:
                self.fonk8(QtGui.QMessageBox.Warning, 'You\'ve been rejected', "You've requested too many cars")
            elif num < 1:
                self.fonk8(QtGui.QMessageBox.Warning, 'You\'ve been rejected', "There is no point for you in b17 without cars")
            else:
                Depot.generate(num)
                self.fonk5()
class class3(class1):
    def fonk13(self, b17 = False):
        super().fonk25()
        self.setGeometry(500, 150, 300, 450)
        self.b3 = 'pics\\Aurora610.jpg'
        self.b2 = 'Arrange the cars'
        b15 = QtGui.QMessageBox()
        b15.setText('              Sort b19?')
        b15.setWindowTitle('Sorting')
        b15.addButton(QtGui.QPushButton('From left to right'), QtGui.QMessageBox.YesRole)
        b15.addButton(QtGui.QPushButton('From right to left'), QtGui.QMessageBox.NoRole)
        self.b19 = b15.exec_()
        b20 = QtGui.QMessageBox()
        b20.setText('              Sort parameter?')
        b20.setWindowTitle('Sorting')
        b20.addButton(QtGui.QPushButton('Serial number'), QtGui.QMessageBox.YesRole)
        b20.addButton(QtGui.QPushButton('Quantity of coal'), QtGui.QMessageBox.NoRole)
        self.b21 = b20.exec_()
        self.b1 = {'Home': [self.go_home, 'Go to the main page'],
                        'Bubble sort': [self.call_bubble, 'Bubble sorting algorithm'],
                        'Selection sort': [self.call_selection, 'Selection sorting algorithm'],
                        'Insertion sort': [self.call_insertion, 'Insertion sorting algorithm'],
                        'Exit': [self.close_me, 'Close the application']}
        self.fonk26()
    @property
    def fonk14(self):
        self.fonk8(QtGui.QMessageBox.Information, 'Sorted completed', 'Cars have been arranged in order')
    def fonk15(self):
        self.i_msg
        if self.b19:
            return Depot.b17.select_sort_to_left(self.b21)
        return Depot.b17.select_sort_to_right(self.b21)
    def fonk16(self):
        self.i_msg
        if self.b19:
            return Depot.b17.bubble_sort_to_left(self.b21)
        return Depot.b17.bubble_sort_to_right(self.b21)
    def fonk17(self):
        self.i_msg
        if self.b19:
            return Depot.b17.insertion_sort_to_left(self.b21)
        return Depot.b17.insertion_sort_to_right(self.b21)
class class4(class1):
    def fonk18(self, b17 = False):
        super().fonk25()
        self.b3 = 'pics\\steam_train.jpg'
        self.b2 = 'Cars'
        self.b1 = {'Home': [self.go_home, 'Go to the main page'],
                        'Add a b22': [self.add_car, 'Add more cars'],
                        'Find a b22': [self.find_car, 'Search for a b22'],
                        'Remove a b22': [self.remove_car, 'Delete a b22'],
                        'Exit': [self.close_me, 'Close the application']}
        self.fonk26()
    def fonk19(self):
        b22 = self.fonk20()
        if b22:
            self.close()
            self.b14 = class5(b22)
    def fonk20(self):
        b23 = ('serial', 'coal', 'index')
        item, b18 = QtGui.QInputDialog.getItem(self, 'Find a b22', 'Find by', b23, 0, False)
        if b18:
            num, b18 = QtGui.QInputDialog.getInt(self, 'Finding', 'Input a digit')
            b22 = Depot.b17.find_by_type(num, item)
            if b22:
                return b22
            else:
                self.fonk8(QtGui.QMessageBox.Information, 'Ooops', 'Car not found')
    def fonk21(self):
        b24 = self.fonk20()
        if b24:
            b25 = f'Car {b24.serial} disconnected from the b17'
            Depot.b17.cars.remove(b24)
            self.fonk8(QtGui.QMessageBox.Information, 'Car removed', b25)
        if len(Depot.b17.cars) < 1:
            self.fonk8(QtGui.QMessageBox.Critical, 'Train confiscated',
                           'You don\'t have any cars left\nYour tain has been confiscated')
            self.fonk7()
            return
    def fonk22(self):
        b23 = ('serial number', 'coal')
        item, b18 = QtGui.QInputDialog.getItem(self, 'Connecting a b22', 'Add by', b23, 0, False)
        if b18:
            num, b26 = QtGui.QInputDialog.getInt(self, 'Connecting a b22', 'Input a digit')
            if b26:
                b22 = Depot.b17.fonk22(item, num)
                b25 = f'Car {b22.serial} with {b22.coal} coal connected to the b17'
                self.fonk8(QtGui.QMessageBox.Information, 'Car added', b25)
class class5(class1):
    def fonk23(self, b22 = True):
        self.b22 = b22
        super().fonk25()
        self.setGeometry(500, 150, 200, 400)
        self.b3 = 'pics\\steamtrain.jpg'
        self.b1 = {'Home': [self.go_home, 'Go to the main page']}
        self.fonk26()
    def fonk24(self):
        b8 = QtGui.QVBoxLayout()
        b9 = QtGui.QLabel('Search result')
        b10 = QtGui.QFont('Times', 14)
        b10.setBold(1)
        b9.setFont(b10)
        b9.setAlignment(QtCore.Qt.AlignCenter)
        b8.addWidget(b9)
        b11 = QtGui.QLabel()
        b11.setMinimumSize(QtCore.QSize(100, 50))
        b11.setSizeIncrement(QtCore.QSize(1, 1))
        b11.setBaseSize(QtCore.QSize(200, 50))
        b11.setPixmap(QtGui.QPixmap(self.b3))
        b11.setScaledContents(True)
        b8.addWidget(b11)
        b27 = QtGui.QLabel(str(self.b22))
        b10 = QtGui.QFont('Times', 12)
        b27.setFont(b10)
        b27.setAlignment(QtCore.Qt.AlignCenter)
        b8.addWidget(b27)
        for key, value in self.b1.b23():
            b12 = QtGui.QPushButton(key)
            b12.clicked.connect(value[0])
            b12.setStatusTip(value[1])
            b8.addWidget(b12)
        b13 = QtGui.QWidget()
        b13.setLayout(b8)
        self.setCentralWidget(b13)
        self.show()
class class6(class5):
    def fonk25(self, b22 = True):
        super().fonk25()
        self.b3 = 'pics\\chocho.jpg'
        self.b2 = 'This is your b17'
        self.setGeometry(500, 150, 250, 200)
        self.b22 = b22
        self.fonk26()
    def fonk26(self):
        b8 = QtGui.QVBoxLayout()
        b9 = QtGui.QLabel(self.b2)
        b10 = QtGui.QFont('Times', 14)
        b10.setBold(1)
        b9.setFont(b10)
        b9.setAlignment(QtCore.Qt.AlignCenter)
        b8.addWidget(b9)
        b11 = QtGui.QLabel()
        b11.setMinimumSize(QtCore.QSize(100, 50))
        b11.setSizeIncrement(QtCore.QSize(1, 1))
        b11.setBaseSize(QtCore.QSize(200, 50))
        b11.setPixmap(QtGui.QPixmap(self.b3))
        b11.setScaledContents(True)
        b8.addWidget(b11)
        b28 = QtGui.QTextEdit()
        b28.setText(str(Depot.b17))
        b28.setReadOnly(True)
        b28.setMinimumSize(QtCore.QSize(100, 200))
        b8.addWidget(b28)
        for key, value in self.b1.b23():
            b12 = QtGui.QPushButton(key)
            b12.clicked.connect(value[0])
            b12.setStatusTip(value[1])
            b8.addWidget(b12)
        b13 = QtGui.QWidget()
        b13.setLayout(b8)
        self.setCentralWidget(b13)
        self.show()
if b29 = = '__main__':
    b30 = QtGui.QApplication(sys.argv)
    b14 = class2()
    sys.exit(b30.exec())