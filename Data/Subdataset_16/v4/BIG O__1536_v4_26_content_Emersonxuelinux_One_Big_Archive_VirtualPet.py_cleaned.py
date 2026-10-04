import pickle
import datetime
import wx
from PythonCard import model, timer, dialog
class class1(model.Background):
    def fonk1(self, event):
        self.fonk2()
        self.fonk3()
        self.update_pet_state_based_on_time()
        self.fonk6()
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
        self.b7 = ["sleep1.gif", "sleep2.gif", "sleep3.gif", "sleep4.gif"]
        self.b8 = ["eat1.gif", "eat2.gif"]
        self.b9 = ["walk1.gif", "walk2.gif", "walk3.gif", "walk4.gif"]
        self.b10 = ["play1.gif", "play2.gif"]
        self.b11 = ["doc1.gif", "doc2.gif"]
        self.b12 = ["pet1.gif", "pet2.gif", "pet3.gif"]
        self.b13 = self.b12
        self.a5 = 0
    def fonk3(self):
        try:
            with open("savedata_vp.pkl", "rb") as b23:
                b14 = pickle.load(b23)
        except (FileNotFoundError, EOFError):
            b14 = [8, 8, 0, datetime.datetime.now(), 0]
        self.a3, self.a4, self.a2, saved_time, self.a1 = b14
        b15 = datetime.datetime.now() - saved_time
        self.fonk4(b15)
    def fonk4(self, b15):
        b16 = b15.seconds
        for _ in range(b16):
            self.a1 = (self.a1 + 1) % 60
            self.fonk5()
    def fonk5(self):
        if self.a1 <= 48:
            self.b3 = False
            if self.a2 < 8:
                self.a2 += 1
        else:
            self.b3 = True
            if self.a2 < 8 and self.a1 % b17 = = 0:
                self.a2 += 1
        if self.a2 >= 7 and self.a1 % b18 = = 0 and self.a4 > 0:
            self.a4 -= 1
        if self.a2 = = 8 and self.a4 > 0:
            self.a4 -= 1
    def fonk6(self):
        self.b19 = timer.Timer(self.components.petwindow, -1)
        self.b19.Start(500)
        self.b20 = timer.Timer(self.components.HungerGauge, -1)
        self.b20.Start(5000)
    def fonk7(self):
        if self.b3:
            b21 = dialog.messageDialog(
                self,
                "WARNING!\nYour pet is b3, if you wake him up he'll be unhappy!\nDo you want to proceed?",
                'WARNING!',
                wx.ICON_EXCLAMATION | wx.YES_NO | wx.NO_DEFAULT
            )
            if b21.accepted:
                self.b3 = False
                self.a3 -= 4
                self.b6 = True
                return True
            else:
                return False
        return True
    def fonk8(self, event):
        if self.fonk7():
            self.fonk13('b1')
    def fonk9(self, event):
        if self.fonk7():
            self.fonk13('b5')
    def fonk10(self, event):
        if self.fonk7():
            self.fonk13('b4')
    def fonk11(self, event):
        if self.fonk7():
            self.fonk13('b2')
    def fonk12(self, event):
        if not self.b3:
            self.fonk13('nothing')
    def fonk13(self, activity):
        b22 = {
            'b1': self.b11,
            'b5': self.b8,
            'b4': self.b10,
            'b2': self.b9,
            'nothing': self.b12
        }
        self.b13 = b22[activity]
        self.b1 = (activity == 'b1')
        self.b5 = (activity == 'b5')
        self.b4 = (activity == 'b4')
        self.b2 = (activity == 'b2')
    def fonk14(self, event):
        if self.b3 and not self.b6:
            self.b13 = self.b7
        self.a5 = (self.a5 + 1) % len(self.b13)
        self.fonk20()
    def fonk15(self, event):
        self.fonk16()
        self.fonk17()
        self.fonk18()
        self.fonk19()
        self.fonk20()
    def fonk16(self):
        self.a1 = (self.a1 + 1) % 60
        if self.a1 = = 0:
            self.b6 = False
    def fonk17(self):
        self.b3 = self.a1 > 48 and not self.b6
    def fonk18(self):
        if self.b1:
            self.a4 = min(self.a4 + 1, 8)
        elif self.b2 and self.a1 % b18 = = 0:
            self.a3 = min(self.a3 + 1, 8)
            self.a4 = min(self.a4 + 1, 8)
        elif self.b4:
            self.a3 = min(self.a3 + 1, 8)
        elif self.b5:
            self.a2 = max(self.a2 - 1, 0)
        elif self.b3:
            if self.a1 % b17 = = 0:
                self.a2 = min(self.a2 + 1, 8)
        else:
            self.a2 = min(self.a2 + 1, 8)
            if self.a1 % b18 = = 0:
                self.a3 = max(self.a3 - 1, 0)
        if self.a2 >= 7 and self.a1 % b18 = = 0:
            self.a4 = max(self.a4 - 1, 0)
        if self.a2 = = 8:
            self.a4 = max(self.a4 - 1, 0)
    def fonk19(self):
        self.a2 = min(max(self.a2, 0), 8)
        self.a4 = min(max(self.a4, 0), 8)
        self.a3 = min(max(self.a3, 0), 8)
    def fonk20(self):
        self.components.petwindow.b23 = self.b13[self.a5]
        self.components.HappyGauge.b24 = self.a3
        self.components.HealthGauge.b24 = self.a4
        self.components.HungerGauge.b24 = self.a2
    def fonk21(self, event):
        self.fonk22()
        event.Skip()
    def fonk22(self):
        b14 = [self.a3, self.a4, self.a2, datetime.datetime.now(), self.a1]
        with open("savedata_vp.pkl", "wb") as b23:
            pickle.dump(b14, b23)
b25 = model.Application(class1)
b25.MainLoop()