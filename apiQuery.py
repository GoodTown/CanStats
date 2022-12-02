import requests
import pandas as pd
import json
from pandas import json_normalize

def main():
    my_headers_hockey = {'Ocp-Apim-Subscription-Key' : '970ba2196f9141d490e8168e084507d4'}
    my_headers_soccer = {'Ocp-Apim-Subscription-Key' : '21957562d4484b5c89377c8bf145a311'}
    # response = requests.get('https://api.sportsdata.io/v3/nhl/stats/json/PlayerSeasonStats/2022', headers=my_headers_hockey)
    response = requests.get('https://api.sportsdata.io/v3/soccer/stats/json/PlayerSeasonStats/744', headers =my_headers_soccer)
    with open('soccer_player_season_2022.json', 'wb') as outf:
         outf.write(response.content)
    df = pd.read_json("soccer_player_season_2022.json",orient='records')
    print(df[['Name','ShotsOnGoal','Games']])

main()
