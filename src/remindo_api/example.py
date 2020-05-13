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

    # s = rclient.list_results(recipe_ids=2335)[0]

    # print("|", s.subscription_id)
    # print("|", s.user_id)
    # print("|", s.user_code)
    # print("|", s.cluster_ids)
    # print("|", s.area_feedback)
    # print("|", s.area_name)
    # print("|", s.try_count)
    # print("|", s.result_id)
    # print("|", s.recipe_id)
    # print("|", s.recipe_type)
    # print("|", s.recipe_name)
    # print("|", s.recipe_code)
    # print("|", s.recipe_category)
    # print("|", s.recipe_source_id)
    # print("|", s.study_id)
    # print("|", s.study_name)
    # print("|", s.status)
    # print("|", s.start_time)
    # print("|", s.end_time)
    # print("|", s.max_score)
    # print("|", s.score)
    # print("|", s.grade)
    # print("|", s.i_count)
    # print("|", s.i_right)
    # print("|", s.i_answered)
    # print("|", s.i_review)
    # print("|", s.i_correct)
    # print("|", s.i_incorrect)
    # print("|", s.i_mostlycorrect)
    # print("|", s.i_mostlyincorrect)
    # print("|", s.show_given_answer)
    # print("|", s.show_score)
    # print("|", s.show_correct)
    # print("|", s.show_grade)
    # print("|", s.show_passed)
    # print("|", s.report_data)
    # print("|", s.passed)

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
