import pandas as pd
import numpy as np
import warnings

warnings.filterwarnings('ignore')

leagues = ['ENG','ESP','FRA','ITA','BRA','GER','HOL','ARG','POR','POL','KSA','RUS']

def get_url_teams(league):
    if league == 'ENG':
        url = 'https://fbref.com/en/comps/9/Premier-League-Stats'
    elif league == 'ESP':
        url = 'https://fbref.com/en/comps/12/La-Liga-Stats'
    elif league == 'FRA':
        url = 'https://fbref.com/en/comps/13/Ligue-1-Stats'
    elif league == 'ITA':
        url = 'https://fbref.com/en/comps/11/Serie-A-Stats'
    elif league == 'BRA':
        url = 'https://fbref.com/en/comps/24/Serie-A-Stats'
    elif league == 'GER':
        url = 'https://fbref.com/en/comps/20/Bundesliga-Stats'
    elif league == 'HOL':
        url = 'https://fbref.com/en/comps/23/Eredivisie-Stats'
    elif league == 'ARG':
        url = 'https://fbref.com/en/comps/21/Primera-Division-Stats'
    elif league == 'POR':
        url = 'https://fbref.com/en/comps/32/Primeira-Liga-Stats'
    elif league == 'POL':
        url = 'https://fbref.com/en/comps/36/Ekstraklasa-Stats'
    elif league == 'KSA':
        url = 'https://fbref.com/en/comps/70/Saudi-Professional-League-Stats'
    elif league == 'RUS':
        url = 'https://fbref.com/en/comps/30/Russian-Premier-League-Stats'
    else:
        raise ValueError(str(league)+' is not a valid parameter. Try one of: "'+'", "'.join(leagues)+'".')

    return url        
        
def get_rankings(league):

    url = get_url_teams(league)

    df = pd.read_html(url)[0]

    df['PCT'] = df['Pts']/(df['MP']*3)

    try:
        df = df[['Rk','Squad','MP','W','D','L','PCT','GF','GA','GD','Pts','Pts/MP',
                 'xG','xGA','xGD','xGD/90','Attendance','Top Team Scorer']]
    except:
        df = df[['Rk','Squad','MP','W','D','L','PCT','GF','GA','GD','Pts','Pts/MP',
                 'Attendance','Top Team Scorer']]

    df['Top Team Scorer'] = df['Top Team Scorer'].fillna('NaN - 0')
    
    df['Top Scorer Goals'] = df['Top Team Scorer'].str.split(' - ').str[1].astype(int)

    df = df.drop(columns=['Top Team Scorer'])

    return df

def get_teams(league):

    url = get_url_teams(league)

    df = pd.read_html(url)[0]

    df = df.sort_values('Squad')

    teams = sorted(list(df['Squad']))

    return teams

def get_url_scores(league):
    
    if league == 'ENG':
        url = 'https://fbref.com/en/comps/9/schedule/Premier-League-Scores-and-Fixtures'
    elif league == 'ESP':
        url = 'https://fbref.com/en/comps/12/schedule/La-Liga-Scores-and-Fixtures'
    elif league == 'FRA':
        url = 'https://fbref.com/en/comps/13/schedule/Ligue-1-Scores-and-Fixtures'
    elif league == 'ITA':
        url = 'https://fbref.com/en/comps/11/schedule/Serie-A-Scores-and-Fixtures'
    elif league == 'BRA':
        url = 'https://fbref.com/en/comps/24/schedule/Serie-A-Scores-and-Fixtures'
    elif league == 'GER':
        url = 'https://fbref.com/en/comps/20/schedule/Bundesliga-Scores-and-Fixtures'
    elif league == 'HOL':
        url = 'https://fbref.com/en/comps/23/schedule/Eredivisie-Scores-and-Fixtures'
    elif league == 'ARG':
        url = 'https://fbref.com/en/comps/21/schedule/Primera-Division-Scores-and-Fixtures'
    elif league == 'POR':
        url = 'https://fbref.com/en/comps/32/schedule/Primeira-Liga-Scores-and-Fixtures'
    elif league == 'POL':
        url = 'https://fbref.com/en/comps/36/schedule/Ekstraklasa-Scores-and-Fixtures'
    elif league == 'KSA':
        url = 'https://fbref.com/en/comps/70/schedule/Saudi-Professional-League-Scores-and-Fixtures'
    elif league == 'RUS':
        url = 'https://fbref.com/en/comps/30/schedule/Russian-Premier-League-Scores-and-Fixtures'
    else:
        raise ValueError(str(league)+' is not a valid parameter. Try one of: "'+'", "'.join(leagues)+'".')

    return url

def groupby_games(df, team, n_games):

    try:
        df = df.iloc[-n_games:]
    except:
        raise ValueError(str(n_games)+' is not a valid parameter. Try an integer number.')

    df['Goals_Home'] = df['Score'].str.split('–').str[0]
    df['Goals_Away'] = df['Score'].str.split('–').str[1]

    df['Squad'] = team

    df['H_or_A'] = np.where(df['Home']==df['Squad'],'Home','Away')

    df['Result'] = np.where(df['Goals_Home']>df['Goals_Away'],'Home','Away')
    df['Result'] = np.where(df['Goals_Home']==df['Goals_Away'],'Draw',df['Result'])
    
    df['Sum_W_'+str(n_games)] = np.where(df['Result']==df['H_or_A'], 1, 0)
    df['Sum_D_'+str(n_games)] = np.where(df['Result']=='Draw', 1, 0)
    df['Sum_L_'+str(n_games)] = np.where((df['Result']!=df['H_or_A'])&(df['Result']!='Draw'), 1, 0)

    df['Sum_GF_'+str(n_games)] = np.where(df['H_or_A']=='Home', df['Goals_Home'], df['Goals_Away']).astype(int)
    df['Sum_GA_'+str(n_games)] = np.where(df['H_or_A']=='Home', df['Goals_Away'], df['Goals_Home']).astype(int)

    df['Wk'] = df['Wk']+1

    df['Home_MP_'+str(n_games)] = np.where(df['H_or_A']=='Home',1,0)

    try:
        df['xG_H'] = np.where(df['Home']==df['Squad'], df['xG'], 0).astype(float)
        df['xG_A'] = np.where(df['Away']==df['Squad'], df['xG.1'], 0).astype(float)
        df['Sum_xG_'+str(n_games)] = df['xG_H'] + df['xG_A']    
    
        agg = df.groupby(['Squad']).agg({'Wk':'max',
                                         'Sum_GF_'+str(n_games):'sum',
                                         'Sum_GA_'+str(n_games):'sum',
                                         'Sum_xG_'+str(n_games):'sum',
                                         'Sum_W_'+str(n_games):'sum',
                                         'Sum_D_'+str(n_games):'sum',
                                         'Sum_L_'+str(n_games):'sum',
                                         'Home_MP_'+str(n_games):'sum'}).reset_index()

        agg['xG/MP_'+str(n_games)] = agg['Sum_xG_'+str(n_games)]/n_games
    except:
        agg = df.groupby(['Squad']).agg({'Wk':'max',
                                         'Sum_GF_'+str(n_games):'sum',
                                         'Sum_GA_'+str(n_games):'sum',
                                         'Sum_W_'+str(n_games):'sum',
                                         'Sum_D_'+str(n_games):'sum',
                                         'Sum_L_'+str(n_games):'sum',
                                         'Home_MP_'+str(n_games):'sum'}).reset_index()

    agg['GF/MP_'+str(n_games)] = agg['Sum_GF_'+str(n_games)]/n_games
    agg['GA/MP_'+str(n_games)] = agg['Sum_GA_'+str(n_games)]/n_games

    agg['PCT_'+str(n_games)] = ((agg['Sum_W_'+str(n_games)]*3)+(agg['Sum_D_'+str(n_games)]*1))/(n_games*3)

    return agg

def get_last_scores_league(league, n_games):

    scores = get_all_scores(league)

    teams = get_teams(league)

    base_f = pd.DataFrame()
    for team in teams:

        df = scores[(scores['Home']==team)|(scores['Away']==team)].reset_index(drop=True)

        if isinstance(n_games, list):

            base = pd.DataFrame()
        
            for n_game in n_games:

                apoio = groupby_games(df, team, n_game)

                if base.empty:
                    base = apoio
                else:
                    base = base.merge(apoio, on=['Squad','Wk'], how='left', validate='1:1')

        else:
            base = groupby_games(df, team, n_games)

        base_f = pd.concat([base_f,base], ignore_index=True)

    return base_f

def get_last_scores_team(league, team, n_games):

    df = get_all_scores(league)

    try:
        df = df[(df['Home']==team)|(df['Away']==team)].reset_index(drop=True)
    except:
        teams = get_teams(league)
        raise ValueError(str(team)+' is not a valid parameter. Try one of: "'+'", "'.join(teams)+'".')

    if df.empty:
        teams = get_teams(league)
        raise ValueError(str(team)+' is not a valid parameter. Try one of: "'+'", "'.join(teams)+'".')
    
    agg = groupby_games(df, team, n_games)

    return agg

def get_all_scores(league):

    try:
        url = get_url_scores(league)
    except:
        raise ValueError(str(league)+' is not a valid parameter. Try one of: "'+'", "'.join(leagues)+'".')

    df = pd.read_html(url)[0]

    df = df[df['Score'].notna()].reset_index(drop=True)

    df['Goals_Home'] = df['Score'].str.split('–').str[0]
    df['Goals_Away'] = df['Score'].str.split('–').str[1]

    df = df.rename(columns={'xG':'xG_Home','xG.1':'xG_Away'})

    df = df.drop(columns=['Match Report','Notes'])

    return df

def get_next_games(league, n=1):

    try:
        url = get_url_scores(league)
    except:
        raise ValueError(str(league)+' is not a valid parameter. Try one of: "'+'", "'.join(leagues)+'".')

    df = pd.read_html(url)[0]

    df = df[(df['Score'].isna())&(df['Wk'].notna())]
    df = df[df['Wk']==df['Wk'].iloc[0]+n-1].reset_index(drop=True)

    try:
        df = df.drop(columns=['Match Report','Notes','xG','xG.1','Score','Attendance','Referee'])
    except:
        df = df.drop(columns=['Match Report','Notes','Score','Attendance','Referee'])

    return df
   
