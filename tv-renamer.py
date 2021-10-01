import requests
import re

def get_serch_results(name):
    results = requests.get(f'https://api.tvmaze.com/search/shows?q={name}').json()
    for res in results:
        series_id=res['show']['id']
        series_name=res['show']['name']
        series_premiered=res['show']['premiered']
        print(f'{series_id} {series_name}({series_premiered})')
    

def get_seasons(series_id):
    seasons=requests.get(f'https://api.tvmaze.com/shows/{series_id}/seasons').json()
    series_name=requests.get(f'https://api.tvmaze.com/shows/{series_id}').json['name']
    for season in seasons:
        season_id=season['id']
        season_num=season['number']
        num_of_episodes=season['episodeOrder']
        print(f'{season_id} {season_num} {num_of_episodes}')

def get_episodes(season_id,series_name):
    episodes=requests.get(f'https://api.tvmaze.com/seasons/{season_id}/episodes').json()
    for episode in episodes:
        episode_id=episode['id']
        episode_num=episode['number']
        season_num=episode['season']
        episode_title=clean_str(episode['name'])
        episode_name(f'{series_name}[{season_num}x{episode_num:02d}] {episode_name}')
        print(f'{series_name}[{season_num}x{episode_num:02d}] {episode_name}')

def clean_str(strg):
    cleaned_str=re.sub(r'[\\/*?<>|]',"",strg)
    cleaned_str=re.sub(r'[:]',"-",cleaned_str)
    cleaned_str=re.sub(r'["]',"'",cleaned_str)
    return cleaned_str
        

def main():
    # get_serch_results('girls')
    # get_seasons(23542)
    # get_episodes(109940,'girls')

if __name__ =="__main__":
    main()
