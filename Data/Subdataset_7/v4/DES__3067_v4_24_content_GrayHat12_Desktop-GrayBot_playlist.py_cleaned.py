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
        self.b4 = vlc.Instance('--input-repeat=-1', '--fullscreen', '--mouse-hide-timeout=0')
        self.b5 = self.b4.media_player_new()
        self.b1 = grayp.GetQueue().get()
        self.b6 = threading.Thread(target=self.handleOptions)
    def fonk2(self, volume):
        self.a1 = volume
    def fonk3(self, link):
        b7 = pafy.new(link)
        self.b8 = b7
        self.b9 = self.b4.media_new(b7.getbestaudio().url)
        self.b9.get_mrl()
    def fonk4(self):
        return self.a1
    def fonk5(self):
        while True:
            b10 = input('...> ')
            if b10 = = 'pause':
                self.b5.set_pause(1)
            elif b10 = = 'help':
                self.fonk6()
            elif b10 = = 'resume':
                self.b5.set_pause(0)
            elif b10 in ('aud', 'vid'):
                self.fonk7(b10)
            elif b10 in ('fff', 'ffb'):
                self.fonk9(b10)
            elif b10.startswith('vol'):
                self.fonk2(int(b10.split(' ')[1]))
                self.b5.audio_set_volume(self.a1)
            elif b10 = = 'gvol':
                print(self.b5.audio_get_volume())
            elif b10 in ('mute', 'unmute'):
                self.b5.audio_set_mute(b10 = = 'mute')
            elif b10 = = 'skip':
                self.fonk10()
            elif b10 = = 'info':
                self.fonk11()
            elif b10 = = 'clr':
                self.fonk12()
            elif b10 = = 'stop':
                self.fonk13()
    def fonk6(self):
        print('skip: for next song')
        print('pause: for pausing playback')
        print('resume: for resuming playback')
        print('fff: to skip forward 5 b18')
        print('ffb: to skip backwards 5 b18')
        print('vol <volume 0-100>: for setting desired volume')
        print('gvol: to get current audio volume')
        print('mute: to mute audio')
        print('unmute: to unmute audio')
        print('stop: to quit')
        print('aud: to download audio')
        print('vid: to download video')
    def fonk7(self, media_type):
        b11 = threading.Thread(target=self.download, args=(media_type,))
        b11.start()
    def fonk8(self, media_type):
        b7 = self.b8.getbestaudio() if media_type == 'aud' else self.b8.getbest()
        print(f"Size: {b7.get_filesize()} bytes")
        b12 = b7.fonk8()
    def fonk9(self, b14):
        b13 = self.b5.get_time()
        if b14 = = 'fff':
            self.b5.set_time(b13 + 1000 * 5)
        elif b14 = = 'ffb':
            self.b5.set_time(max(0, b13 - 1000 * 5))
    def fonk10(self):
        self.b5.stop()
        self.b2 = False
    def fonk11(self):
        print(self.b8.title)
        b15 = (self.b5.get_time()
        b15 = int(b15 * 10)
        b16 = self.b5.get_time()
        b17 = b16
        b18 = b16 - b17 * 60
        print(f'{b17}:{b18}', b19 = '')
        for b20 in range(10):
            if b20 = = b15:
                print('>.', b19 = '')
            else:
                print('..', b19 = '')
        b21 = self.b8.length
        b22 = b21
        b18 = b21 - b22 * 60
        print(f'{b22}:{b18}')
    def fonk12(self):
        os.system('cls' if os.b23 = = 'nt' else 'clear')
    def fonk13(self):
        print('Stopping the Script...')
        self.b5.stop()
        sys.exit('USER CHOSE TO QUIT')
    def fonk14(self):
        self.b3 = True
        print('help for CONTROLS')
        self.b6.start()
        for song in self.b1:
            try:
                self.fonk3(song)
                print('CURRENTLY PLAYING : ',)
                print(self.b8)
                print('FROM YOUR FAVORITE ARTISTS')
                self.b5.set_media(self.b9)
                self.b5.audio_set_volume(self.fonk4())
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
    def fonk15(self):
        return self.b1
b5 = class1()
print('PLAYING YOUR QUEUE...')
b24 = b5.fonk15()
if len(b24) > 0:
    b5.fonk14(b24)
else:
    print('NO SONGS FOUND IN YOUR PLAYLIST')