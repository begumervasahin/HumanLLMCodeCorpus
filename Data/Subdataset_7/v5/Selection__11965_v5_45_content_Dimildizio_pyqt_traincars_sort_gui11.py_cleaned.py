import sys
from PyQt4 import QtGui, QtCore
from cars_coal import *
class class1(QtGui.QMainWindow):
    def fonk1(self):
        super().fonk31()
        self.b1 = {
            'Show': [self.go_train, 'Show the whole b16'],
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
        self.statusBar()
        self.fonk2()
        self.fonk32()
    def fonk2(self):
        b4 = QtGui.QAction('&Exit me', self)
        b4.setShortcut('Ctrl+Q')
        b4.setStatusTip('Leave the App')
        b4.triggered.connect(self.close_me)
        b5 = self.menuBar()
        b6 = b5.addMenu('&File')
        b6.addAction(b4)
        b6.addSeparator()
    def fonk3(self):
        b7 = QtGui.QVBoxLayout()
        b8 = self.fonk4(self.b2)
        b7.addWidget(b8)
        b9 = self.fonk5(self.b3)
        b7.addWidget(b9)
        for key, value in self.b1.b22():
            b10 = self.fonk6(key, value[0], value[1])
            b7.addWidget(b10)
        b11 = QtGui.QWidget()
        b11.setLayout(b7)
        self.setCentralWidget(b11)
        self.show()
    def fonk4(self, b24):
        b8 = QtGui.QLabel(b24)
        b12 = QtGui.QFont('Times', 14)
        b12.setBold(1)
        b8.setFont(b12)
        b8.setAlignment(QtCore.Qt.AlignCenter)
        return b8
    def fonk5(self, b3):
        b9 = QtGui.QLabel()
        b9.setPixmap(QtGui.QPixmap(b3))
        b9.setAlignment(QtCore.Qt.AlignCenter)
        b9.setScaledContents(True)
        return b9
    def fonk6(self, b24, func, tip):
        b10 = QtGui.QPushButton(b24)
        b10.clicked.connect(func)
        b10.setStatusTip(tip)
        return b10
    def fonk7(self):
        self.close()
        self.b13 = class4()
    def fonk8(self):
        self.close()
        self.b13 = class6()
    def fonk9(self):
        self.close()
        self.b13 = class1()
    def fonk10(self):
        self.close()
        self.b13 = class3()
    def fonk11(self):
        self.close()
        self.b13 = class2()
    def fonk12(self, icon, title, b24):
        b14 = QtGui.QMessageBox(
            icon, title, b24, b1 = QtGui.QMessageBox.Ok)
        return b14.exec_()
    def fonk13(self):
        b14 = QtGui.QMessageBox()
        b14.setText('Are you sure you want to exit?')
        b14.setWindowTitle('Exit')
        b14.setIcon(QtGui.QMessageBox.Information)
        b14.addButton(QtGui.QPushButton('Yes'), QtGui.QMessageBox.YesRole)
        b14.addButton(QtGui.QPushButton('No'), QtGui.QMessageBox.NoRole)
        b15 = b14.exec_()
        if not b15:
            sys.exit()
    def fonk14(self):
        self.fonk12(QtGui.QMessageBox.Information, 'Boom!',
                       'Your b16 has been destroyed')
        Depot.b16 = False
        self.fonk11()
class class2(class1):
    def fonk15(self):
        super().fonk31()
        self.b1 = {
            'Generate': [self.get_train, 'Generate a b16'],
            'Exit': [self.close_me, 'Close the application']
        }
        self.b2 = 'Welcome to the b16 manager!\nDo you wish to create a b16?'
        self.b3 = 'pics\\facttrain.jpg'
        self.fonk32()
    def fonk16(self):
        num, b17 = QtGui.QInputDialog.getInt(
            self, 'Generating b16', 'How many cars?')
        if b17:
            if num > 5000:
                self.fonk12(QtGui.QMessageBox.Warning,
                               'You\'ve been rejected',
                               "You've requested too many cars")
            elif num < 1:
                self.fonk12(QtGui.QMessageBox.Warning,
                               'You\'ve been rejected',
                               "There is no point for you in b16 without cars")
            else:
                Depot.generate(num)
                self.fonk9()
class class3(class1):
    def fonk17(self, b16 = False):
        super().fonk31()
        self.setGeometry(500, 150, 300, 450)
        self.b3 = 'pics\\Aurora610.jpg'
        self.b2 = 'Arrange the cars'
        self.fonk18()
        self.b1 = {
            'Home': [self.go_home, 'Go to the main page'],
            'Bubble sort': [self.call_bubble, 'Bubble sorting algorithm'],
            'Selection sort': [self.call_selection, 'Selection sorting algorithm'],
            'Insertion sort': [self.call_insertion, 'Insertion sorting algorithm'],
            'Exit': [self.close_me, 'Close the application']
        }
        self.fonk32()
    def fonk18(self):
        b14 = self.fonk19('Sort b18?', ['From left to right', 'From right to left'])
        self.b18 = b14.exec_()
        b19 = self.fonk19('Sort parameter?', ['Serial number', 'Quantity of coal'])
        self.b20 = b19.exec_()
    def fonk19(self, title, b1):
        b14 = QtGui.QMessageBox()
        b14.setText(title)
        b14.setWindowTitle('Sorting')
        for btn_text in b1:
            b14.addButton(QtGui.QPushButton(btn_text), QtGui.QMessageBox.YesRole)
        return b14
    def fonk20(self):
        self.fonk23('Selection sort completed')
        if self.b18:
            return Depot.b16.select_sort_to_left(self.b20)
        return Depot.b16.select_sort_to_right(self.b20)
    def fonk21(self):
        self.fonk23('Bubble sort completed')
        if self.b18:
            return Depot.b16.bubble_sort_to_left(self.b20)
        return Depot.b16.bubble_sort_to_right(self.b20)
    def fonk22(self):
        self.fonk23('Insertion sort completed')
        if self.b18:
            return Depot.b16.insertion_sort_to_left(self.b20)
        return Depot.b16.insertion_sort_to_right(self.b20)
    def fonk23(self, message):
        self.fonk12(QtGui.QMessageBox.Information, 'Sorted completed', message)
class class4(class1):
    def fonk24(self, b16 = False):
        super().fonk31()
        self.b3 = 'pics\\steam_train.jpg'
        self.b2 = 'Cars'
        self.b1 = {
            'Home': [self.go_home, 'Go to the main page'],
            'Add a b21': [self.add_car, 'Add more cars'],
            'Find a b21': [self.find_car, 'Search for a b21'],
            'Remove a b21': [self.remove_car, 'Delete a b21'],
            'Exit': [self.close_me, 'Close the application']
        }
        self.fonk32()
    def fonk25(self):
        b21 = self.fonk26()
        if b21:
            self.close()
            self.b13 = class5(b21)
    def fonk26(self):
        b22 = ('serial', 'coal', 'index')
        item, b17 = QtGui.QInputDialog.getItem(
            self, 'Find a b21', 'Find by', b22, 0, False)
        if b17:
            num, b17 = QtGui.QInputDialog.getInt(
                self, 'Finding', 'Input a digit')
            b21 = Depot.b16.find_by_type(num, item)
            if b21:
                return b21
            else:
                self.fonk12(QtGui.QMessageBox.Information,
                               'Ooops', 'Car not found')
    def fonk27(self):
        b23 = self.fonk26()
        if b23:
            b24 = f'Car {b23.serial} disconnected from the b16'
            Depot.b16.cars.remove(b23)
            self.fonk12(QtGui.QMessageBox.Information,
                           'Car removed', b24)
        if len(Depot.b16.cars) < 1:
            self.fonk12(QtGui.QMessageBox.Critical,
                           'Train confiscated',
                           'You don\'t have any cars left\nYour b16 has been confiscated')
            self.fonk11()
    def fonk28(self):
        b22 = ('serial number', 'coal')
        item, b17 = QtGui.QInputDialog.getItem(
            self, 'Connecting a b21', 'Add by', b22, 0, False)
        if b17:
            num, b25 = QtGui.QInputDialog.getInt(
                self, 'Connecting a b21', 'Input a digit')
            if b25:
                b21 = Depot.b16.fonk28(item, num)
                b24 = f'Car {b21.serial} with {b21.coal} coal connected to the b16'
                self.fonk12(QtGui.QMessageBox.Information,
                               'Car added', b24)
class class5(class1):
    def fonk29(self, b21 = True):
        self.b21 = b21
        super().fonk31()
        self.setGeometry(500, 150, 200, 400)
        self.b3 = 'pics\\steamtrain.jpg'
        self.b1 = {'Home': [self.go_home, 'Go to the main page']}
        self.fonk32()
    def fonk30(self):
        b7 = QtGui.QVBoxLayout()
        b8 = self.fonk4('Search result')
        b7.addWidget(b8)
        b9 = self.fonk5(self.b3)
        b7.addWidget(b9)
        b26 = self.fonk4(str(self.b21))
        b7.addWidget(b26)
        for key, value in self.b1.b22():
            b10 = self.fonk6(key, value[0], value[1])
            b7.addWidget(b10)
        b11 = QtGui.QWidget()
        b11.setLayout(b7)
        self.setCentralWidget(b11)
        self.show()
class class6(class5):
    def fonk31(self, b21 = True):
        super().fonk31()
        self.b3 = 'pics\\chocho.jpg'
        self.b2 = 'This is your b16'
        self.setGeometry(500, 150, 250, 200)
        self.b21 = b21
        self.fonk32()
    def fonk32(self):
        b7 = QtGui.QVBoxLayout()
        b8 = self.fonk4(self.b2)
        b7.addWidget(b8)
        b9 = self.fonk5(self.b3)
        b7.addWidget(b9)
        b27 = QtGui.QTextEdit()
        b27.setText(str(Depot.b16))
        b27.setReadOnly(True)
        b27.setMinimumSize(QtCore.QSize(100, 200))
        b7.addWidget(b27)
        for key, value in self.b1.b22():
            b10 = self.fonk6(key, value[0], value[1])
            b7.addWidget(b10)
        b11 = QtGui.QWidget()
        b11.setLayout(b7)
        self.setCentralWidget(b11)
        self.show()
if b28 = = '__main__':
    b29 = QtGui.QApplication(sys.argv)
    b13 = class2()
    sys.exit(b29.exec())