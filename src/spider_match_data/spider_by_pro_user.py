#!/usr/bin/python
# -*- coding: utf-8 -*-
CONFIG_PATH = "./../../conf"

# spider result will save in DATA_PATH 
DATA_PATH = "./../../data"

import sys
import os
import time
import datetime
sys.path.append(CONFIG_PATH)

import requests

import spider_config

if __name__ == "__main__":
    pro_players = requests.get("https://api.opendota.com/api/proPlayers", verify = False).json()
    print len(pro_players)
    print pro_players[0]
    for each_player in pro_players:
        account_id = each_player["account_id"]
        name = each_player["name"]
        player_name = each_player["personaname"]
        if name != None:
            name = name.encode('utf8')
        if player_name != None:
            player_name = player_name.encode('utf8')
        print "%s\t\t\t%s\t\t\t%s" % (account_id, name, player_name)
    
