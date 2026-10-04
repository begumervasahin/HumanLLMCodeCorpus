import pypyodbc
from DFSFootball_Lib import TeamReformat
def get_defensive_dvoa(team_name, cursor):
    while True:
        row = cursor.fetchone()
        if row is None:
            return 'error'
        if row.get("Team") == team_name:
            return row.get("DefDVOA")
def setup_database_connection(db_path):
    connection_string = (
        r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};"
        f"Dbq={db_path};"
    )
    return pypyodbc.connect(connection_string)
def main():
    db_path = r"C:\Users\mille\OneDrive\Documents\DFSFootball.accdb"
    pypyodbc.lowercase = False
    conn = setup_database_connection(db_path)
    with conn.cursor() as matchups_cursor, conn.cursor() as def_stats_cursor:
        matchups_cursor.execute("SELECT ID, AwayTeam, HomeTeam FROM Matchups")
        def_stats_cursor.execute("SELECT Team, DefDVOA FROM DefensiveStats")
        for matchup in matchups_cursor:
            away_team = TeamReformat(matchup.get("AwayTeam"))
            home_team = TeamReformat(matchup.get("HomeTeam"))
            away_dvoa = get_defensive_dvoa(away_team, def_stats_cursor)
            print(f"{away_team}'s DVOA = {away_dvoa}")
    conn.close()
if __name__ == "__main__":
    main()