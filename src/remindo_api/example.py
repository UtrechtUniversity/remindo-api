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

    # mom = 3487
    # rec = 2335
    st = rclient.list_stats(recipe_id=2335)
    # print(st.api_call_params_recipe_id)
    for s in st:
        print(s.api_call_params_recipe_id)

    # a = {"S": 2}
    # b = {"S": 3}
    # print(a.update(b))
    # print(s.duration)

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
