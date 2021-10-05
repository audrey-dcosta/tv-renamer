from tkinter import filedialog
import os
import sys
import requests
import re

def clean_str(strg):
    cleaned_str=re.sub(r'[\\/*?<>|]',"",strg)
    cleaned_str=re.sub(r'[:]',"-",cleaned_str)
    cleaned_str=re.sub(r'["]',"'",cleaned_str)
    return cleaned_str

def get_search_results(name,seriesList,lb):
    results = requests.get(f'https://api.tvmaze.com/search/shows?q={name}').json()
    if results:
        try:
            for res in results:
                series_id=res['show']['id']
                series_title=res['show']['name']
                series_premiered=res['show']['premiered']
                series_name=f'{series_title} ({series_premiered})'
                print(f'{series_id} {series_title}({series_premiered})')
                seriesList.append({'series_id':series_id,'series_name':series_name})
                lb.insert('end',series_name)
            print(seriesList[2]['series_id'])
        except Exception as e:
            print(e)
        return

def get_seasons(series_id,seasonList,lb):
    # series_id=seriesList[lb.curselection()[0]]['series_id']
    seasons=requests.get(f'https://api.tvmaze.com/shows/{series_id}/seasons').json()
    series_name=requests.get(f'https://api.tvmaze.com/shows/{series_id}').json()['name']
    print(series_name)
    lb.delete(0,'end')
    for season in seasons:
        season_id=season['id']
        season_num=season['number']
        num_of_episodes=season['episodeOrder']
        print(f'{season_id} {season_num} {num_of_episodes}')
        season_title=f'Season {season_num} (eps: {num_of_episodes})'
        season_name=f'{series_name} S{season_num:02d}'
        seasonList.append({'season_id':season_id,'season_title':season_title,'series_name':series_name,'season_name':season_name})
        lb.insert('end',f'{season_name} (eps: {num_of_episodes})')
    return True

def get_episodes(season_id,episodeList,series_name,lb,season_name):
    try:
        episodes=requests.get(f'https://api.tvmaze.com/seasons/{season_id}/episodes').json()
        lb.delete(0,'end')
        for episode in episodes:
            episode_id=episode['id']
            episode_num=episode['number']
            season_num=episode['season']
            episode_title=clean_str(episode['name'])
            episode_name=f'{series_name} [{season_num}x{episode_num:02d}]{episode_title}'
            print(f'[{season_num}x{episode_num:02d}] {episode_name}')
            episodeList.append({'episode_name':episode_name,'season_name':season_name})
            lb.insert('end',episode_name)
        return True
    except Exception as e:
        print(e)
        return False













    
    