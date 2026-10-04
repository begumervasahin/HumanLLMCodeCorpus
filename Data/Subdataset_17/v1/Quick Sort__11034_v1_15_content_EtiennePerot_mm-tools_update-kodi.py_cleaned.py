import os
import sys
import sqlite3
import xml.etree.ElementTree as ET
import data
_VIEWMODE_LOW_LIST = 66037
_VIEWMODE_POSTERS = 458808
_VIEWMODE_MAPPING = {
    data.Context.KIND_SERIES: _VIEWMODE_POSTERS,
    data.Context.KIND_SEASON: _VIEWMODE_LOW_LIST,
    data.Context.KIND_MOVIE: _VIEWMODE_LOW_LIST,
    data.Context.KIND_OVA: _VIEWMODE_LOW_LIST,
}
_WINDOW = 10025
_SORT_METHOD = 4
_SORT_ORDER = 1
_SORT_ATTRIBUTES = 0
_SKIN = 'skin.aeon.nox.5'
_QUERY_SELECT = 'SELECT idView, window, viewMode, sortMethod, sortOrder, sortAttributes, skin FROM view WHERE path = ?'
_QUERY_INSERT = 'INSERT INTO view (window, path, viewMode, sortMethod, sortOrder, sortAttributes, skin) VALUES(?, ?, ?, ?, ?, ?, ?)'
_QUERY_UPDATE = 'UPDATE view SET viewMode = ?, sortMethod = ?, sortOrder = ?, sortAttributes = ? WHERE idView = ?'
_BACKGROUND_KEYS = (
    'skin.aeon.nox.5.System.Fallback',
    'skin.aeon.nox.5.Movies.Fallback',
    'skin.aeon.nox.5.TVShows.Fallback',
    'skin.aeon.nox.5.Videos.Fallback',
)
def _run_query(cursor, query, parameters):
    print('Running query: {} with parameters {}'.format(query, parameters))
    cursor.execute(query, parameters)
def update_database(context, cursor):
    mode = _VIEWMODE_MAPPING.get(context.kind)
    if not mode:
        return
    reflected_path = context.reflected_path
    if not reflected_path.endswith(os.sep):
        reflected_path += os.sep
    row = cursor.execute(_QUERY_SELECT, (reflected_path,)).fetchone()
    if row:
        idView, window, viewMode, sortMethod, sortOrder, sortAttributes, skin = row
        if (window, viewMode, sortMethod, sortOrder, sortAttributes, skin) != (_WINDOW, mode, _SORT_METHOD, _SORT_ORDER, _SORT_ATTRIBUTES, _SKIN):
            _run_query(cursor, _QUERY_UPDATE, (mode, _SORT_METHOD, _SORT_ORDER, _SORT_ATTRIBUTES, idView))
    else:
        _run_query(cursor, _QUERY_INSERT, (_WINDOW, reflected_path, mode, _SORT_METHOD, _SORT_ORDER, _SORT_ATTRIBUTES, _SKIN))
def update_kodi_profile(library, profile):
    guisettings = os.path.join(profile, 'userdata/guisettings.xml')
    tree = ET.parse(guisettings)
    changed = False
    for setting in tree.getroot().findall('.
        if setting.get('name') in _BACKGROUND_KEYS and setting.text != library.background:
            changed = True
            setting.text = library.background
    if changed:
        tree.write(guisettings)
if __name__ == '__main__':
    libraries = {}
    databases = {}
    try:
        for path in sys.argv[1:]:
            for context in data.Traverse(path):
                print('Updating database entry for:', context)
                library = context.library
                if library.path not in libraries:
                    libraries[library.path] = library
                    for profile in library.kodi_profiles:
                        if profile in databases:
                            continue
                        database = os.path.join(profile, 'userdata/Database/ViewModes6.db')
                        if not os.path.isfile(database):
                            raise RuntimeError('Database file {} does not exist.'.format(database))
                        conn = sqlite3.connect(database)
                        cursor = conn.cursor()
                        databases[profile] = (conn, cursor)
                for profile in library.kodi_profiles:
                    update_database(context, databases[profile][1])
    finally:
        for conn, _ in databases.values():
            conn.commit()
            conn.close()
    for library in libraries.values():
        print('Updating library settings for:', library)
        for profile in library.kodi_profiles:
            print('Updating Kodi profile for', library, 'at', profile)
            update_kodi_profile(library, profile)