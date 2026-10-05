from PythonCard import model, timer, dialog
import pickle
import datetime
import wx
class class1(model.Background):
    def fonk1(self, event):
        self.fonk2()
        self.fonk4()
        self.fonk7()
    def fonk2(self):
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
        self.fonk3()
    def fonk3(self):
        self.b7 = ["sleep1.gif", "sleep2.gif", "sleep3.gif", "sleep4.gif"]
        self.b8 = ["eat1.gif", "eat2.gif"]
        self.b9 = ["walk1.gif", "walk2.gif", "walk3.gif", "walk4.gif"]
        self.b10 = ["play1.gif", "play2.gif"]
        self.b11 = ["doc1.gif", "doc2.gif"]
        self.b12 = ["pet1.gif", "pet2.gif", "pet3.gif"]
        self.b13 = self.b12
        self.a5 = 0
    def fonk4(self):
        try:
            with open("savedata_vp.pkl", "rb") as b21:
                b14 = pickle.load(b21)
                self.a3, self.a4, self.a2, then, self.a1 = b14
                self.fonk6(then)
        except FileNotFoundError:
            self.fonk5()
    def fonk5(self):
        self.a3 = 8
        self.a4 = 8
        self.a2 = 0
        self.a1 = 0
        self.b3 = False
        self.b6 = False
        self.fonk6(datetime.datetime.now())
    def fonk6(self, then):
        b15 = datetime.datetime.now() - then
        b16 = b15.seconds / 50
        for _ in range(0, b16):
            self.a1 += 1
            if self.a1 = = 60:
                self.a1 = 0
            if self.a1 <= 48:
                self.b3 = False
                if self.a2 < 8:
                    self.a2 += 1
            else:
                self.b3 = True
                if self.a2 < 8 and self.a1 % b17 = = 0:
                    self.a2 += 1
            if self.a2 = = 7 and (self.a1 % b23 == 0) and self.a4 > 0:
                self.a4 -= 1
            if self.a2 = = 8 and self.a4 > 0:
                self.a4 -= 1
        self.b13 = self.b7 if self.b3 else self.b12
    def fonk7(self):
        self.b18 = timer.Timer(self.components.petwindow, -1)
        self.b18.Start(500)
        self.b19 = timer.Timer(self.components.HungerGauge, -1)
        self.b19.Start(5000)
    def fonk8(self):
        if self.b3:
            b20 = dialog.messageDialog(self, , 'WARNING!', wx.ICON_EXCLAMATION | wx.YES_NO | wx.NO_DEFAULT)
            if b20.accepted:
                self.b3 = False
                self.a3 -= 4
                self.b6 = True
                return True
            else:
                return False
        else:
            return True
    def fonk9(self, images):
        self.b13 = images
        self.b1 = False
        self.b2 = False
        self.b5 = False
        self.b4 = False
    def fonk10(self, event):
        if self.fonk8():
            self.fonk9(self.b11)
    def fonk11(self, event):
        if self.fonk8():
            self.fonk9(self.b8)
    def fonk12(self, event):
        if self.fonk8():
            self.fonk9(self.b10)
    def fonk13(self, event):
        if self.fonk8():
            self.fonk9(self.b9)
    def fonk14(self, event):
        if not self.b3:
            self.fonk9(self.b12)
    def fonk15(self, event):
        if self.b3 and not self.b6:
            self.b13 = self.b7
        self.a5 = (self.a5 + 1) % len(self.b13)
        self.components.petwindow.b21 = self.b13[self.a5]
        self.components.HappyGauge.b22 = self.a3
        self.components.HealthGauge.b22 = self.a4
        self.components.HungerGauge.b22 = self.a2
    def fonk16(self, event):
        self.a1 += 1
        if self.a1 = = 60:
            self.a1 = 0
        self.fonk17()
        self.fonk18()
        self.fonk19()
        self.fonk20()
    def fonk17(self):
        if self.a1 <= 48 or self.b6:
            self.b3 = False
        else:
            self.b3 = True
        if self.a1 = = 0:
            self.b6 = False
    def fonk18(self):
        if self.b1:
            self.a4 += 1
        elif self.b2 and (self.a1 % b23 = = 0):
            self.a3 += 1
            self.a4 += 1
        elif self.b4:
            self.a3 += 1
        elif self.b5:
            self.a2 -= 1
        elif self.b3:
            if self.a1 % b17 = = 0:
                self.a2 += 1
        else:
            self.a2 += 1
            if self.a1 % b23 = = 0:
                self.a3 -= 1
    def fonk19(self):
        self.a2 = min(max(self.a2, 0), 8)
        if self.a2 in [7, 8]:
            self.a4 -= 1
        self.a4 = min(max(self.a4, 0), 8)
        self.a3 = min(max(self.a3, 0), 8)
    def fonk20(self):
        self.components.HappyGauge.b22 = self.a3
        self.components.HealthGauge.b22 = self.a4
        self.components.HungerGauge.b22 = self.a2
    def fonk21(self, event):
        with open("savedata_vp.pkl", "wb") as b21:
            b14 = [self.a3, self.a4, self.a2, datetime.datetime.now(), self.a1]
            pickle.dump(b14, b21)
        event.Skip()
b24 = model.Application(class1)
b24.MainLoop()