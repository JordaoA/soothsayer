import requests
import json

#nickname = input()
#format_nickname = lambda nick : ''.join(nick.split()).lower()
#formated_nickname = format_nickname(nickname)

config = open('config.json')

congfig_json = json.load(config)

config.close()

dev_key = congfig_json.get('dev_key')

print(dev_key)