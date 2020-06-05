# flake8: noqa
import configparser
import logging
import logging.config

from remindo_api import client

# from remindo_api import collectdata as collectdata

# Reading configurations
config = configparser.ConfigParser()
config.read_file(open("config.cfg"))


def main():
    print("hello")
    logging.debug("Creating remindo client in example.py.")
    rclient = client.RemindoClient(
        config["REMINDOKEYS"]["UUID"],
        config["REMINDOKEYS"]["SECRET"],
        config["REMINDOKEYS"]["URL_BASE"],
    )

    c = rclient.hello_world()
    print(c.message)

    # mom = 3487
    # rec = 2335
    # stats = rclient.list_stats(recipe_id=2323)
    # print(stats[0])

    # s = rclient.list_reliability(recipe_id=2335, moment_id=3487)
    # print("|", s.alpha)
    # print("|", s.sem)
    # print("|", s.notes)
    # print("|", s.missing_count)
    # print("|", s.answer_count)
    # print("|", s.stdev)
    # print("|", s.average)
    # print("|", s.max)
    # print("|", s.api_call_params_recipe_id)
    # print("|", s.api_call_params_moment_id)

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
