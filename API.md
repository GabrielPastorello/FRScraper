# Documentation

For code examples, check the `examples.py` file.

**Importing:**
```
from FRScraper import FRScraper
```

**Functions:**
### `get_rankings(league)`
Gets the current ranking from a given league.

Parameters:
  - **`league`**: Desired league (one of `'ENG'`, `'ESP'`, `'FRA'`, `'ITA'`, `'BRA'`, `'POR'`, `'GER'`, `'HOL'`, `'ARG'`, `'POL'`, `'KSA'`, `'RUS'`).
  
### `get_teams(league)`
Gets the current teams from a given league.

Parameters:
  - **`league`**: Desired league (one of `'ENG'`, `'ESP'`, `'FRA'`, `'ITA'`, `'BRA'`, `'POR'`, `'GER'`, `'HOL'`, `'ARG'`, `'POL'`, `'KSA'`, `'RUS'`).

### `get_last_scores_league(league, n_games)`
Gets the performance for the last `n` games for all teams from the selected league.

Parameters:
  - **`league`**: Desired league (one of `'ENG'`, `'ESP'`, `'FRA'`, `'ITA'`, `'BRA'`, `'POR'`, `'GER'`, `'HOL'`, `'ARG'`, `'POL'`, `'KSA'`, `'RUS'`).
  - **`n_games`**: Number of games, integer.

### `get_last_scores_team(league, team, n_games)`
Gets the performance for the last `n` games for a particular team from the selected league.

Parameters:
  - **`league`**: Desired league (one of `'ENG'`, `'ESP'`, `'FRA'`, `'ITA'`, `'BRA'`, `'POR'`, `'GER'`, `'HOL'`, `'ARG'`, `'POL'`, `'KSA'`, `'RUS'`).
  - **`team`**: Desired team from the selected league.
  - **`n_games`**: Number of games, integer.

### `get_all_scores(league)`
Gets all scores so far from the current season from a given league.

Parameters:
  - **`league`**: Desired league (one of `'ENG'`, `'ESP'`, `'FRA'`, `'ITA'`, `'BRA'`, `'POR'`, `'GER'`, `'HOL'`, `'ARG'`, `'POL'`, `'KSA'`, `'RUS'`).

### `get_next_games(league, n)`
Gets the next `n` games for all teams from the selected league.

Parameters:
  - **`league`**: Desired league (one of `'ENG'`, `'ESP'`, `'FRA'`, `'ITA'`, `'BRA'`, `'POR'`, `'GER'`, `'HOL'`, `'ARG'`, `'POL'`, `'KSA'`, `'RUS'`).
  - **`n`**: Number of games, integer.
