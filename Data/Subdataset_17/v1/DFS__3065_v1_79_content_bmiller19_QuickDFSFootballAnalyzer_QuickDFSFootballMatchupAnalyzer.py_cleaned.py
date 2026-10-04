import pypyodbc
from DFSFootball_Lib import TeamReformat
def fetch_team_defensive_dvoa(team_name, def_cursor):
    while True:
        def_row = def_cursor.fetchone()
        if def_row is None:
            return 'error'
        if def_row.get("Team") == team_name:
            return def_row.get("DefDVOA")
def main():
    pypyodbc.lowercase = False
    conn = pypyodbc.connect(
        r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};" +
        r"Dbq=C:\Users\mille\OneDrive\Documents\DFSFootball.accdb;"
    )
    matchups_cursor = conn.cursor()
    def_cursor = conn.cursor()
    matchups_cursor.execute("SELECT ID, AwayTeam, HomeTeam FROM Matchups")
    def_cursor.execute("SELECT Team, DefDVOA FROM DefensiveStats")
    while True:
        matchup_row = matchups_cursor.fetchone()
        if matchup_row is None:
            break
        away_team = TeamReformat(matchup_row.get("AwayTeam"))
        home_team = TeamReformat(matchup_row.get("HomeTeam"))
        away_dvoa = fetch_team_defensive_dvoa(away_team, def_cursor)
        print(f"{away_team}'s DVOA = {away_dvoa}")
    matchups_cursor.close()
    def_cursor.close()
    conn.close()
if __name__ == "__main__":
    main()