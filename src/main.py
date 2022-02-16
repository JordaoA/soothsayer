import requests
import pprint

nickname = input()

format_nickname = lambda nick : ''.join(nick.split()).lower()

formated_nickname = format_nickname(nickname)

dev_key = 'RGAPI-b1d75b85-3e3e-404f-b44a-b6abd1c07272'

url_get_name = f'https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{formated_nickname}?api_key={dev_key}'

response_somoner = requests.get(url_get_name)

puuid = response_somoner.json().get('puuid')

url_get_matchs = f'https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count=100&api_key={dev_key}'


response_matchs = requests.get(url_get_matchs)

matchs = response_matchs.json()

for match_id in matchs:    
    url_get_match = f'https://americas.api.riotgames.com/lol/match/v5/matches/{match_id}?api_key={dev_key}'
    response_match = requests.get(url_get_match)
    participants = response_match.json().get('metadata').get('participants')
    
    aliados_info = []
    inimigos_info = []
    
    team = 0
    add_team = lambda count: True if count <= 5 else False

    for puuid in participants:
        team+=1
        
        url_get_puuid = f'https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{puuid}?api_key={dev_key}'
        
        response_puuid = requests.get(url_get_puuid)
        name = response_puuid.json().get('name')
        #level = response_puuid.json().get('summonerLevel')
        
        if add_team(team): aliados_info.append(name)
        
        else: inimigos_info.append(name)
    
    print(f'Aliados: {aliados_info}')
    print(f'Inimigos: {inimigos_info}')
    print()