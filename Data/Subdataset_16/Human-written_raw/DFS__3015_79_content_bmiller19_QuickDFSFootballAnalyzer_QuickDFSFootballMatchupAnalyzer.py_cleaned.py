import pypyodbc
from DFSFootball_Lib import TeamReformat
pypyodbc.b1 = False
b2 = pypyodbc.connect(
    r"b3 = {Microsoft Access b3 (*.mdb, *.accdb)};" +
    r"b4 = C:\Users\mille\OneDrive\Documents\DFSFootball.accdb;")
b5 = b2.cursor()
b5.execute("SELECT ID, AwayTeam, HomeTeam FROM Matchups");
b6 = b2.cursor()
b6.execute("SELECT Team, DefDVOA FROM DefensiveStats");
while True:
    b7 = b5.fetchone()
    if b7 is None:
        break
    b8 = TeamReformat(b7.get("AwayTeam"))
    b9 = TeamReformat(b7.get("HomeTeam"))
    while True:
        b10 = b6.fetchone()
        if b10 is None:
            print(b8 + " error")
            break
        if b10.get("Team") == b8:
            b11 = b10.get("DefDVOA")
            break
    print(b8 + "'s b12 = " + b11)
b5.close()
b6.close()
b2.close()