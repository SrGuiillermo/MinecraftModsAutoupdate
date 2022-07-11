import json
import requests
import wget
import os


if __name__ == '__main__':
    
    try:
        with open('confg.json', 'r') as f:
            confg = json.load(f)
    except FileNotFoundError:
        confg = {
            'api_key' : '',
            'client' : [],
        }

        with open('confg.json', 'w') as f:
            json.dump(confg, f)

        print('Api key or Mods ids file not found. Please introduce your CurseForge API key and the ids of the mods in the created configuration file.')
        input()
        exit()


    mod_input = input('List of mods to download (Name of the list of mods in json confg file): ')

    headers = {
        'Accept': 'application/json',
        'x-api-key': confg['api_key'],
    }

    if not os.path.exists('./mods'):
        os.mkdir('./mods')

    download_links = [requests.get(f'https://api.curseforge.com/v1/mods/{i}/files/', headers= headers).json()['data'][0]['downloadUrl'] for i in confg[mod_input]]

    for i in download_links:
        wget.download(i, out='./mods')