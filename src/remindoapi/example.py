# flake8: noqa
import configparser
import logging
import logging.config

from remindoapi import client

# from remindoapi import collectdata as collectdata

# Reading configurations
config = configparser.ConfigParser()
config.read_file(open("config.cfg"))


def main():
    print("hello")
    # logging.debug("Creating remindo client in example.py.")
    # rclient = client.RemindoClient(
    #     config["REMINDOKEYS"]["UUID"],
    #     config["REMINDOKEYS"]["SECRET"],
    #     config["REMINDOKEYS"]["URL_BASE"],
    # )

    # rcollector = collectdata.RemindoCollect(
    #     rclient, config["DATA_DIR_PATH"]["PATH"], config["DATE"]["SINCE"]
    # )
    # logging.debug("Fetching data from {0}.".format(config["DATE"]["SINCE"]))

    # wait_time = int(config["TIMEPARAM"]["WAIT_TIME"])
    # logging.debug(f"Execution started at {datetime.now()}")

    # try:
    #     rcollector.fetch_clusters()
    #     time.sleep(wait_time)
    #     rcollector.fetch_studies_recipes()
    #     time.sleep(wait_time)
    #     rcollector.fetch_recipes()
    #     time.sleep(wait_time)
    # except Exception:
    #     pass


if __name__ == "__main__":
    main()
    logging.debug("Closing.")
