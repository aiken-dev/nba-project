from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats
from tabulate import tabulate 
from halo import Halo

from modules.find_players import find_player_id, find_player_full_name
from modules.calculate_stats import calculate_ppg, calculate_apg, calculate_rpg, calculate_3ptPCT, calculate_FGPCT

player1 = input("Enter first player full name: ")
player1_id = find_player_id(player1)

player2 = input("Enter second player full name: ")
player2_id = find_player_id(player2)

spinner = Halo(text="Comparing...", spinner="dots")
spinner.start()

player1_ppg = calculate_ppg(player1_id)
player2_ppg = calculate_ppg(player2_id)

player1_apg = calculate_apg(player1_id)
player2_apg = calculate_apg(player2_id)

player1_rpg = calculate_rpg(player1_id)
player2_rpg = calculate_rpg(player2_id)

player1_FG3_PCT = calculate_3ptPCT(player1_id)
player2_FG3_PCT = calculate_3ptPCT(player2_id)

player1_FG_PCT = calculate_FGPCT(player1_id)
player2_FG_PCT = calculate_FGPCT(player2_id)


player1_name = find_player_full_name(player1_id)
player2_name = find_player_full_name(player2_id)

spinner.succeed("Finished!")

if player2_ppg > player1_ppg:
    difference = round(player2_ppg - player1_ppg, 1)
    player2_ppg = f'{player2_ppg} (+{difference})'
elif player1_ppg > player2_ppg:
    difference = round(player1_ppg - player2_ppg, 1)
    player1_ppg = f'{player1_ppg} (+{difference})'

if player2_apg > player1_apg:
    difference = round(player2_apg - player1_apg, 1)
    player2_apg = f'{player2_apg} (+{difference})'
elif player1_apg > player2_apg:
    difference = round(player1_apg - player2_apg, 1)
    player1_apg = f'{player1_apg} (+{difference})'

if player2_rpg > player1_rpg:
    difference = round(player2_rpg - player1_rpg, 1)
    player2_rpg = f'{player2_rpg} (+{difference})'
elif player1_rpg > player2_rpg:
    difference = round(player1_rpg - player2_rpg, 1)
    player1_rpg = f'{player1_rpg} (+{difference})'

if player1_FG3_PCT > player2_FG3_PCT:
    difference = round(player1_FG3_PCT - player2_FG3_PCT, 1)
    player1_FG3_PCT = f'{player1_FG3_PCT} (+{difference})'
elif player2_FG3_PCT > player1_FG3_PCT:
    difference = round(player2_FG3_PCT - player1_FG3_PCT, 1)
    player2_FG3_PCT = f'{player2_FG3_PCT} (+{difference})'

if player1_FG_PCT > player2_FG_PCT:
    difference = round(player1_FG_PCT - player2_FG_PCT, 1)
    player1_FG_PCT = f'{player1_FG_PCT} (+{difference})'
elif player2_FG_PCT > player1_FG_PCT:
    difference = round(player2_FG_PCT - player1_FG_PCT, 1)
    player2_FG_PCT = f'{player2_FG_PCT} (+{difference})'


table_data = [  [player1_name, player2_name],
                ['PPG', player1_ppg, player2_ppg],
                ['APG', player1_apg, player2_apg],
                ['RPG', player1_rpg, player2_rpg],
                ['3PT%', player1_FG3_PCT, player2_FG3_PCT],
                ['FG%', player1_FG_PCT, player2_FG_PCT]
            ]

print(tabulate(table_data, headers="firstrow", tablefmt="fancy_grid"))
print("\n")

