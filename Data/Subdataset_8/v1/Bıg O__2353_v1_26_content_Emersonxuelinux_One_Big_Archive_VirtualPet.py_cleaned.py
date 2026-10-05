import wx
import pickle
import datetime
import wx.lib.dialogs
class MyBackground(wx.Frame):
    def __init__(self):
        super(MyBackground, self).__init__(None, title="Virtual Pet", size=(800, 600))
        self.panel = wx.Panel(self)
        self.initialize_variables()
        self.create_widgets()
        self.load_saved_data()
        self.Bind(wx.EVT_CLOSE, self.on_close)
    def initialize_variables(self):
        self.doctor = False
        self.walking = False
        self.sleeping = False
        self.playing = False
        self.eating = False
        self.time_cycle = 0
        self.hunger = 0
        self.happiness = 8
        self.health = 8
        self.forceAwake = False
        self.sleepImages = ["sleep1.gif", "sleep2.gif", "sleep3.gif", "sleep4.gif"]
        self.eatImages = ["eat1.gif", "eat2.gif"]
        self.walkImages = ["walk1.gif", "walk2.gif", "walk3.gif", "walk4.gif"]
        self.playImages = ["play1.gif", "play2.gif"]
        self.doctorImages = ["doc1.gif", "doc2.gif"]
        self.nothingImages = ["pet1.gif", "pet2.gif", "pet3.gif"]
        self.imageList = self.nothingImages
        self.imageIndex = 0
    def create_widgets(self):
        pass
    def load_saved_data(self):
        try:
            with open("savedata_vp.pkl", "rb") as file:
                save_list = pickle.load(file)
                self.happiness = save_list[0]
                self.health = save_list[1]
                self.hunger = save_list[2]
                then = save_list[3]
                self.time_cycle = save_list[4]
                self.update_pet_state(then)
        except FileNotFoundError:
            self.reset_pet_state()
    def reset_pet_state(self):
        self.happiness = 8
        self.health = 8
        self.hunger = 0
        self.time_cycle = 0
        self.sleeping = False
        self.forceAwake = False
        self.update_pet_state(datetime.datetime.now())
    def update_pet_state(self, then):
        difference = datetime.datetime.now() - then
        ticks = difference.seconds / 50
        for i in range(0, ticks):
            self.time_cycle += 1
            if self.time_cycle == 60:
                self.time_cycle = 0
            if self.time_cycle <= 48:
                self.sleeping = False
                if self.hunger < 8:
                    self.hunger += 1
            else:
                self.sleeping = True
                if self.hunger < 8 and self.time_cycle % 3 == 0:
                    self.hunger += 1
            if self.hunger == 7 and (self.time_cycle % 2 == 0) and self.health > 0:
                self.health -= 1
            if self.hunger == 8 and self.health > 0:
                self.health -= 1
        if self.sleeping:
            self.imageList = self.sleepImages
        else:
            self.imageList = self.nothingImages
    def on_close(self, event):
        with open("savedata_vp.pkl", "wb") as file:
            save_list = [self.happiness, self.health, self.hunger, datetime.datetime.now(), self.time_cycle]
            pickle.dump(save_list, file)
        event.Skip()
if __name__ == "__main__":
    app = wx.App()
    frame = MyBackground()
    frame.Show()
    app.MainLoop()