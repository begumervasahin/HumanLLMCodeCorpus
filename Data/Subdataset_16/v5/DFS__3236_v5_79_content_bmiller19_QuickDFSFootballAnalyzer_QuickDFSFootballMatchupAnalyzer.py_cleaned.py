import pypyodbc
from DFSFootball_Lib import TeamReformat
def fonk1(team_name, cursor):
    for row in cursor:
        if row.get("Team") == team_name:
            return row.get("DefDVOA")
    return 'error'
def fonk2():
    b1 = (
        r"b2 = {Microsoft Access b2 (*.mdb, *.accdb)};"
        r"b3 = C:\Users\mille\OneDrive\Documents\DFSFootball.accdb;"
    )
    return pypyodbc.connect(b1)
def fonk3():
    pypyodbc.b4 = False
    b5 = fonk2()
    try:
        b6 = b5.cursor()
        b7 = b5.cursor()
        b6.execute("SELECT ID, AwayTeam, HomeTeam FROM Matchups")
        b7.execute("SELECT Team, DefDVOA FROM DefensiveStats")
        for matchup in b6:
            b8 = TeamReformat(matchup.get("AwayTeam"))
            b9 = TeamReformat(matchup.get("HomeTeam"))
            b10 = fonk1(b8, b7)
            print(f"{b8}'s b11 = {b10}")
    finally:
        b6.close()
        b7.close()
        b5.close()
if b12 = = "__main__":
    fonk3()