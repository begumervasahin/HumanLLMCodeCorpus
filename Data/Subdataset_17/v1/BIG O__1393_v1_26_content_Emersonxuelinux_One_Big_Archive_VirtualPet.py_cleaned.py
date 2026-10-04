import wx
from PythonCard import model, timer, dialog
import pickle
import datetime
class MyBackground(model.Background):
    def on_initialize(self, event):
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
        self.myTimer1 = timer.Timer(self.components.petwindow, -1)
        self.myTimer1.Start(500)
        self.myTimer2 = timer.Timer(self.components.HungerGauge, -1)
        self.myTimer2.Start(5000)
        try:
            with open("savedata_vp.pkl", "rb") as file:
                save_list = pickle.load(file)
        except FileNotFoundError:
            save_list = [8, 8, 0, datetime.datetime.now(), 0]
        self.happiness = save_list[0]
        self.health = save_list[1]
        self.hunger = save_list[2]
        then = save_list[3]
        self.time_cycle = save_list[4]
        difference = datetime.datetime.now() - then
        ticks = int(difference.total_seconds() / 50)
        for _ in range(ticks):
            self.update_state()
        if self.sleeping:
            self.imageList = self.sleepImages
        else:
            self.imageList = self.nothingImages
    def sleep_test(self):
        if self.sleeping:
            result = dialog.messageDialog(self,
                "WARNING!\nYour pet is sleeping, if you wake him up he'll be unhappy!\nDo you want to proceed?",
                'WARNING!', wx.ICON_EXCLAMATION | wx.YES_NO | wx.NO_DEFAULT)
            if result.accepted:
                self.sleeping = False
                self.happiness -= 4
                self.forceAwake = True
                return True
            else:
                return False
        else:
            return True
    def on_doctor_mouseClick(self, event):
        if self.sleep_test():
            self.imageList = self.doctorImages
            self.set_activity(doctor=True)
    def on_feed_mouseClick(self, event):
        if self.sleep_test():
            self.imageList = self.eatImages
            self.set_activity(eating=True)
    def on_play_mouseClick(self, event):
        if self.sleep_test():
            self.imageList = self.playImages
            self.set_activity(playing=True)
    def on_walk_mouseClick(self, event):
        if self.sleep_test():
            self.imageList = self.walkImages
            self.set_activity(walking=True)
    def on_stop_mouseClick(self, event):
        if not self.sleeping:
            self.imageList = self.nothingImages
            self.set_activity()
    def set_activity(self, doctor=False, eating=False, playing=False, walking=False):
        self.doctor = doctor
        self.eating = eating
        self.playing = playing
        self.walking = walking
    def on_petwindow_timer(self, event):
        if self.sleeping and not self.forceAwake:
            self.imageList = self.sleepImages
        self.imageIndex = (self.imageIndex + 1) % len(self.imageList)
        self.components.petwindow.file = self.imageList[self.imageIndex]
        self.update_gauges()
    def on_HungerGauge_timer(self, event):
        self.update_state()
        self.update_gauges()
    def update_state(self):
        self.time_cycle = (self.time_cycle + 1) % 60
        if self.time_cycle <= 48 or self.forceAwake:
            self.sleeping = False
        else:
            self.sleeping = True
        if self.time_cycle == 0:
            self.forceAwake = False
        if self.doctor:
            self.health = min(self.health + 1, 8)
        elif self.walking and self.time_cycle % 2 == 0:
            self.happiness = min(self.happiness + 1, 8)
            self.health = min(self.health + 1, 8)
        elif self.playing:
            self.happiness = min(self.happiness + 1, 8)
        elif self.eating:
            self.hunger = max(self.hunger - 1, 0)
        elif self.sleeping and self.time_cycle % 3 == 0:
            self.hunger = min(self.hunger + 1, 8)
        else:
            self.hunger = min(self.hunger + 1, 8)
            if self.time_cycle % 2 == 0:
                self.happiness = max(self.happiness - 1, 0)
        if self.hunger >= 7 and self.time_cycle % 2 == 0:
            self.health = max(self.health - 1, 0)
        if self.hunger == 8:
            self.health = max(self.health - 1, 0)
    def update_gauges(self):
        self.components.HappyGauge.value = self.happiness
        self.components.HealthGauge.value = self.health
        self.components.HungerGauge.value = self.hunger
    def on_close(self, event):
        with open("savedata_vp.pkl", "wb") as file:
            save_list = [self.happiness, self.health, self.hunger, datetime.datetime.now(), self.time_cycle]
            pickle.dump(save_list, file)
        event.Skip()
app = model.Application(MyBackground)
app.MainLoop()