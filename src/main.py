import requests
import json
import pprint
from modules.getSummonerInfo.summoner_info import summoner_info

nickname = input()
format_nickname = lambda nick : ''.join(nick.split()).lower()
formated_nickname = format_nickname(nickname)

config = open('../config.json')

congfig_json = json.load(config)

config.close()

dev_key = congfig_json.get('dev_key')

summonerInfo = summoner_info(formated_nickname, dev_key)

summonerInfo = summonerInfo.getSummoner()

pprint.pprint(summonerInfo)