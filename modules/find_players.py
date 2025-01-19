from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats

def find_player_id(player_name):
    matching_players = players.find_players_by_full_name(player_name)
    if not matching_players:
        matching_players = players.find_players_by_last_name(player_name)
        if not matching_players:
            matching_players = players.find_players_by_first_name(player_name)
    if not matching_players:
        raise ValueError(f"{player_name} not found")
    player_id = matching_players[0]['id']
    return player_id

def find_player_full_name(player_id):
    player_list = players.get_players()
    for player in player_list:
        if player['id'] == player_id:
            player_full_name = player['full_name']
    return player_full_name