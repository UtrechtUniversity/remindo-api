import configparser

from collections import OrderedDict
import pandas as pd
from pandas.io.json import json_normalize
import os
import csv
import time
from datetime import datetime
import logging
import logging.config
from pathlib import Path
import time
import cx_Oracle

from remindoapi import client
from remindoapi.recipe import RemindoRecipe
import apikey

# Reading configurations
config = configparser.ConfigParser()
config.read_file(open("config.cfg"))

def main():
    logging.debug("Creating remindo client in example.py.")
    rclient = client.RemindoClient(
        config["REMINDOKEYS"]["UUID"], config["REMINDOKEYS"]["SECRET"], config["REMINDOKEYS"]["URL_BASE"]
    )
    l = list()


    r = rclient.list_moments_results(ids=3472)
    for c in r:
        print(
            c.subscription_id, 
            "|", c.user_id,
            "|", c.user_code,
            "|", c.cluster_ids,
            "|", c.area_feedback,
            "|", c.area_name,
            "|", c.try_count
        )

    # print(
    #     c.rid, 
    #     "|", c.caesura,
    #     "|", c.code,
    #     "|", c.datasource_id,
    #     "|", c.date_end,
    #     "|", c.date_start,
    #     "|", c.duration,
    #     "|", c.extra_time,
    #     "|", c.limit_ips,
    #     "|", c.name,
    #     "|", c.recipe_id,
    #     "|", c.recipe_type,
    #     "|", c.requires_approval,
    #     "|", c.recipe_type,
    #     "|", c.show_result,
    #     "|", c.show_result_date,
    #     "|", c.show_result_delay,
    #     "|", c.show_result_delay_type,
    #     "|", c.show_result_time,
    #     "|", c.status,
    #     "|", c.study_id,
    #     "|", c.study_name,
    #     "|", c.time_end,
    #     "|", c.time_start,
    #     "|", c.type
    # )


if __name__ == '__main__':
    main()
    logging.debug("Closing.")

