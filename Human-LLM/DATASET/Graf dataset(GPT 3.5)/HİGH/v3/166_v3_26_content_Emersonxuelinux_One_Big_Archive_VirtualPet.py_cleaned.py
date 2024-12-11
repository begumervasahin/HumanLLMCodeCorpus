import wx
import pickle
import datetime
class class1(wx.Frame):
    def fonk1(self):
        super().fonk1(None, b1 = "Virtual Pet", size=(800, 600))
        self.b2 = wx.Panel(self)
        self.fonk2()
        self.fonk3()
        self.fonk4()
        self.Bind(wx.EVT_CLOSE, self.on_close)
    def fonk2(self):
        self.b3 = False
        self.b4 = False
        self.b5 = False
        self.b6 = False
        self.b7 = False
        self.a1 = 0
        self.a2 = 0
        self.a3 = 8
        self.a4 = 8
        self.b8 = False
        self.b9 = ["sleep1.gif", "sleep2.gif", "sleep3.gif", "sleep4.gif"]
        self.b10 = ["eat1.gif", "eat2.gif"]
        self.b11 = ["walk1.gif", "walk2.gif", "walk3.gif", "walk4.gif"]
        self.b12 = ["play1.gif", "play2.gif"]
        self.b13 = ["doc1.gif", "doc2.gif"]
        self.b14 = ["pet1.gif", "pet2.gif", "pet3.gif"]
        self.b15 = self.b14
        self.a5 = 0
    def fonk3(self):
        pass
    def fonk4(self):
        try:
            with open("savedata_vp.pkl", "rb") as file:
                b16 = pickle.load(file)
                self.a3, self.a4, self.a2, then, self.a1 = b16
                self.fonk6(then)
        except FileNotFoundError:
            self.fonk5()
    def fonk5(self):
        self.a3 = 8
        self.a4 = 8
        self.a2 = 0
        self.a1 = 0
        self.b5 = False
        self.b8 = False
        self.fonk6(datetime.datetime.now())
    def fonk6(self, then):
        b17 = datetime.datetime.now() - then
        b18 = b17.seconds / 50
        for _ in range(0, b18):
            self.a1 += 1
            if self.a1 = = 60:
                self.a1 = 0
            if self.a1 <= 48:
                self.b5 = False
                if self.a2 < 8:
                    self.a2 += 1
            else:
                self.b5 = True
                if self.a2 < 8 and self.a1 % b19 = = 0:
                    self.a2 += 1
            if self.a2 = = 7 and (self.a1 % 2 == 0) and self.a4 > 0:
                self.a4 -= 1
            if self.a2 = = 8 and self.a4 > 0:
                self.a4 -= 1
        self.b15 = self.b9 if self.b5 else self.b14
    def fonk7(self, event):
        with open("savedata_vp.pkl", "wb") as file:
            b16 = [self.a3, self.a4, self.a2, datetime.datetime.now(), self.a1]
            pickle.dump(b16, file)
        event.Skip()
if b20 = = "__main__":
    b21 = wx.App()
    b22 = class1()
    b22.Show()
    b21.MainLoop()