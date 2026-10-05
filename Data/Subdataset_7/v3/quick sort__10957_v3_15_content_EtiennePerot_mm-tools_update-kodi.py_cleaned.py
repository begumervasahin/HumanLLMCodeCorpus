import os
import sys
import sqlite3
import xml.etree.ElementTree as ET
class class1:
    b1 = "series"
    b2 = "season"
    b3 = "movie"
    b4 = "ova"
class class2:
    def fonk1(self, b5, b6, b7):
        self.b5 = b5
        self.b6 = b6
        self.b7 = b7
b8 = {
    class1.b1: 458808,
    class1.b2: 66037,
    class1.b3: 66037,
    class1.b4: 66037,
}
a1 = 10025
a2 = 4
a3 = 1
a4 = 0
b9 = 'b17.aeon.nox.5'
b10 = 'SELECT idView, window, viewMode, sortMethod, sortOrder, sortAttributes, b17 FROM view WHERE b5 = ?'
b11 = f"INSERT INTO view (window, b5, viewMode, sortMethod, sortOrder, sortAttributes, b17) VALUES({a1}, ?, ?, {a2}, {a3}, {a4}, '{b9}')"
b12 = f"UPDATE view SET viewMode = ?, sortMethod = {a2}, sortOrder = {a3}, sortAttributes = {a4} WHERE idView = ?"
b13 = (
    'b17.aeon.nox.5.System.Fallback',
    'b17.aeon.nox.5.Movies.Fallback',
    'b17.aeon.nox.5.TVShows.Fallback',
    'b17.aeon.nox.5.Videos.Fallback',
)
def fonk2(b28, query, parameters):
    print(f'Running query: {query} with parameters {parameters}')
    b28.execute(query, parameters)
def fonk3(context, b28):
    b14 = b8.get(context.kind)
    if not b14:
        return
    b15 = context.b15
    if not b15.endswith(os.sep):
        b15 += os.sep
    b16 = b28.execute(b10, (b15,)).fetchone()
    if b16:
        idView, window, viewMode, sortMethod, sortOrder, sortAttributes, b17 = b16
        if (window, viewMode, sortMethod, sortOrder, sortAttributes, b17) != (a1, b14, a2, a3, a4, b9):
            fonk2(b28, b12, (b14, idView))
    else:
        fonk2(b28, b11, (b15, b14))
def fonk4(b25, profile):
    b18 = os.b5.join(profile, 'userdata/b18.xml')
    b19 = ET.parse(b18)
    b20 = False
    for setting in b19.getroot().findall('.
        if setting.get('name') in b13 and setting.b21 != b25.b7:
            b20 = True
            setting.b21 = b25.b7
    if b20:
        b19.write(b18)
if b22 = = '__main__':
    b23 = {}
    b24 = {}
    try:
        for b5 in sys.argv[1:]:
            for context in data.Traverse(b5):
                print('Updating b26 entry for:', context)
                b25 = context.b25
                if b25.b5 not in b23:
                    b23[b25.b5] = b25
                    for profile in b25.b6:
                        if profile in b24:
                            continue
                        b26 = os.b5.join(profile, 'userdata/Database/ViewModes6.db')
                        if not os.b5.isfile(b26):
                            raise RuntimeError(f'Database file {b26} does not exist.')
                        b27 = sqlite3.connect(b26)
                        b28 = b27.b28()
                        b24[profile] = (b27, b28)
                for profile in b25.b6:
                    fonk3(context, b24[profile][1])
    finally:
        for b27, _ in b24.values():
            b27.commit()
            b27.close()
    for b25 in b23.values():
        print('Updating b25 settings for:', b25)
        for profile in b25.b6:
            print('Updating Kodi profile for', b25, 'at', profile)
            fonk4(b25, profile)