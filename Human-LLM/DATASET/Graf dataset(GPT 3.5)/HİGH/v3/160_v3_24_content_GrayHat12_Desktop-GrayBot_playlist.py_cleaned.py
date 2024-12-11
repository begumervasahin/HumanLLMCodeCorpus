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
        self.b3 = vlc.Instance('--input-repeat=-1', '--fullscreen', '--mouse-hide-timeout=0')
        self.b4 = self.b3.media_player_new()
        self.b5 = threading.Thread(target=self.handle_options)
    def fonk2(self, volume):
        self.a1 = volume
    def fonk3(self, link):
        b6 = pafy.new(link)
        self.b7 = b6
        self.fonk4(b6)
    def fonk4(self, b6):
        self.b8 = self.b3.media_new(b6.getbestaudio().url)
        self.b8.get_mrl()
    def fonk5(self):
        return self.a1
    def fonk6(self):
        while True:
            b9 = input('...> ')
            if b9 = = 'pause':
                self.b4.set_pause(1)
            elif b9 = = 'help':
                self.fonk7()
            elif b9 = = 'resume':
                self.b4.set_pause(0)
            elif b9 in ('aud', 'vid'):
                self.fonk8(b9)
            elif b9 in ('fff', 'ffb'):
                self.fonk10(b9)
            elif b9.startswith('vol'):
                self.fonk2(b9.split(' ')[1])
            elif b9 = = 'gvol':
                print(self.b4.audio_get_volume())
            elif b9 in ('mute', 'unmute'):
                self.fonk11(b9)
            elif b9 = = 'skip':
                self.fonk12()
            elif b9 = = 'info':
                self.fonk13()
            elif b9 = = 'clr':
                self.fonk14()
            elif b9 = = 'stop':
                self.fonk15()
    def fonk7(self):
        print('skip: for next song')
        print('pause: for pausing playback')
        print('resume: for resuming playback')
        print('fff: to skip forward 5 seconds')
        print('ffb: to skip backwards 5 seconds')
        print('vol <volume 0-100>: for setting desired volume')
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
        b13 = self.b4.get_time()
        if b9 = = 'fff':
            self.b4.set_time(b13 + 1000 * 5)
        elif b9 = = 'ffb':
            self.b4.set_time(max(0, b13 - 1000 * 5))
    def fonk11(self, b9):
        self.b4.audio_set_mute(b9 = = 'mute')
    def fonk12(self):
        self.b4.stop()
        self.b2 = False
    def fonk13(self):
        print(self.b7.title)
        b14 = (self.b4.get_time()
        b14 = int(b14 * 10)
        b15 = self.b4.get_time()
        b16 = b15
        b15 = b15 - b16 * 60
        print(f'{b16}:{b15}', b17 = '')
        for b18 in range(10):
            if b18 = = b14:
                print('>.', b17 = '')
            else:
                print('..', b17 = '')
        b19 = self.b7.length
        b20 = b19
        b19 = b19 - b20 * 60
        print(f'{b20}:{b19}')
    def fonk14(self):
        os.system('cls' if os.b21 = = 'nt' else 'clear')
    def fonk15(self):
        print('Stopping the Script...')
        self.b4.stop()
        sys.exit('USER CHOSE TO QUIT')
    def fonk16(self, b1):
        print('help for CONTROLS')
        self.b5.start()
        for link in self.b1:
            try:
                self.fonk3(link)
                print('CURRENTLY PLAYING : ')
                print(self.b7)
                print('FROM YOUR FAVORITE ARTISTS')
                self.b4.fonk4(self.b8)
                self.b4.audio_set_volume(self.fonk5())
                self.b4.play()
                self.b2 = True
                while self.b2:
                    if self.b4.get_state() == vlc.State.Ended:
                        self.b2 = False
                        self.b4.stop()
                        break
                    if not self.b5.isAlive():
                        self.b2 = False
                        sys.exit('USER CHOSE TO EXIT..\n' + 'Script might still wait for the download to finish...')
                        break
            except Exception as ex:
                print(ex)
                continue
            continue
        self.b5.join()
        print('QUEUE ENDED')
    def fonk17(self):
        return self.b1
b22 = class1()
print('PLAYING YOUR QUEUE...')
b1 = b22.fonk17()
if len(b1) > 0:
    b22.fonk16(b1)
else:
    print('NO SONGS FOUND IN YOUR PLAYLIST')