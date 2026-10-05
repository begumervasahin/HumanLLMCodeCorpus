import threading
import vlc
import gplaylist as grayp
import pafy
import sys
from os import system,b19
import requests
import urllib
class class1:
    def fonk1(self):
        self.b1 = set()
        self.b2 = False
        self.a1 = 150
        self.b3 = True
        self.b4 = b4 = vlc.b4('--input-repeat=-1', '--fullscreen', '--mouse-hide-timeout=0')
        self.b5 = b4.media_player_new()
        self.b1 = grayp.GetQueue().get()
        self.b6 = threading.Thread(target=self.getOptions)
    def fonk2(self, b13):
        self.a1 = b13
    def fonk3(self,lnk):
        b7 = pafy.new(lnk)
        self.b7 = b7
        self.fonk4(b7)
    def fonk4(self,b7):
        self.b8 = self.b4.media_new(b7.getbestaudio().url)
        self.b8.get_mrl()
    def fonk5(self):
        return self.a1
    def fonk6(self):
        while True:
            b9 = input('...>')
            if b9 = = 'pause':
                self.b5.set_pause(1)
            elif b9 = = 'help':
                print('skip : for next song\npause : for pausing playback\nresume : for resuming playback\nfff : to skip forward 5 seconds\nffb : to skip backwards 5 seconds\nvol <volume 0-100> : for setting desired volume\ngvol : to get current audio volume\nmute : to mute audio\nunmute : to unmute audio\nstop : to quit'+
                      'aud : to download audio\nvid : to download video')
            elif b9 = = 'resume':
                self.b5.set_pause(0)
            elif b9 = = 'aud':
                b10 = threading.Thread(target=self.downloada)
                b10.start()
            elif b9 = = 'aud':
                b11 = threading.Thread(target=self.downloadv)
                b11.start()
            elif b9 = = 'fff':
                b12 = self.b5.get_time()
                self.b5.set_time(b12+1000*5)
            elif b9 = = 'ffb':
                b12 = self.b5.get_time()
                if b12-5000 < 0:
                    self.b5.set_time(0)
                else:
                    self.b5.set_time(b12-1000*5)
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
            elif b9 = ='skip':
                self.b5.stop()
                self.b2 = False
            elif b9 = = 'info':
                print(self.b7.title)
                b14 = (self.b5.get_time()
                b14 = b14*10
                b14 = int(b14)
                b15 = self.b5.get_time()
                b16 = b15
                b15 = b15-b16*60
                print(str(b16)+':'+str(b15), b17 = '')
                for b18 in range(10):
                    if b18 = = b14:
                        print('>.', b17 = '')
                    else:
                        print('..', b17 = '')
                b15 = self.b7.length
                b16 = b15
                b15 = b15-b16*60
                print(str(b16)+':'+str(b15), b17 = '')
                print()
            elif b9 = = 'clr':
                if b19 = = 'nt':
                    b20 = system('cls')
                elif b19 = = 'posix':
                    b20 = system('clear')
                else:
                    print('Sorry Clear Screen not supported for your OS : '+b19)
            elif b9 = ='stop':
                print('Stopping the Script...')
                self.b5.stop()
                sys.exit('USER CHOSE TO QUIT')
                exit(0)
    def fonk7(self,b1):
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
                    if self.b5.get_state()==vlc.State.Ended:
                        self.b2 = False
                        self.b5.stop()
                        break
                    if self.b6.isAlive() == False:
                        self.b2 = False
                        sys.exit('USER CHOSE TO EXIT..\n'+'Script might still wait for the download to finish...')
                        break
            except Exception as ex:
                print(ex)
                continue
            continue
        self.b6.join()
        print('QUEUE ENDED')
    def fonk8(self):
        return self.b1
    def fonk9(self):
        b21 = self.b7.getbestaudio()
        print("Size : "+str(b21.get_filesize())+' bytes')
        b22 = b21.download()
    def fonk10(self):
        b21 = self.b7.getbest()
        print("Size : "+str(b21.get_filesize())+' bytes')
        b22 = b21.download()
b23 = class1()
print('PLAYING YOUR QUEUE...')
b1 = b23.fonk8()
if len(b1)>0:
    b23.fonk7(b1)
else:
    print('NO SONGS FOUND IN YOUR PLAYLIST')