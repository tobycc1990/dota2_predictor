#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
get match data from steam dota2api

Authors: tobycc1990@gmail.com
Date: 2018-01-11 15:26:37
"""

CONFIG_PATH = "./../../conf"

# spider result will save in DATA_PATH 
DATA_PATH = "./../../data"

import sys
import os
sys.path.append(CONFIG_PATH)

import spider_config

# if you don't have dota2api lib
# please install with 'pip install dota2api'
# refer: http://dota2api.readthedocs.io/en/latest/installation.html
import dota2api

if __name__ == "__main__":
    api = dota2api.Initialise(spider_config.steam_web_api_key)
    heroes = api.get_heroes()
    print heroes
