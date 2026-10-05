import sys
from PyQt4 import QtGui, QtCore
from cars_coal import *
class class1(QtGui.QMainWindow):
    def fonk1(self):
        super().fonk28()
        self.b1 = {
            'Show': [self.go_train, 'Show the whole b17'],
            'Cars': [self.go_cars, 'Manipulate cars'],
            'Arrange': [self.go_sort, 'Sort cars in order'],
            'Destroy': [self.boom, 'Boom!'],
            'Exit': [self.close_me, 'Close the application']
        }
        self.b2 = 'Train'
        self.setWindowIcon(QtGui.QIcon('pics\\bullet_train.ico'))
        self.b3 = 'pics\\trainsteam.jpg'
        self.setGeometry(500, 150, 260, 450)
        self.setWindowTitle('Trains')
        self.setMaximumSize(300, 450)
        self.b4 = QtGui.QApplication.setStyle(QtGui.QStyleFactory.create('Plastique'))
        self.statusBar()
        self.fonk2()
    def fonk2(self):
        b5 = QtGui.QAction('&Exit me', self)
        b5.setShortcut('Ctrl+Q')
        b5.setStatusTip('Leave the App')
        b5.triggered.connect(self.close_me)
        b6 = self.menuBar()
        b7 = b6.addMenu('&File')
        b7.addAction(b5)
        b7.addSeparator()
    def fonk3(self):
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
        for key, value in self.b1.b22():
            b12 = QtGui.QPushButton(key)
            b12.clicked.connect(value[0])
            b12.setStatusTip(value[1])
            b8.addWidget(b12)
        b13 = QtGui.QWidget()
        b13.setLayout(b8)
        self.setCentralWidget(b13)
        self.show()
    def fonk4(self):
        self.close()
        self.b14 = class4()
    def fonk5(self):
        self.close()
        self.b14 = class6()
    def fonk6(self):
        self.close()
        self.b14 = class1()
    def fonk7(self):
        self.close()
        self.b14 = class3()
    def fonk8(self):
        self.close()
        self.b14 = class2()
    def fonk9(self, icon, title, b24):
        b15 = QtGui.QMessageBox(icon, title, b24, b1=QtGui.QMessageBox.Ok)
        return b15.exec_()
    def fonk10(self):
        b15 = QtGui.QMessageBox()
        b15.setText('Are you sure you want to exit?')
        b15.setWindowTitle('Exit')
        b15.setIcon(QtGui.QMessageBox.Information)
        b15.addButton(QtGui.QPushButton('Yes'), QtGui.QMessageBox.YesRole)
        b15.addButton(QtGui.QPushButton('No'), QtGui.QMessageBox.NoRole)
        b16 = b15.exec_()
        if not b16:
            sys.exit()
    def fonk11(self):
        self.fonk9(QtGui.QMessageBox.Information, 'Boom!', 'Your b17 has been destroyed')
        Depot.b17 = False
        self.fonk8()
class class2(class1):
    def fonk12(self):
        super().fonk28()
        self.b1 = {
            'Generate': [self.get_train, 'Generate a b17'],
            'Exit': [self.close_me, 'Close the application']
        }
        self.b2 = 'Welcome to the b17 manager!\nDo you wish to create a b17?'
        self.b3 = 'pics\\facttrain.jpg'
        self.fonk29()
    def fonk13(self):
        num, b18 = QtGui.QInputDialog.getInt(self, 'Generating b17', 'How many cars?')
        if b18:
            if num > 5000:
                self.fonk9(QtGui.QMessageBox.Warning, 'You\'ve been rejected', "You've requested too many cars")
            elif num < 1:
                self.fonk9(QtGui.QMessageBox.Warning, 'You\'ve been rejected', "There is no point for you in b17 without cars")
            else:
                Depot.generate(num)
                self.fonk6()
class class3(class1):
    def fonk14(self, b17 = False):
        super().fonk28()
        self.setGeometry(500, 150, 300, 450)
        self.b3 = 'pics\\Aurora610.jpg'
        self.b2 = 'Arrange the cars'
        self.b19 = self.fonk15()
        self.b20 = self.fonk16()
        self.b1 = {
            'Home': [self.go_home, 'Go to the main page'],
            'Bubble sort': [self.call_bubble, 'Bubble sorting algorithm'],
            'Selection sort': [self.call_selection, 'Selection sorting algorithm'],
            'Insertion sort': [self.call_insertion, 'Insertion sorting algorithm'],
            'Exit': [self.close_me, 'Close the application']
        }
        self.fonk29()
    def fonk15(self):
        b15 = QtGui.QMessageBox()
        b15.setText('              Sort b19?')
        b15.setWindowTitle('Sorting')
        b15.addButton(QtGui.QPushButton('From left to right'), QtGui.QMessageBox.YesRole)
        b15.addButton(QtGui.QPushButton('From right to left'), QtGui.QMessageBox.NoRole)
        return b15.exec_()
    def fonk16(self):
        b15 = QtGui.QMessageBox()
        b15.setText('              Sort parameter?')
        b15.setWindowTitle('Sorting')
        b15.addButton(QtGui.QPushButton('Serial number'), QtGui.QMessageBox.YesRole)
        b15.addButton(QtGui.QPushButton('Quantity of coal'), QtGui.QMessageBox.NoRole)
        return b15.exec_()
    def fonk17(self):
        return self.fonk9(QtGui.QMessageBox.Information, 'Sorted completed', 'Cars have been arranged in order')
    def fonk18(self):
        self.fonk17()
        if self.b19:
            return Depot.b17.select_sort_to_left(self.b20)
        return Depot.b17.select_sort_to_right(self.b20)
    def fonk19(self):
        self.fonk17()
        if self.b19:
            return Depot.b17.bubble_sort_to_left(self.b20)
        return Depot.b17.bubble_sort_to_right(self.b20)
    def fonk20(self):
        self.fonk17()
        if self.b19:
            return Depot.b17.insertion_sort_to_left(self.b20)
        return Depot.b17.insertion_sort_to_right(self.b20)
class class4(class1):
    def fonk21(self, b17 = False):
        super().fonk28()
        self.b3 = 'pics\\steam_train.jpg'
        self.b2 = 'Cars'
        self.b1 = {
            'Home': [self.go_home, 'Go to the main page'],
            'Add a b21': [self.add_car, 'Add more cars'],
            'Find a b21': [self.find_car, 'Search for a b21'],
            'Remove a b21': [self.remove_car, 'Delete a b21'],
            'Exit': [self.close_me, 'Close the application']
        }
        self.fonk29()
    def fonk22(self):
        b21 = self.fonk23()
        if b21:
            self.close()
            self.b14 = class5(b21)
    def fonk23(self):
        b22 = ('serial', 'coal', 'index')
        item, b18 = QtGui.QInputDialog.getItem(self, 'Find a b21', 'Find by', b22, 0, False)
        if b18:
            num, b18 = QtGui.QInputDialog.getInt(self, 'Finding', 'Input a digit')
            b21 = Depot.b17.find_by_type(num, item)
            if b21:
                return b21
            else:
                self.fonk9(QtGui.QMessageBox.Information, 'Ooops', 'Car not found')
    def fonk24(self):
        b23 = self.fonk23()
        if b23:
            b24 = f'Car {b23.serial} disconnected from the b17'
            Depot.b17.cars.remove(b23)
            self.fonk9(QtGui.QMessageBox.Information, 'Car removed', b24)
        if len(Depot.b17.cars) < 1:
            self.fonk9(QtGui.QMessageBox.Critical, 'Train confiscated',
                           'You don\'t have any cars left\nYour tain has been confiscated')
            self.fonk8()
            return
    def fonk25(self):
        b22 = ('serial number', 'coal')
        item, b18 = QtGui.QInputDialog.getItem(self, 'Connecting a b21', 'Add by', b22, 0, False)
        if b18:
            num, b25 = QtGui.QInputDialog.getInt(self, 'Connecting a b21', 'Input a digit')
            if b25:
                b21 = Depot.b17.fonk25(item, num)
                b24 = f'Car {b21.serial} with {b21.coal} coal connected to the b17'
                self.fonk9(QtGui.QMessageBox.Information, 'Car added', b24)
class class5(class1):
    def fonk26(self, b21 = True):
        self.b21 = b21
        super().fonk28()
        self.setGeometry(500, 150, 200, 400)
        self.b3 = 'pics\\steamtrain.jpg'
        self.b1 = {
            'Home': [self.go_home, 'Go to the main page']
        }
        self.fonk29()
    def fonk27(self):
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
        b26 = QtGui.QLabel(str(self.b21))
        b10 = QtGui.QFont('Times', 12)
        b26.setFont(b10)
        b26.setAlignment(QtCore.Qt.AlignCenter)
        b8.addWidget(b26)
        for key, value in self.b1.b22():
            b12 = QtGui.QPushButton(key)
            b12.clicked.connect(value[0])
            b12.setStatusTip(value[1])
            b8.addWidget(b12)
        b13 = QtGui.QWidget()
        b13.setLayout(b8)
        self.setCentralWidget(b13)
        self.show()
class class6(class5):
    def fonk28(self, b21 = True):
        super().fonk28()
        self.b3 = 'pics\\chocho.jpg'
        self.b2 = 'This is your b17'
        self.setGeometry(500, 150, 250, 200)
        self.b21 = b21
        self.fonk29()
    def fonk29(self):
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
        b27 = QtGui.QTextEdit()
        b27.setText(str(Depot.b17))
        b27.setReadOnly(True)
        b27.setMinimumSize(QtCore.QSize(100, 200))
        b8.addWidget(b27)
        for key, value in self.b1.b22():
            b12 = QtGui.QPushButton(key)
            b12.clicked.connect(value[0])
            b12.setStatusTip(value[1])
            b8.addWidget(b12)
        b13 = QtGui.QWidget()
        b13.setLayout(b8)
        self.setCentralWidget(b13)
        self.show()
if b28 = = '__main__':
    b29 = QtGui.QApplication(sys.argv)
    b14 = class2()
    sys.exit(b29.exec_())