import os
import sys
import sqlite3
import xml.etree.ElementTree as ET
class class1:
    b1 = "series"
    b2 = "season"
    b3 = "movie"
    b4 = "ova"
    def fonk1(self, b5, b6, b7):
        self.b5 = b5
        self.b6 = b6
        self.b7 = b7
class class2:
    def fonk2(self, b8, b9, b10):
        self.b8 = b8
        self.b9 = b9
        self.b10 = b10
def fonk3(b29, query, parameters):
    print('Running query: %r with parameters %r' % (query, parameters))
    b29.execute(query, parameters)
def fonk4(context, b29):
    b11 = b21.get(context.b5)
    if not b11:
        return
    b6 = context.b6
    if not b6.endswith(os.sep):
        b6 += os.sep
    b12 = b29.execute(b23, (b6,)).fetchone()
    if b12:
        idView, window, viewMode, sortMethod, sortOrder, sortAttributes, b13 = b12
        if (window, viewMode, sortMethod, sortOrder, sortAttributes, b13) != (a1, b11, a2, a3, a4, b22):
            fonk3(b29, b25, (b11, idView))
    else:
        fonk3(b29, b24, (b6, b11))
def fonk5(b7, profile):
    b14 = os.b8.join(profile, 'userdata/b14.xml')
    b15 = ET.parse(b14)
    b16 = False
    for setting in b15.getroot().findall('.
        if setting.get('name') in b26 and setting.b17 != b7.b10:
            b16 = True
            setting.b17 = b7.b10
    if b16:
        b15.write(b14)
if b18 = = '__main__':
    b19 = {}
    b20 = {}
    b21 = {
        class1.b1: 458808,
        class1.b2: 66037,
        class1.b3: 66037,
        class1.b4: 66037,
    }
    a1 = 10025
    a2 = 4
    a3 = 1
    a4 = 0
    b22 = 'b13.aeon.nox.5'
    b23 = 'SELECT idView, window, viewMode, sortMethod, sortOrder, sortAttributes, b13 FROM view WHERE b8 = ?'
    b24 = 'INSERT INTO view (window, b8, viewMode, sortMethod, sortOrder, sortAttributes, b13) VALUES(%d, ?, ?, %d, %d, %d, %r)' % (a1, a2, a3, a4, b22)
    b25 = 'UPDATE view SET viewMode = ?, sortMethod = %d, sortOrder = %d, sortAttributes = %d WHERE idView = ?' % (a2, a3, a4)
    b26 = (
        'b13.aeon.nox.5.System.Fallback',
        'b13.aeon.nox.5.Movies.Fallback',
        'b13.aeon.nox.5.TVShows.Fallback',
        'b13.aeon.nox.5.Videos.Fallback',
    )
    try:
        for b8 in sys.argv[1:]:
            for context in data.Traverse(b8):
                print('Updating b27 entry for:', context)
                b7 = context.b7
                if b7.b8 not in b19:
                    b19[b7.b8] = b7
                    for profile in b7.b9:
                        if profile in b20:
                            continue
                        b27 = os.b8.join(profile, 'userdata/Database/ViewModes6.db')
                        if not os.b8.isfile(b27):
                            raise RuntimeError('Database file %r does not exist.' % (b27,))
                        b28 = sqlite3.connect(b27)
                        b29 = b28.b29()
                        b20[profile] = (b28, b29)
                for profile in b7.b9:
                    fonk4(context, b20[profile][1])
    finally:
        for b28, _ in b20.values():
            b28.commit()
            b28.close()
    for b7 in b19.values():
        print('Updating b7 settings for:', b7)
        for profile in b7.b9:
            print('Updating Kodi profile for', b7, 'at', profile)
            fonk5(b7, profile)