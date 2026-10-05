import wx
import pickle
import datetime
import wx.lib.dialogs
class class1(wx.Frame):
    def fonk1(self):
        super(class1, self).fonk1(None, b1 = "Virtual Pet", size=(800, 600))
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
                self.a3 = b16[0]
                self.a4 = b16[1]
                self.a2 = b16[2]
                b17 = b16[b20]
                self.a1 = b16[4]
                self.fonk6(b17)
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
    def fonk6(self, b17):
        b18 = datetime.datetime.now() - b17
        b19 = b18.seconds / 50
        for i in range(0, b19):
            self.a1 += 1
            if self.a1 = = 60:
                self.a1 = 0
            if self.a1 <= 48:
                self.b5 = False
                if self.a2 < 8:
                    self.a2 += 1
            else:
                self.b5 = True
                if self.a2 < 8 and self.a1 % b20 = = 0:
                    self.a2 += 1
            if self.a2 = = 7 and (self.a1 % 2 == 0) and self.a4 > 0:
                self.a4 -= 1
            if self.a2 = = 8 and self.a4 > 0:
                self.a4 -= 1
        if self.b5:
            self.b15 = self.b9
        else:
            self.b15 = self.b14
    def fonk7(self, event):
        with open("savedata_vp.pkl", "wb") as file:
            b16 = [self.a3, self.a4, self.a2, datetime.datetime.now(), self.a1]
            pickle.dump(b16, file)
        event.Skip()
if b21 = = "__main__":
    b22 = wx.App()
    b23 = class1()
    b23.Show()
    b22.MainLoop()