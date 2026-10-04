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
b4 = 'INSERT INTO view (window, path, viewMode, sortMethod, sortOrder, sortAttributes, b10) VALUES(?, ?, ?, ?, ?, ?, ?)'
b5 = 'UPDATE view SET viewMode = ?, sortMethod = ?, sortOrder = ?, sortAttributes = ? WHERE idView = ?'
b6 = (
    'b10.aeon.nox.5.System.Fallback',
    'b10.aeon.nox.5.Movies.Fallback',
    'b10.aeon.nox.5.TVShows.Fallback',
    'b10.aeon.nox.5.Videos.Fallback',
)
def fonk1(b20, query, parameters):
    print(f'Running query: {query} with parameters {parameters}')
    b20.execute(query, parameters)
def fonk2(context, b20):
    b7 = b1.get(context.kind)
    if not b7:
        return
    b8 = context.b8
    if not b8.endswith(os.sep):
        b8 += os.sep
    b9 = b20.execute(b3, (b8,)).fetchone()
    if b9:
        idView, window, viewMode, sortMethod, sortOrder, sortAttributes, b10 = b9
        if (window, viewMode, sortMethod, sortOrder, sortAttributes, b10) != (a3, b7, a4, a5, a6, b2):
            fonk1(b20, b5, (b7, a4, a5, a6, idView))
    else:
        fonk1(b20, b4, (a3, b8, b7, a4, a5, a6, b2))
def fonk3(b17, profile):
    b11 = os.path.join(profile, 'userdata/guisettings.xml')
    b12 = ET.parse(b11)
    b13 = False
    for setting in b12.getroot().findall('.
        if setting.get('name') in b6 and setting.b14 != b17.background:
            b13 = True
            setting.b14 = b17.background
    if b13:
        b12.write(b11)
def fonk4():
    b15 = {}
    b16 = {}
    try:
        for path in sys.argv[1:]:
            for context in data.Traverse(path):
                print(f'Updating database entry for: {context}')
                b17 = context.b17
                if b17.path not in b15:
                    b15[b17.path] = b17
                    for profile in b17.kodi_profiles:
                        if profile in b16:
                            continue
                        b18 = os.path.join(profile, 'userdata/Database/ViewModes6.db')
                        if not os.path.isfile(b18):
                            raise RuntimeError(f'Database file {b18} does not exist.')
                        b19 = sqlite3.connect(b18)
                        b20 = b19.b20()
                        b16[profile] = (b19, b20)
                for profile in b17.kodi_profiles:
                    fonk2(context, b16[profile][1])
    finally:
        for b19, _ in b16.values():
            b19.commit()
            b19.close()
    for b17 in b15.values():
        print(f'Updating b17 settings for: {b17}')
        for profile in b17.kodi_profiles:
            print(f'Updating Kodi profile for {b17} at {profile}')
            fonk3(b17, profile)
if b21 = = '__main__':
    fonk4()