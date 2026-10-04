import pypyodbc
from DFSFootball_Lib import TeamReformat
def fonk1(team_name, b7):
    while True:
        b1 = b7.fetchone()
        if b1 is None:
            return 'error'
        if b1.get("Team") == team_name:
            return b1.get("DefDVOA")
def fonk2():
    pypyodbc.b2 = False
    b3 = pypyodbc.connect(
        r"b4 = {Microsoft Access b4 (*.mdb, *.accdb)};" +
        r"b5 = C:\Users\mille\OneDrive\Documents\DFSFootball.accdb;"
    )
    b6 = b3.cursor()
    b7 = b3.cursor()
    b6.execute("SELECT ID, AwayTeam, HomeTeam FROM Matchups")
    b7.execute("SELECT Team, DefDVOA FROM DefensiveStats")
    while True:
        b8 = b6.fetchone()
        if b8 is None:
            break
        b9 = TeamReformat(b8.get("AwayTeam"))
        b10 = TeamReformat(b8.get("HomeTeam"))
        b11 = fonk1(b9, b7)
        print(f"{b9}'s b12 = {b11}")
    b6.close()
    b7.close()
    b3.close()
if b13 = = "__main__":
    fonk2()