from PythonCard import model, timer, dialog
import pickle, datetime, wx
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
        self.b7 = ["sleep1.gif","sleep2.gif","sleep3.gif", "sleep4.gif"]
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
        b16 = True
        try:
            b17 = open("savedata_vp.pkl", "r")
        except:
            b16 = False
        if b16:
            b18 = pickle.load(b17)
            b17.close()
        else:
            b18 = [8, 8, 0, datetime.datetime.now(), 0]
        self.a3 = b18[0]
        self.a4 = b18[1]
        self.a2 = b18[b25]
        b19 = b18[b22]
        self.a1 = b18[4]
        b20 = datetime.datetime.now() - b19
        b21 = b20.seconds / 50
        for i in range(0, b21):
            self.a1 += 1
            if self.a1 = = 60:
                self.a1 = 0
            if self.a1 <= 48:
                self.b3 = False
                if self.a2 < 8:
                    self.a2 += 1
            else:
                self.b3 = True
                if self.a2 < 8 and self.a1 % b22 = = 0:
                    self.a2 += 1
            if self.a2 = = 7 and (self.a1 % b25 ==0) and self.a4 > 0:
                self.a4 -= 1
            if self.a2 = = 8 and self.a4 > 0:
                self.a4 -=1
        if self.b3:
            self.b13 = self.b7
        else:
            self.b13 = self.b12
    def fonk2(self):
        if self.b3:
            b23 = dialog.messageDialog(self, , 'WARNING!',
wx.ICON_EXCLAMATION | wx.YES_NO | wx.NO_DEFAULT)
            if b23.accepted:
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
            self.b1 = True
            self.b2 = False
            self.b5 = False
            self.b4 = False
    def fonk4(self, event):
        if self.fonk2():
            self.b13 = self.b8
            self.b5 = True
            self.b2 = False
            self.b4 = False
            self.b1 = False
    def fonk5(self, event):
        if self.fonk2():
            self.b13 = self.b10
            self.b4 = True
            self.b2 = False
            self.b5 = False
            self.b1 = False
    def fonk6(self, event):
        if self.fonk2():
            self.b13 = self.b9
            self.b2 = True
            self.b5 = False
            self.b4 = False
            self.b1 = False
    def fonk7(self, event):
        if not self.b3:
            self.b13 = self.b12
            self.b2 = False
            self.b5 = False
            self.b4 = False
            self.b1 = False
    def fonk8(self, event):
        if self.b3 and not self.b6:
            self.b13 = self.b7
        self.a5 += 1
        if self.a5 >= len(self.b13):
            self.a5 = 0
        self.components.petwindow.b17 = self.b13[self.a5]
        self.components.HappyGauge.b24 = self.a3
        self.components.HealthGauge.b24 = self.a4
        self.components.HungerGauge.b24 = self.a2
    def fonk9(self, event):
        self.a1 += 1
        if self.a1 = = 60:
            self.a1 = 0
        if self.a1 <= 48 or self.b6:
            self.b3 = False
        else:
            self.b3 = True
        if self.a1 = = 0:
            self.b6 = False
        if self.b1:
            self.a4 += 1
        elif self.b2 and (self.a1 % b25 = = 0):
            self.a3 += 1
            self.a4 += 1
        elif self.b4:
            self.a3 += 1
        elif self.b5:
            self.a2 -= 1
        elif self.b3:
            if self.a1 % b22 = = 0:
                self.a2 += 1
        else:
            self.a2 += 1
            if self.a1 % b25 = = 0:
                self.a3 -= 1
        if self.a2 > 8:  self.a2 = 8
        if self.a2 < 0:  self.a2 = 0
        if self.a2 = = 7 and (self.a1 % b25 ==0) :
            self.a4 -= 1
        if self.a2 = = 8:
            self.a4 -=1
        if self.a4 > 8:  self.a4 = 8
        if self.a4 < 0:  self.a4 = 0
        if self.a3 > 8:  self.a3 = 8
        if self.a3 < 0:  self.a3 = 0
        self.components.HappyGauge.b24 = self.a3
        self.components.HealthGauge.b24 = self.a4
        self.components.HungerGauge.b24 = self.a2
    def fonk10(self, event):
        b17 = open("savedata_vp.pkl", "w")
        b18 = [self.a3, self.a4, self.a2, datetime.datetime.now(), self.a1]
        pickle.dump(b18, b17)
        event.Skip()
b26 = model.Application(class1)
b26.MainLoop()