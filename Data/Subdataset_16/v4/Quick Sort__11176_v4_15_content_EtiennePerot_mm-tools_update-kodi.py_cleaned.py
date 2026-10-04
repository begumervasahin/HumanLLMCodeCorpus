import os
import sys
import sqlite3
import xml.etree.ElementTree as ET
import data
a1 = 66037
a2 = 458808
b1 = {
    data.Context.KIND_SERIES: a2,
    data.Context.KIND_SEASON: a1,
    data.Context.KIND_MOVIE: a1,
    data.Context.KIND_OVA: a1,
}
a3 = 10025
a4 = 4
a5 = 1
a6 = 0
b2 = 'b10.aeon.nox.5'
b3 = 'SELECT idView, window, viewMode, sortMethod, sortOrder, sortAttributes, b10 FROM view WHERE path = ?'
b4 = f'INSERT INTO view (window, path, viewMode, sortMethod, sortOrder, sortAttributes, b10) VALUES({a3}, ?, ?, {a4}, {a5}, {a6}, "{b2}")'
b5 = f'UPDATE view SET viewMode = ?, sortMethod = {a4}, sortOrder = {a5}, sortAttributes = {a6} WHERE idView = ?'
b6 = (
    'b10.aeon.nox.5.System.Fallback',
    'b10.aeon.nox.5.Movies.Fallback',
    'b10.aeon.nox.5.TVShows.Fallback',
    'b10.aeon.nox.5.Videos.Fallback',
)
def fonk1(b21, query, parameters):
    print(f'Running query: {query} with parameters {parameters}')
    b21.execute(query, parameters)
def fonk2(context, b21):
    b7 = b1.get(context.kind)
    if not b7:
        return
    b8 = context.b8
    if not b8.endswith(os.sep):
        b8 += os.sep
    b9 = b21.execute(b3, (b8,)).fetchone()
    if b9:
        idView, window, viewMode, sortMethod, sortOrder, sortAttributes, b10 = b9
        if (window, viewMode, sortMethod, sortOrder, sortAttributes, b10) != (a3, b7, a4, a5, a6, b2):
            fonk1(b21, b5, (b7, idView))
    else:
        fonk1(b21, b4, (b8, b7))
def fonk3(b18, profile):
    b11 = os.path.join(profile, 'userdata/b11.xml')
    b12 = ET.parse(b11)
    b13 = False
    for setting in b12.getroot().findall('.
        if setting.get('name') in b6 and setting.b14 != b18.background:
            b13 = True
            setting.b14 = b18.background
    if b13:
        b12.write(b11)
if b15 = = '__main__':
    b16 = {}
    b17 = {}
    try:
        for path in sys.argv[1:]:
            for context in data.Traverse(path):
                print(f'Updating b19 entry for: {context}')
                b18 = context.b18
                if b18.path not in b16:
                    b16[b18.path] = b18
                    for profile in b18.kodi_profiles:
                        if profile in b17:
                            continue
                        b19 = os.path.join(profile, 'userdata/Database/ViewModes6.db')
                        if not os.path.isfile(b19):
                            raise RuntimeError(f'Database file {b19} does not exist.')
                        b20 = sqlite3.connect(b19)
                        b21 = b20.b21()
                        b17[profile] = (b20, b21)
                for profile in b18.kodi_profiles:
                    fonk2(context, b17[profile][1])
    finally:
        for b20, _ in b17.values():
            b20.commit()
            b20.close()
    for b18 in b16.values():
        print(f'Updating b18 settings for: {b18}')
        for profile in b18.kodi_profiles:
            print(f'Updating Kodi profile for {b18} at {profile}')
            fonk3(b18, profile)