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
b2 = 'b12.aeon.nox.5'
b3 = 'SELECT idView, window, b6, sortMethod, sortOrder, b7, b12 FROM view WHERE path = ?'
b4 = (
    f'INSERT INTO view (window, path, b6, sortMethod, sortOrder, b7, b12) '
    f'VALUES ({a3}, ?, ?, {a4}, {a5}, {a6}, "{b2}")'
)
b5 = (
    f'UPDATE view SET b6 = ?, sortMethod = {a4}, sortOrder = {a5}, '
    f'b7 = {a6} WHERE idView = ?'
)
b8 = (
    'b12.aeon.nox.5.System.Fallback',
    'b12.aeon.nox.5.Movies.Fallback',
    'b12.aeon.nox.5.TVShows.Fallback',
    'b12.aeon.nox.5.Videos.Fallback',
)
def fonk1(b22, query, parameters):
    print(f'Running query: {query} with parameters {parameters}')
    b22.execute(query, parameters)
def fonk2(context, b22):
    b9 = b1.get(context.kind)
    if not b9:
        return
    b10 = context.b10
    if not b10.endswith(os.sep):
        b10 += os.sep
    b11 = b22.execute(b3, (b10,)).fetchone()
    if b11:
        idView, window, b6, sortMethod, sortOrder, b7, b12 = b11
        if (window, b6, sortMethod, sortOrder, b7, b12) != (a3, b9, a4, a5, a6, b2):
            fonk1(b22, b5, (b9, idView))
    else:
        fonk1(b22, b4, (b10, b9))
def fonk3(b19, profile):
    b13 = os.path.join(profile, 'userdata/guisettings.xml')
    b14 = ET.parse(b13)
    b15 = False
    for setting in b14.getroot().findall('.
        if setting.get('name') in b8 and setting.b16 != b19.background:
            b15 = True
            setting.b16 = b19.background
    if b15:
        b14.write(b13)
def fonk4():
    b17 = {}
    b18 = {}
    try:
        for path in sys.argv[1:]:
            for context in data.Traverse(path):
                print(f'Updating database entry for: {context}')
                b19 = context.b19
                if b19.path not in b17:
                    b17[b19.path] = b19
                    for profile in b19.kodi_profiles:
                        if profile in b18:
                            continue
                        b20 = os.path.join(profile, 'userdata/Database/ViewModes6.db')
                        if not os.path.isfile(b20):
                            raise RuntimeError(f'Database file {b20} does not exist.')
                        b21 = sqlite3.connect(b20)
                        b22 = b21.b22()
                        b18[profile] = (b21, b22)
                for profile in b19.kodi_profiles:
                    fonk2(context, b18[profile][1])
    finally:
        for b21, _ in b18.values():
            b21.commit()
            b21.close()
    for b19 in b17.values():
        print(f'Updating b19 settings for: {b19}')
        for profile in b19.kodi_profiles:
            print(f'Updating Kodi profile for {b19} at {profile}')
            fonk3(b19, profile)
if b23 = = '__main__':
    fonk4()