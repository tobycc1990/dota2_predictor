#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
get match data in last 30 day from steam dota2api

Authors: tobycc1990@gmail.com
Date: 2018-01-11 15:26:37
"""

CONFIG_PATH = "./../../conf"

# spider result will save in DATA_PATH 
DATA_PATH = "./../../data"

import sys
import os
import time
import datetime
sys.path.append(CONFIG_PATH)

import spider_config

# if you don't have dota2api lib
# please install with 'pip install dota2api'
# refer: http://dota2api.readthedocs.io/en/latest/installation.html
import dota2api

if __name__ == "__main__":
    api = dota2api.Initialise(spider_config.steam_web_api_key)
    
    # get 30 day before date
    today = datetime.date.today()
    delta_days = datetime.timedelta(days = 2)
    dueday = today - delta_days
    # get timestamp
    dueday_timestamp = time.mktime(dueday.timetuple())

    # get latest match
    latest_match = api.get_match_history(matches_request = 1)
    latest_match = latest_match["matches"][0]
    latest_match_id = latest_match["match_id"]
    latest_match_start_time_ts = latest_match["start_time"]
    
    iter_match_id = latest_match_id
    iter_timestamp = latest_match_start_time_ts
    while (iter_timestamp > dueday_timestamp):
        match_lists = api.get_match_history(start_at_match_id = iter_match_id)
        if match_lists["status"] != 1 or len(match_lists["matches"]) <= 0:
            break
        for each_match in match_lists["matches"]:
            each_match_id = each_match["match_id"]
            each_match_start_time = datetime.datetime.fromtimestamp(each_match["start_time"])
            print each_match_id, each_match_start_time
            print each_match
        iter_timestamp = match_lists["matches"][-1]["start_time"]
        iter_match_id = match_lists["matches"][-1]["match_id"]
