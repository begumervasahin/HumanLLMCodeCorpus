import threading
import vlc
import pafy
import sys
import os
class class1:
    def fonk1(self):
        self.b1 = set()
        self.b2 = False
        self.a1 = 150
        self.b3 = True
        self.b4 = vlc.b4('--input-repeat=-1', '--fullscreen', '--mouse-hide-timeout=0')
        self.b5 = self.b4.media_player_new()
        self.b6 = threading.Thread(target=self.getOptions)
    def fonk2(self, b14):
        self.a1 = b14
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
                self.fonk7()
            elif b9 = = 'resume':
                self.b5.set_pause(0)
            elif b9 in ('aud', 'vid'):
                self.fonk8(b9)
            elif b9 in ('fff', 'ffb'):
                self.fonk10(b9)
            elif b9.startswith('b14'):
                self.fonk11(b9)
            elif b9 = = 'gvol':
                print(self.b5.audio_get_volume())
            elif b9 in ('mute', 'unmute'):
                self.fonk12(b9)
            elif b9 = = 'skip':
                self.fonk13()
            elif b9 = = 'info':
                self.fonk14()
            elif b9 = = 'clr':
                self.fonk15()
            elif b9 = = 'stop':
                self.fonk16()
    def fonk7(self):
        print('skip: for next song')
        print('pause: for pausing playback')
        print('resume: for resuming playback')
        print('fff: to skip forward 5 seconds')
        print('ffb: to skip backwards 5 seconds')
        print('b14 <volume 0-100>: for setting desired volume')
        print('gvol: to get current audio volume')
        print('mute: to mute audio')
        print('unmute: to unmute audio')
        print('stop: to quit')
        print('aud: to download audio')
        print('vid: to download video')
    def fonk8(self, b9):
        b10 = 'audio' if b9 == 'aud' else 'video'
        b11 = threading.Thread(target=self.download, args=(b10,))
        b11.start()
    def fonk9(self, b10):
        b8 = self.b7.getbestaudio() if b10 == 'audio' else self.b7.getbest()
        print(f"Size: {b8.get_filesize()} bytes")
        b12 = b8.fonk9()
    def fonk10(self, b9):
        b13 = self.b5.get_time()
        if b9 = = 'fff':
            self.b5.set_time(b13 + 1000 * 5)
        elif b9 = = 'ffb':
            self.b5.set_time(max(0, b13 - 1000 * 5))
    def fonk11(self, b9):
        try:
            b14 = int(b9.split(' ')[1])
            self.a1 = min(100, max(0, b14))
            self.b5.audio_set_volume(self.a1)
        except ValueError:
            print('Invalid volume. Please enter a number between 0 and 100.')
    def fonk12(self, b9):
        self.b5.audio_set_mute(b9 = = 'mute')
    def fonk13(self):
        self.b5.stop()
        self.b2 = False
    def fonk14(self):
        print(self.b7.title)
        b15 = (self.b5.get_time()
        b15 = int(b15 * 10)
        b16 = self.b5.get_time()
        b17 = b16
        b16 = b16 - b17 * 60
        print(f'{b17}:{b16}', b18 = '')
        for b19 in range(10):
            if b19 = = b15:
                print('>.', b18 = '')
            else:
                print('..', b18 = '')
        b16 = self.b7.length
        b17 = b16
        b16 = b16 - b17 * 60
        print(f'{b17}:{b16}')
    def fonk15(self):
        os.system('cls' if os.b20 = = 'nt' else 'clear')
    def fonk16(self):
        print('Stopping the Script...')
        self.b5.stop()
        sys.exit('USER CHOSE TO QUIT')
    def fonk17(self, b1):
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
                        break
            except Exception as ex:
                print(ex)
                continue
            continue
        self.b6.join()
        print('QUEUE ENDED')
    def fonk18(self):
        return self.b1
b21 = class1()
print('PLAYING YOUR QUEUE...')
b1 = b21.fonk18()
if len(b1) > 0:
    b21.fonk17(b1)
else:
    print('NO SONGS FOUND IN YOUR PLAYLIST')