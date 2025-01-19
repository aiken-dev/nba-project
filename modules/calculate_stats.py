from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats

def calculate_ppg(player_id):
    player_career = playercareerstats.PlayerCareerStats(player_id)
    df = player_career.get_data_frames()[0]

    sumPoints = df['PTS'].sum()
    sumGames = df['GP'].sum() #gs means games
    ppg = round((sumPoints / sumGames), 1)

    return float(ppg)

def calculate_apg(player_id):
    player_career = playercareerstats.PlayerCareerStats(player_id)
    df = player_career.get_data_frames()[0]

    sumAssists = df['AST'].sum()
    sumGames = df['GP'].sum() #gs means games
    apg = round((sumAssists / sumGames), 1)

    return float(apg)

def calculate_rpg(player_id):
    player_career = playercareerstats.PlayerCareerStats(player_id)
    df = player_career.get_data_frames()[0]

    sumRebounds = df['REB'].sum()
    sumGames = df['GP'].sum() #gs means games
    rpg = round((sumRebounds / sumGames), 1)

    return float(rpg)

def calculate_3ptPCT(player_id):
    player_career = playercareerstats.PlayerCareerStats(player_id)
    df = player_career.get_data_frames()[0]

    fg3_made = df['FG3M'].sum()
    fg3_attempts = df['FG3A'].sum()

    if fg3_attempts == 0:
        return 0.0
    
    FG3_PCT = (fg3_made / fg3_attempts) * 100
    return float(round(FG3_PCT, 1))

def calculate_3ptPCT(player_id):
    player_career = playercareerstats.PlayerCareerStats(player_id)
    df = player_career.get_data_frames()[0]

    fg3_made = df['FG3M'].sum()
    fg3_attempts = df['FG3A'].sum()
    
    FG3_PCT = (fg3_made / fg3_attempts) * 100
    return float(round(FG3_PCT, 1))

def calculate_FGPCT(player_id):
    player_career = playercareerstats.PlayerCareerStats(player_id)
    df = player_career.get_data_frames()[0]

    fg_made = df['FGM'].sum()
    fg_attempts = df['FGA'].sum()

    if fg_attempts == 0:
        return 0.0
        
    FG_PCT = (fg_made / fg_attempts) * 100
    return round(FG_PCT, 1)