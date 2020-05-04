from datetime import datetime
import configparser
import logging
import logging.config
from pathlib import Path
import time

from remindoapi import client
from remindoapi import collectdata

# Setting up logger, Logger properties are defined in logging.ini file
logging.config.fileConfig(f"{Path(__file__).parents[0]}/logging.ini")
logger = logging.getLogger(__name__)

# Reading configurations
config = configparser.ConfigParser()
config.read_file(open("config.cfg"))


def main():
    logging.debug("Creating Remindo client.")
    rclient = client.RemindoClient(
        config["REMINDOKEYS"]["UUID"],
        config["REMINDOKEYS"]["SECRET"],
        config["REMINDOKEYS"]["URL_BASE"],
    )
    rcollector = collectdata.RemindoCollect(
        rclient, config["DATA_DIR_PATH"]["PATH"], config["DATE"]["SINCE"]
    )
    logging.debug("Fetching data from {0}.".format(config["DATE"]["SINCE"]))

    wait_time = int(config["TIMEPARAM"]["WAIT_TIME"])
    logging.debug(f"Execution started at {datetime.now()}")

    try:
        rcollector.fetch_clusters()
        time.sleep(wait_time)
        rcollector.fetch_studies_recipes()
        time.sleep(wait_time)
        rcollector.fetch_recipes()
        time.sleep(wait_time)
        rcollector.fetch_moments()
        time.sleep(wait_time)
        rcollector.fetch_moments_result()
        time.sleep(wait_time)
        rcollector.fetch_stats_data()
        time.sleep(wait_time)
        rcollector.fetch_item_data()
    except Exception as e:
        logging.exception("A exception occured: ", e)

    try:
        logging.debug("Deleting data lists.")
        rcollector.reset_data_lists()
    except Exception as e:
        logging.exception("A exception occured: ", e)
    logging.debug("Execution ended.")


if __name__ == "__main__":
    main()
    logging.debug("Exiting.")
