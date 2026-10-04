import wx
from PythonCard import model, timer, dialog
import pickle
import datetime
class class1(model.Background):
    def fonk1(self, event):
        self.b1 = False
        self.b2 = False
        self.b3 = False
        self.b4 = False
        self.b5 = False
        self.a1 = 0
        self.a2 = 0
        self.a3 = 8
        self.a4 = 8
        self.b6 = False
        self.b7 = ["sleep1.gif", "sleep2.gif", "sleep3.gif", "sleep4.gif"]
        self.b8 = ["eat1.gif", "eat2.gif"]
        self.b9 = ["walk1.gif", "walk2.gif", "walk3.gif", "walk4.gif"]
        self.b10 = ["play1.gif", "play2.gif"]
        self.b11 = ["doc1.gif", "doc2.gif"]
        self.b12 = ["pet1.gif", "pet2.gif", "pet3.gif"]
        self.b13 = self.b12
        self.a5 = 0
        self.b14 = timer.Timer(self.components.petwindow, -1)
        self.b14.Start(500)
        self.b15 = timer.Timer(self.components.HungerGauge, -1)
        self.b15.Start(5000)
        try:
            with open("savedata_vp.pkl", "rb") as b21:
                b16 = pickle.load(b21)
        except FileNotFoundError:
            b16 = [8, 8, 0, datetime.datetime.now(), 0]
        self.a3 = b16[0]
        self.a4 = b16[1]
        self.a2 = b16[b22]
        b17 = b16[b23]
        self.a1 = b16[4]
        b18 = datetime.datetime.now() - b17
        b19 = int(b18.total_seconds() / 50)
        for _ in range(b19):
            self.fonk11()
        if self.b3:
            self.b13 = self.b7
        else:
            self.b13 = self.b12
    def fonk2(self):
        if self.b3:
            b20 = dialog.messageDialog(self,
                "WARNING!\nYour pet is b3, if you wake him up he'll be unhappy!\nDo you want to proceed?",
                'WARNING!', wx.ICON_EXCLAMATION | wx.YES_NO | wx.NO_DEFAULT)
            if b20.accepted:
                self.b3 = False
                self.a3 -= 4
                self.b6 = True
                return True
            else:
                return False
        else:
            return True
    def fonk3(self, event):
        if self.fonk2():
            self.b13 = self.b11
            self.fonk8(b1 = True)
    def fonk4(self, event):
        if self.fonk2():
            self.b13 = self.b8
            self.fonk8(b5 = True)
    def fonk5(self, event):
        if self.fonk2():
            self.b13 = self.b10
            self.fonk8(b4 = True)
    def fonk6(self, event):
        if self.fonk2():
            self.b13 = self.b9
            self.fonk8(b2 = True)
    def fonk7(self, event):
        if not self.b3:
            self.b13 = self.b12
            self.fonk8()
    def fonk8(self, b1 = False, b5=False, b4=False, b2=False):
        self.b1 = b1
        self.b5 = b5
        self.b4 = b4
        self.b2 = b2
    def fonk9(self, event):
        if self.b3 and not self.b6:
            self.b13 = self.b7
        self.a5 = (self.a5 + 1) % len(self.b13)
        self.components.petwindow.b21 = self.b13[self.a5]
        self.fonk12()
    def fonk10(self, event):
        self.fonk11()
        self.fonk12()
    def fonk11(self):
        self.a1 = (self.a1 + 1) % 60
        if self.a1 <= 48 or self.b6:
            self.b3 = False
        else:
            self.b3 = True
        if self.a1 = = 0:
            self.b6 = False
        if self.b1:
            self.a4 = min(self.a4 + 1, 8)
        elif self.b2 and self.a1 % b22 = = 0:
            self.a3 = min(self.a3 + 1, 8)
            self.a4 = min(self.a4 + 1, 8)
        elif self.b4:
            self.a3 = min(self.a3 + 1, 8)
        elif self.b5:
            self.a2 = max(self.a2 - 1, 0)
        elif self.b3 and self.a1 % b23 = = 0:
            self.a2 = min(self.a2 + 1, 8)
        else:
            self.a2 = min(self.a2 + 1, 8)
            if self.a1 % b22 = = 0:
                self.a3 = max(self.a3 - 1, 0)
        if self.a2 >= 7 and self.a1 % b22 = = 0:
            self.a4 = max(self.a4 - 1, 0)
        if self.a2 = = 8:
            self.a4 = max(self.a4 - 1, 0)
    def fonk12(self):
        self.components.HappyGauge.b24 = self.a3
        self.components.HealthGauge.b24 = self.a4
        self.components.HungerGauge.b24 = self.a2
    def fonk13(self, event):
        with open("savedata_vp.pkl", "wb") as b21:
            b16 = [self.a3, self.a4, self.a2, datetime.datetime.now(), self.a1]
            pickle.dump(b16, b21)
        event.Skip()
b25 = model.Application(class1)
b25.MainLoop()