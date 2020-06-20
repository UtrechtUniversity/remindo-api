import configparser
from datetime import datetime
import json
import logging
import logging.config
import os
from pathlib import Path

# import time

from remindo_api import client
from remindo_api import collectdata
from six.moves import input

# Setting up logger, Logger properties are defined in logging.ini file
logging.config.fileConfig(f"{Path(__file__).parents[0]}/logging.ini")
logger = logging.getLogger(__name__)

# Reading configurations
config = configparser.ConfigParser()
config.read_file(open(os.path.join(Path(__file__).parents[0], "config.cfg")))

# TODO: fix manual change when retrieval breaks
# Either: 1) delete what was retrieved and restart
# select only the missing recipes and moments and continue
# TODO: display total time at the end of the retrieval


def _open_from_temp(directory, name):
    file = os.path.join(directory, f"{name}.txt")
    with open(file, "r") as f:
        result = list()
        for line in f:
            result.append(int(line.strip()))
        return result


def _open_from_temp_dict(directory, name):
    file = os.path.join(directory, f"{name}.json")
    with open(file, "r") as f:
        new = json.load(f)
        return new


def _is_file(directory, name):
    if os.path.isfile(os.path.join(directory, name)):
        return True
    else:
        return False


def _input_continue(input):
    if input != "Yes":
        return False
    else:
        return True


def main():
    logging.debug("Creating Remindo client.")
    rclient = client.RemindoClient(
        config["REMINDOKEYS"]["UUID"],
        config["REMINDOKEYS"]["SECRET"],
        config["REMINDOKEYS"]["URL_BASE"],
    )

    working_directory = Path(__file__).parent.absolute() / "data"

    logging.debug("Fetching data from {0}.".format(config["DATE"]["SINCE"]))
    logging.debug(f"Execution started at {datetime.now()}")

    if _is_file(working_directory, "items.csv"):
        try:
            logging.debug(f"Found items.csv")
            r = _open_from_temp(working_directory, "recipe_id_list")
            m = _open_from_temp(working_directory, "moment_id_list")
            rm = _open_from_temp_dict(working_directory, "recipe_moment_id_dict")

            val = input("Do you want to continue fetching the reliability? (Yes/No) ")
            answer = _input_continue(val)

            if answer:
                rcollector = collectdata.RemindoCollect(
                    rclient=rclient,
                    data_directory=working_directory,
                    since_date=config["DATE"]["SINCE"],
                    until_date=config["DATE"]["UNTIL"],
                    from_date=config["DATE"]["FROM"],
                    recipe_id_list=r,
                    moment_id_list=m,
                    recipe_moment_id_dict=rm,
                )
                rcollector.fetch_reliability()
                logging.debug(f"Finished retrieving reliability")
        except KeyError as e:
            logging.exception("MAIN ", e)
        try:
            logging.debug("Deleting data lists.")
            rcollector.reset_data_lists()
        except Exception as e:
            logging.exception("A exception occured: ", e)

    elif _is_file(working_directory, "stats.csv"):
        try:
            logging.debug(f"Found stats.csv.")
            r = _open_from_temp(working_directory, "recipe_id_list")
            m = _open_from_temp(working_directory, "moment_id_list")
            rm = _open_from_temp_dict(working_directory, "recipe_moment_id_dict")

            rcollector = collectdata.RemindoCollect(
                rclient=rclient,
                data_directory=working_directory,
                since_date=config["DATE"]["SINCE"],
                until_date=config["DATE"]["UNTIL"],
                from_date=config["DATE"]["FROM"],
                recipe_id_list=r,
                moment_id_list=m,
                recipe_moment_id_dict=rm,
            )
            rcollector.fetch_item_data()
            logging.debug(f"Finished retrieving items")
            rcollector.fetch_reliability()
            logging.debug(f"Finished retrieving reliability")
        except KeyError as e:
            logging.exception("MAIN ", e)
        try:
            logging.debug("Deleting data lists.")
            rcollector.reset_data_lists()
        except Exception as e:
            logging.exception("A exception occured: ", e)

    elif (
        _is_file(working_directory, "recipe_id_list.txt")
        and _is_file(working_directory, "moment_id_list.txt")
        and _is_file(working_directory, "recipe_moment_id_dict.json")
    ):
        try:
            logging.debug(f"Found all id lists.")
            r = _open_from_temp(working_directory, "recipe_id_list")
            m = _open_from_temp(working_directory, "moment_id_list")
            rm = _open_from_temp_dict(working_directory, "recipe_moment_id_dict")

            rcollector = collectdata.RemindoCollect(
                rclient=rclient,
                data_directory=working_directory,
                since_date=config["DATE"]["SINCE"],
                until_date=config["DATE"]["UNTIL"],
                from_date=config["DATE"]["FROM"],
                recipe_id_list=r,
                moment_id_list=m,
                recipe_moment_id_dict=rm,
            )
            rcollector.fetch_stats_data()
            logging.debug(f"Finished retrieving stats")
            rcollector.fetch_item_data()
            logging.debug(f"Finished retrieving items")
            rcollector.fetch_reliability()
            logging.debug(f"Finished retrieving reliability")
        except KeyError as e:
            logging.exception("MAIN ", e)
        try:
            logging.debug("Deleting data lists.")
            rcollector.reset_data_lists()
        except Exception as e:
            logging.exception("A exception occured: ", e)

    elif _is_file(working_directory, "recipe_id_list.txt"):
        try:
            logging.debug(f"Found recipe id list.")
            r = _open_from_temp(working_directory, "recipe_id_list")
            rcollector = collectdata.RemindoCollect(
                rclient=rclient,
                data_directory=working_directory,
                since_date=config["DATE"]["SINCE"],
                until_date=config["DATE"]["UNTIL"],
                from_date=config["DATE"]["FROM"],
                recipe_id_list=r,
            )

            rcollector.fetch_moments()
            logging.debug(f"Finished retrieving moments")
            rcollector.fetch_stats_data()
            logging.debug(f"Finished retrieving stats")
            rcollector.fetch_item_data()
            logging.debug(f"Finished retrieving items")
            rcollector.fetch_reliability()
            logging.debug(f"Finished retrieving reliability")
        except KeyError as e:
            logging.exception("MAIN ", e)
        try:
            logging.debug("Deleting data lists.")
            rcollector.reset_data_lists()
        except Exception as e:
            logging.exception("A exception occured: ", e)
    else:
        try:
            logging.debug(f"No id lists found, starting from studies.")
            rcollector = collectdata.RemindoCollect(
                rclient=rclient,
                data_directory=working_directory,
                since_date=config["DATE"]["SINCE"],
                until_date=config["DATE"]["UNTIL"],
                from_date=config["DATE"]["FROM"],
            )
            rcollector.fetch_studies_recipes()
            logging.debug(f"Finished retrieving studies")
            rcollector.fetch_recipes()
            logging.debug(f"Finished retrieving recipes")
            rcollector.fetch_moments()
            logging.debug(f"Finished retrieving moments")
            rcollector.fetch_stats_data()
            logging.debug(f"Finished retrieving stats")
            rcollector.fetch_item_data()
            logging.debug(f"Finished retrieving items")
            rcollector.fetch_reliability()
            logging.debug(f"Finished retrieving reliability")
        except KeyError as e:
            logging.exception("MAIN ", e)
        try:
            logging.debug("Deleting data lists.")
            rcollector.reset_data_lists()
        except Exception as e:
            logging.exception("A exception occured: ", e)
    logging.debug("Execution ended.")


if __name__ == "__main__":
    main()
    logging.debug("Finished data retrival. Exiting.")
