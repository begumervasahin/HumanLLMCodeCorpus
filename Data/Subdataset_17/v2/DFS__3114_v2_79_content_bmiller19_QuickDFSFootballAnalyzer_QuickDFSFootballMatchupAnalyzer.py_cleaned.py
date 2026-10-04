import pypyodbc
from DFSFootball_Lib import TeamReformat
def get_defensive_dvoa(team_name, cursor):
    while True:
        row = cursor.fetchone()
        if row is None:
            return 'error'
        if row.get("Team") == team_name:
            return row.get("DefDVOA")
def main():
    pypyodbc.lowercase = False
    conn = pypyodbc.connect(
        r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};" +
        r"Dbq=C:\Users\mille\OneDrive\Documents\DFSFootball.accdb;"
    )
    matchups_cursor = conn.cursor()
    def_stats_cursor = conn.cursor()
    matchups_cursor.execute("SELECT ID, AwayTeam, HomeTeam FROM Matchups")
    def_stats_cursor.execute("SELECT Team, DefDVOA FROM DefensiveStats")
    while True:
        matchup = matchups_cursor.fetchone()
        if matchup is None:
            break
        away_team = TeamReformat(matchup.get("AwayTeam"))
        home_team = TeamReformat(matchup.get("HomeTeam"))
        away_dvoa = get_defensive_dvoa(away_team, def_stats_cursor)
        print(f"{away_team}'s DVOA = {away_dvoa}")
    matchups_cursor.close()
    def_stats_cursor.close()
    conn.close()
if __name__ == "__main__":
    main()