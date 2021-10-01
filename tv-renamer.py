import requests

def get_serch_results(name):
    results = requests.get(f'https://api.tvmaze.com/search/shows?q={name}').json()
    for res in results:
        series_id=res['show']['id']
        series_name=res['show']['name']
        print(f'{series_id} {series_name}')
    

def get_seasons(series_id):
    seasons=requests.get(f'https://api.tvmaze.com/shows/{series_id}/seasons').json()
    for season in seasons:
        season_id=season['id']
        season_num=season['number']
        num_of_episodes=season['episodeOrder']
        print(f'{season_id} {season_num} {num_of_episodes}')
        

def main():
    # get_serch_results('girls')
    get_seasons(23542)

if __name__ =="__main__":
    main()
