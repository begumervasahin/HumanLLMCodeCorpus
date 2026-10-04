import csv
import string
def get_player_list():
    filename = input('Enter filename (without .csv extension): ') + '.csv'
    player_list = []
    try:
        with open(filename, newline='') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                player = {
                    'FIRST': row[2],
                    'LAST': row[4],
                    'POS': row[1],
                    'PRICE': row[6],
                    'TEAM': row[9],
                    'OPP': row[10],
                    'INJ': row[11]
                }
                player_list.append(player)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except IndexError:
        print(f"Error: The file '{filename}' does not have the expected format.")
    return player_list
def trim_names(player_list):
    for player in player_list:
        player['FIRST'] = player['FIRST'].translate(str.maketrans('', '', string.punctuation))
        player['LAST'] = player['LAST'].translate(str.maketrans('', '', string.punctuation))
    return player_list
def main():
    players = get_player_list()
    if players:
        players = trim_names(players)
        for player in players:
            print(player)
if __name__ == "__main__":
    main()