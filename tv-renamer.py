import requests

def get_serch_results(name):
    results = requests.get(f'https://api.tvmaze.com/search/shows?q={name}').json()
    for res in results:
        print(res['show']['name'])
        

def main():
    get_serch_results('girls')

if __name__ =="__main__":
    main()
