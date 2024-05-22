import FRScraper

# League table
df = FRScraper.get_rankings('ENG')

# League teams
df = FRScraper.get_rankings('ESP')

# Team's performance for the last 5 games for the entire league
df = FRScraper.get_last_scores_league('FRA', 5)

# Individual team's performance for the last 5 games
df = FRScraper.get_last_scores_team('ITA', 'Milan', 5)

# All league scores so far
df = FRScraper.get_all_scores('GER')

# Next 3 games for all teams in a league
df = FRScraper.get_next_games('ARG', 3)
