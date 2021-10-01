import requests

def get_serch_results(name):
    results = requests.get(f'https://api.tvmaze.com/search/shows?q={name}').json()
    for res in results:
        series_id=res['show']['id']
        series_name=res['show']['name']
        series_premiered=res['show']['premiered']
        print(f'{series_id} {series_name}({series_premiered})')
    

def get_seasons(series_id):
    seasons=requests.get(f'https://api.tvmaze.com/shows/{series_id}/seasons').json()
    for season in seasons:
        season_id=season['id']
        season_num=season['number']
        num_of_episodes=season['episodeOrder']
        print(f'{season_id} {season_num} {num_of_episodes}')

def get_episodes(season_id):
    episodes=requests.get(f'https://api.tvmaze.com/seasons/{season_id}/episodes').json()
    for episode in episodes:
        episode_id=episode['id']
        episode_name=episode['name']
        print(f'{episode_id} {episode_name}')
        

def main():
    # get_serch_results('girls')
    # get_seasons(23542)
    get_episodes(109940)

if __name__ =="__main__":
    main()
