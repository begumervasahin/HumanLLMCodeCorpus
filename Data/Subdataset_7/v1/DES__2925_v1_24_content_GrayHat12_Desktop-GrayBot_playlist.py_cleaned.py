import threading
import vlc
import pafy
import sys
import os
import requests
class class1:
    def fonk1(self):
        self.b1 = set()
        self.b2 = False
        self.a1 = 150
        self.b3 = True
        self.b4 = vlc.b4('--input-repeat=-1', '--fullscreen', '--mouse-hide-timeout=0')
        self.b5 = self.b4.media_player_new()
        self.b6 = threading.Thread(target=self.getOptions)
    def fonk2(self, b13):
        self.a1 = b13
    def fonk3(self, lnk):
        b7 = pafy.new(lnk)
        self.b7 = b7
        self.fonk4(b7)
    def fonk4(self, b7):
        self.b8 = self.b4.media_new(b7.getbestaudio().url)
        self.b8.get_mrl()
    def fonk5(self):
        return self.a1
    def fonk6(self):
        while True:
            b9 = input('...> ')
            if b9 = = 'pause':
                self.b5.set_pause(1)
            elif b9 = = 'help':
                print('skip: for next song\npause: for pausing playback\nresume: for resuming playback')
                print('fff: to skip forward 5 seconds\nffb: to skip backwards 5 seconds\nvol <volume 0-100>: for setting desired volume')
                print('gvol: to get current audio volume\nmute: to mute audio\nunmute: to unmute audio\nstop: to quit')
                print('aud: to download audio\nvid: to download video')
            elif b9 = = 'resume':
                self.b5.set_pause(0)
            elif b9 = = 'aud':
                b10 = threading.Thread(target=self.downloada)
                b10.start()
            elif b9 = = 'vid':
                b11 = threading.Thread(target=self.downloadv)
                b11.start()
            elif b9 = = 'fff':
                b12 = self.b5.get_time()
                self.b5.set_time(b12 + 1000 * 5)
            elif b9 = = 'ffb':
                b12 = self.b5.get_time()
                if b12 - 5000 < 0:
                    self.b5.set_time(0)
                else:
                    self.b5.set_time(b12 - 1000 * 5)
            elif b9.startswith('b13'):
                b13 = int(b9.split(' ')[1])
                self.a1 = b13
                self.b5.audio_set_volume(self.a1)
            elif b9 = = 'gvol':
                print(self.b5.audio_get_volume())
            elif b9 = = 'mute':
                self.b5.audio_set_mute(True)
            elif b9 = = 'unmute':
                self.b5.audio_set_mute(False)
            elif b9 = = 'skip':
                self.b5.stop()
                self.b2 = False
            elif b9 = = 'info':
                print(self.b7.title)
                b14 = (self.b5.get_time()
                b14 = b14 * 10
                b14 = int(b14)
                b15 = self.b5.get_time()
                b16 = b15
                b15 = b15 - b16 * 60
                print(str(b16) + ':' + str(b15), b17 = '')
                for b18 in range(10):
                    if b18 = = b14:
                        print('>.', b17 = '')
                    else:
                        print('..', b17 = '')
                b15 = self.b7.length
                b16 = b15
                b15 = b15 - b16 * 60
                print(str(b16) + ':' + str(b15), b17 = '')
                print()
            elif b9 = = 'clr':
                os.system('cls' if os.b19 = = 'nt' else 'clear')
            elif b9 = = 'stop':
                print('Stopping the Script...')
                self.b5.stop()
                sys.exit('USER CHOSE TO QUIT')
                exit(0)
    def fonk7(self, b1):
        self.b3 = True
        print('help for CONTROLS')
        self.b6.start()
        for song in self.b1:
            try:
                self.fonk3(song)
                print('CURRENTLY PLAYING : ',)
                print(self.b7)
                print('FROM YOUR FAVORITE ARTISTS')
                self.b5.set_media(self.b8)
                self.b5.audio_set_volume(self.fonk5())
                self.b5.play()
                self.b2 = True
                while self.b2:
                    if self.b5.get_state() == vlc.State.Ended:
                        self.b2 = False
                        self.b5.stop()
                        break
                    if not self.b6.isAlive():
                        self.b2 = False
                        sys.exit('USER CHOSE TO EXIT..\n' + 'Script might still wait for the download to finish...')