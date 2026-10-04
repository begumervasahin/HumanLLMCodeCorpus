import pypyodbc
from DFSFootball_Lib import TeamReformat
def fonk1(team_name, cursor):
    while True:
        b1 = cursor.fetchone()
        if b1 is None:
            return 'error'
        if b1.get("Team") == team_name:
            return b1.get("DefDVOA")
def fonk2(b5):
    b2 = (
        r"b3 = {Microsoft Access b3 (*.mdb, *.accdb)};"
        f"b4 = {b5};"
    )
    return pypyodbc.connect(b2)
def fonk3():
    b5 = r"C:\Users\mille\OneDrive\Documents\DFSFootball.accdb"
    pypyodbc.b6 = False
    b7 = fonk2(b5)
    with b7.cursor() as matchups_cursor, b7.cursor() as def_stats_cursor:
        matchups_cursor.execute("SELECT ID, AwayTeam, HomeTeam FROM Matchups")
        def_stats_cursor.execute("SELECT Team, DefDVOA FROM DefensiveStats")
        for matchup in matchups_cursor:
            b8 = TeamReformat(matchup.get("AwayTeam"))
            b9 = TeamReformat(matchup.get("HomeTeam"))
            b10 = fonk1(b8, def_stats_cursor)
            print(f"{b8}'s b11 = {b10}")
    b7.close()
if b12 = = "__main__":
    fonk3()