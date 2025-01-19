from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats



def find_player_id(player_name):
    matching_players = players.find_players_by_full_name(player_name)
    player_id = matching_players[0]['id']
    return player_id

def find_player_full_name(player_id):
    player_list = players.get_players()
    for player in player_list:
        if player['id'] == player_id:
            player_full_name = player['full_name']
    return player_full_name

def calculate_ppg(player_id):
    player_career = playercareerstats.PlayerCareerStats(player_id)
    df = player_career.get_data_frames()[0]

    sumPoints = df['PTS'].sum()
    sumGames = df['GS'].sum() #gs means games
    ppg = round((sumPoints / sumGames), 1)

    return ppg

def calculate_apg(player_id):
    player_career = playercareerstats.PlayerCareerStats(player_id)
    df = player_career.get_data_frames()[0]

    sumAssists = df['AST'].sum()
    sumGames = df['GS'].sum() #gs means games
    apg = round((sumAssists / sumGames), 1)

    return apg

player1 = input("Enter first player full name: ")
player2 = input("Enter second player full name: ")



player1_id = find_player_id(player1)
player2_id = find_player_id(player2)

player1_ppg = calculate_ppg(player1_id)
player2_ppg = calculate_ppg(player2_id)

player1_apg = calculate_apg(player1_id)
player2_apg = calculate_apg(player2_id)

player1_name = find_player_full_name(player1_id)
player2_name = find_player_full_name(player2_id)

print("\n")
print(player1_name, "PPG:", player1_ppg)
print(player2_name, "PPG:", player2_ppg)

if player1_ppg > player2_ppg:
    print(player1_name, "has a higher PPG.")
elif player2_ppg > player1_ppg:
    print(player2_name, "has a higher PPG")
else:
    print("Both", player1_name, "and", player2_name, "have the same PPG")

print("\n")
print(player1_name, "APG:", player1_apg)
print(player2_name, "APG:", player2_apg)

if player1_apg > player2_apg:
    print(player1_name, "has a higher APG.")
elif player2_APG > player1_APG:
    print(player2_name, "has a higher APG")
else:
    print("Both", player1_name, "and", player2_name, "have the same APG")