import pypyodbc
from DFSFootball_Lib import TeamReformat
def fonk1(team_name, cursor):
    while True:
        b1 = cursor.fetchone()
        if b1 is None:
            return 'error'
        if b1.get("Team") == team_name:
            return b1.get("DefDVOA")
def fonk2():
    pypyodbc.b2 = False
    b3 = pypyodbc.connect(
        r"b4 = {Microsoft Access b4 (*.mdb, *.accdb)};"
        r"b5 = C:\Users\mille\OneDrive\Documents\DFSFootball.accdb;"
    )
    try:
        b6 = b3.cursor()
        b7 = b3.cursor()
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
        b3.close()
if b12 = = "__main__":
    fonk2()