import json
import requests
from modules.getSummonerInfo.summoner import Summoner

# Classe que coleta informações basicas sobre o user com base no nickname
class summoner_info:
    
    def __init__(self, summoner_name, dev_key):
        self.summoner_name = summoner_name
        self.dev_key = dev_key
    
    # Retorna DataClass com representação do Player, a partir do nickname
    def getSummoner(self): 
        summoner_info_url = f'https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{self.summoner_name}?api_key={self.dev_key}'
        summner_info = requests.get(summoner_info_url)

        summoner_id = summner_info.json().get('id')
        accountId = summner_info.json().get('accountId')
        puuid = summner_info.json().get('puuid')
        profileIconId = summner_info.json().get('profileIconId')
        summonerLevel = summner_info.json().get('summonerLevel')

        summoner_ = Summoner(summoner_id, self.summoner_name, 
                            accountId, puuid, profileIconId, summonerLevel)
        
        return(summoner_)