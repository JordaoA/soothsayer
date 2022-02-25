import requests

"""
Codigo responsavel por coletar json's diretamente dos end points da API.
"""
class getMatches():

    def __init__(self, summoner_info, start, count, dev_key):
        self.puuid = summoner_info.puuid
        self.name = summoner_info.name
        self.start = start
        self.count = count
        self.dev_key = dev_key

    def getMatchList(self):
        matches_url = f'https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{self.puuid}/ids?start={self.start}&count={self.count}&api_key={self.dev_key}'
        match_ids = requests.get(matches_url)

        match_list = match_ids.json()

        return match_list
        