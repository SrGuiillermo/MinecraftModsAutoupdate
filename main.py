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
            'mods_ids' : [],
        }

        with open('confg.json', 'w') as f:
            json.dump(confg, f)

        print('Api key or Mods ids file not found. Please introduce your CurseForge API key and the ids of the mods in the created configuration file.')
        input()
        exit()

    if len(list(confg.keys())) > 2:
        list_of_mods = list(confg.keys())
        del list_of_mods[0]
        
        print(f'More than one list of mods detected: {list_of_mods}')
        mod_input = input('Enter the list you want to download: ')
    else:
        mod_input = list(confg.keys())[-1]

    headers = {
        'Accept': 'application/json',
        'x-api-key': confg['api_key'],
    }

    if not os.path.exists('./mods'):
        os.mkdir('./mods')

    download_links = [requests.get(f'https://api.curseforge.com/v1/mods/{i}/files/', headers= headers).json()['data'][0]['downloadUrl'] for i in confg[mod_input]]

    for i in download_links:
        wget.download(i, out='./mods')