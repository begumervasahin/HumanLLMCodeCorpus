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
        self.b1 = {
            'doctor': False,
            'walking': False,
            'sleeping': False,
            'playing': False,
            'eating': False
        }
        self.a1 = 0
        self.a2 = 0
        self.a3 = 8
        self.a4 = 8
        self.b2 = False
        self.b3 = {
            'sleep': ["sleep1.gif", "sleep2.gif", "sleep3.gif", "sleep4.gif"],
            'eat': ["eat1.gif", "eat2.gif"],
            'walk': ["walk1.gif", "walk2.gif", "walk3.gif", "walk4.gif"],
            'play': ["play1.gif", "play2.gif"],
            'doctor': ["doc1.gif", "doc2.gif"],
            'nothing': ["pet1.gif", "pet2.gif", "pet3.gif"]
        }
        self.b4 = self.b3['nothing']
        self.a5 = 0
    def fonk3(self):
        try:
            with open("savedata_vp.pkl", "rb") as b14:
                b5 = pickle.load(b14)
        except (FileNotFoundError, EOFError):
            b5 = [8, 8, 0, datetime.datetime.now(), 0]
        self.a3, self.a4, self.a2, saved_time, self.a1 = b5
        b6 = datetime.datetime.now() - saved_time
        self.fonk4(b6)
    def fonk4(self, b6):
        b7 = b6.seconds
        for _ in range(b7):
            self.a1 = (self.a1 + 1) % 60
            self.fonk5()
    def fonk5(self):
        if self.a1 <= 48:
            self.b1['sleeping'] = False
            if self.a2 < 8:
                self.a2 += 1
        else:
            self.b1['sleeping'] = True
            if self.a2 < 8 and self.a1 % b8 = = 0:
                self.a2 += 1
        if self.a2 >= 7 and self.a1 % b9 = = 0 and self.a4 > 0:
            self.a4 -= 1
        if self.a2 = = 8 and self.a4 > 0:
            self.a4 -= 1
    def fonk6(self):
        self.b10 = timer.Timer(self.components.petwindow, -1)
        self.b10.Start(500)
        self.b11 = timer.Timer(self.components.HungerGauge, -1)
        self.b11.Start(5000)
    def fonk7(self):
        if self.b1['sleeping']:
            b12 = dialog.messageDialog(
                self,
                "WARNING!\nYour pet is sleeping, if you wake him up he'll be unhappy!\nDo you want to proceed?",
                'WARNING!',
                wx.ICON_EXCLAMATION | wx.YES_NO | wx.NO_DEFAULT
            )
            if b12.accepted:
                self.b1['sleeping'] = False
                self.a3 -= 4
                self.b2 = True
                return True
            else:
                return False
        return True
    def fonk8(self, event):
        if self.fonk7():
            self.fonk13('doctor')
    def fonk9(self, event):
        if self.fonk7():
            self.fonk13('eating')
    def fonk10(self, event):
        if self.fonk7():
            self.fonk13('playing')
    def fonk11(self, event):
        if self.fonk7():
            self.fonk13('walking')
    def fonk12(self, event):
        if not self.b1['sleeping']:
            self.fonk13('nothing')
    def fonk13(self, activity):
        self.b4 = self.b3[activity]
        for b13 in self.b1:
            self.b1[b13] = (b13 = = activity)
    def fonk14(self, event):
        if self.b1['sleeping'] and not self.b2:
            self.b4 = self.b3['sleep']
        self.a5 = (self.a5 + 1) % len(self.b4)
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
            self.b2 = False
    def fonk17(self):
        self.b1['sleeping'] = self.a1 > 48 and not self.b2
    def fonk18(self):
        if self.b1['doctor']:
            self.a4 = min(self.a4 + 1, 8)
        elif self.b1['walking'] and self.a1 % b9 = = 0:
            self.a3 = min(self.a3 + 1, 8)
            self.a4 = min(self.a4 + 1, 8)
        elif self.b1['playing']:
            self.a3 = min(self.a3 + 1, 8)
        elif self.b1['eating']:
            self.a2 = max(self.a2 - 1, 0)
        elif self.b1['sleeping']:
            if self.a1 % b8 = = 0:
                self.a2 = min(self.a2 + 1, 8)
        else:
            self.a2 = min(self.a2 + 1, 8)
            if self.a1 % b9 = = 0:
                self.a3 = max(self.a3 - 1, 0)
        if self.a2 >= 7 and self.a1 % b9 = = 0:
            self.a4 = max(self.a4 - 1, 0)
        if self.a2 = = 8:
            self.a4 = max(self.a4 - 1, 0)
    def fonk19(self):
        self.a2 = min(max(self.a2, 0), 8)
        self.a4 = min(max(self.a4, 0), 8)
        self.a3 = min(max(self.a3, 0), 8)
    def fonk20(self):
        self.components.petwindow.b14 = self.b4[self.a5]
        self.components.HappyGauge.b15 = self.a3
        self.components.HealthGauge.b15 = self.a4
        self.components.HungerGauge.b15 = self.a2
    def fonk21(self, event):
        self.fonk22()
        event.Skip()
    def fonk22(self):
        b5 = [self.a3, self.a4, self.a2, datetime.datetime.now(), self.a1]
        with open("savedata_vp.pkl", "wb") as b14:
            pickle.dump(b5, b14)
b16 = model.Application(class1)
b16.MainLoop()