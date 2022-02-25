import json
import pprint
from modules.getSummonerInfo.summoner_info import summoner_info
from modules.getData.getMatches import getMatches

nickname = input()
format_nickname = lambda nick : ''.join(nick.split()).lower()
formated_nickname = format_nickname(nickname)

config = open('../config.json')

congfig_json = json.load(config)

dev_key = congfig_json.get('dev_key')
start = congfig_json.get('match').get('start')
count = congfig_json.get('match').get('count')

config.close()

summonerInfo = summoner_info(formated_nickname, dev_key)

summonerInfo = summonerInfo.getSummoner()

matches = getMatches(summonerInfo, start, count, dev_key)

matchlist = matches.getMatchList()

pprint.pprint(matchlist)