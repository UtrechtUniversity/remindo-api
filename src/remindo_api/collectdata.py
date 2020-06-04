"""Class implementation for fetching remindo data"""
from collections import OrderedDict
import csv
from datetime import datetime
import logging
import logging.config
import os
import time

import pandas as pd


logger = logging.getLogger(__name__)
# TODO: retrieve individual recipes based on date
# use it to quality check with those retrieved from studies?

# _parse_moment_data() is not parsing subscriptions settings on purpose
# list_results() currently not being used - no need to save students' data?
# list_reliability() currently not being used because does not work


class RemindoCollectException(Exception):
    """Class that is called for exception messages

    You can see the usage of this class looking at the test

    """

    def __init__(self, error_msg):
        self.error_msg = error_msg

    def __str__(self):
        return self.error_msg


class RemindoCollect:
    def __init__(self, rclient, data_directory, since_date):
        self._rclient = rclient
        self._data_directory = data_directory
        self._since_date = since_date

        self._cluster_data_list = list()
        self._study_data_list = list()
        self._recipe_data_list = list()
        self._moment_data_list = list()
        self._moment_result_data_list = list()
        self._result_data_list = list()
        self._reliability_data_list = list()
        self._stats_data_list = list()
        self._item_data_list = list()

        self._recipe_id_list = list()
        self._recipe_moment_id_dict = dict()
        self._moment_id_list = list()
        self._moment = int()
        self._recipe = int()
        self._base_directory = os.path.join(data_directory, "data/landing-zone")
        if not os.path.isdir(self._base_directory):
            os.makedirs(self._base_directory)

    def fetch_clusters(self):
        logging.debug("Fetching clusters data.")
        clusters = self._rclient.list_clusters()
        for cluster in clusters:
            self._cluster_data_list.append(self._parse_cluster_data(cluster))

        for module_name, module_data in zip(["clusters"], [self._cluster_data_list]):
            logging.debug(f"Writing data for: {module_name}")
            self._write_to_disk(module_name, module_data)

    def fetch_studies_recipes(self):
        logging.debug("Fetching study data.")
        global studies
        studies, recipes = self._rclient.list_studies(
            complete=True, since=self._since_date
        )
        for study in studies:
            self._study_data_list.append(self._parse_study_data(study))
        # These are the recipes modified from the date chosen
        for recipe in recipes:
            self._recipe_id_list.append(recipe.rid)

        for module_name, module_data in zip(["studies"], [self._study_data_list]):
            logging.debug(f"Writing data for: {module_name}")
            self._write_to_disk(module_name, module_data)

    def fetch_recipes(self):
        logging.debug("Fetching recipes data from studies.")
        for rid in self._recipe_id_list:
            try:
                recipes = self._rclient.list_recipes(recipe_id=rid)
                # recipe comes within a list because of how list_recipes works
                if len(recipes) == 1:
                    try:
                        self._recipe_data_list.append(
                            self._parse_recipe_data(recipes[0])
                        )
                    except KeyError:
                        print("A Key Error occurred on recipe {0} ".format(rid))
                        continue
                elif len(recipes) > 1:
                    for recipe in recipes:
                        try:
                            self._recipe_data_list.append(
                                self._parse_recipe_data(recipe)
                            )
                        except KeyError:
                            print("A Key Error occurred on recipe {0} ".format(rid))
                            continue
                else:
                    print("ERROR")
                    continue
                time.sleep(0.1)
            except Exception:
                print("An error occurred on recipe id {0}".format(rid))
                continue

        for module_name, module_data in zip(["recipes"], [self._recipe_data_list]):
            logging.debug(f"Writing data for: {module_name}")
            self._write_to_disk(module_name, module_data)

    def fetch_moments(self):
        logging.debug("Fetching moments from recipes.")
        for recipe in self._recipe_id_list:
            try:
                moments = self._rclient.list_moments(recipe_ids=recipe)
                moment_temp_list = []
                for moment in moments:
                    moment_temp_list.append(moment.rid)
                    self._moment_data_list.append(self._parse_moment_data(moment))
                    self._moment_id_list.append(moment.rid)
                # Possibility of saving individual moments not as list
                # and empty list as "None"?
                self._recipe_moment_id_dict[recipe] = moment_temp_list
                time.sleep(0.1)
            except Exception:
                print("An error occurred on recipe {0}".format(recipe))
                continue

        for module_name, module_data in zip(["moments"], [self._moment_data_list]):
            logging.debug(f"Writing data for: {module_name}")
            self._write_to_disk(module_name, module_data)

    def fetch_moments_result(self):
        logging.debug("Fetching moments result data from moments.")
        for moment in self._moment_id_list:
            try:
                moment_results = self._rclient.list_moments_results(ids=moment)
                if moment_results is not False:
                    for moment_result in moment_results:
                        self._moment_result_data_list.append(
                            self._parse_moment_result_data(moment_result)
                        )
                time.sleep(0.1)
            except Exception:
                print("An error occurred on moment {0}".format(moment))
                continue

        for module_name, module_data in zip(
            ["moment_results"], [self._moment_result_data_list]
        ):
            logging.debug(f"Writing data for: {module_name}")
            self._write_to_disk(module_name, module_data)

    def fetch_reliability(self):
        logging.debug("Fetching reliability data from moments.")
        for moment in self._moment_id_list:
            try:
                reliability_result = self._rclient.list_reliability(moment_id=moment)
                if reliability_result is not None:
                    self._reliability_data_list.append(
                        self._parse_reliability_result_data(reliability_result)
                    )
                time.sleep(0.1)
            except Exception:
                print("An error occurred on moment {0}".format(moment))
                continue

        for module_name, module_data in zip(
            ["reliability"], [self._reliability_data_list]
        ):
            logging.debug(f"Writing data for: {module_name}")
            self._write_to_disk(module_name, module_data)

    def fetch_stats_data(self):
        # Checks if recipes have mutiple list of moments
        logging.debug("Fetching stats data from moments.")
        for recipe in self._recipe_moment_id_dict.keys():
            for moment in self._recipe_moment_id_dict[recipe]:
                if moment is None:
                    try:
                        stats_results = self._rclient.list_stats(recipe_id=recipe)
                        if stats_results is not None:
                            for result in stats_results:
                                self._stats_data_list.append(
                                    self._parse_stats_data(result)
                                )
                    except Exception:
                        print(
                            "An error occurred on recipe {0}, moment {1}".format(
                                recipe, moment
                            )
                        )
                        continue
                else:
                    try:
                        stats_results = self._rclient.list_stats(
                            recipe_id=recipe, moment_id=moment
                        )
                        if stats_results is not None:
                            for result in stats_results:
                                self._stats_data_list.append(
                                    self._parse_stats_data(result)
                                )
                        time.sleep(0.1)
                    except Exception as e:
                        print(
                            "An error of class {0} occurred on recipe {1}, moment {2}:".format(
                                type(e), recipe, moment
                            )
                        )
                        print("with message {0}".format(e))
                        continue

        for module_name, module_data in zip(["stats"], [self._stats_data_list]):
            logging.debug(f"Writing data for: {module_name}")
            self._write_to_disk(module_name, module_data)

    def fetch_item_data(self):
        logging.debug("Fetching item data from recipes and moments.")
        for recipe in self._recipe_moment_id_dict.keys():
            for moment in self._recipe_moment_id_dict[recipe]:
                if moment is None:
                    continue
                else:
                    try:
                        item_results = self._rclient.list_item_results(
                            recipe_id=recipe, moment_id=moment
                        )
                        if item_results is not None:
                            for item_result in item_results:
                                self._item_data_list.append(
                                    self._parse_item_data(item_result)
                                )
                        time.sleep(0.1)
                    except Exception as e:
                        print(
                            "An error of class {0} occurred on recipe {1}, moment {2} ".format(
                                type(e), recipe, moment
                            )
                        )
                        print("with message: '{0}'".format(e))
                        continue

        for module_name, module_data in zip(["items"], [self._item_data_list]):
            logging.debug(f"Writing data for: {module_name}")
            self._write_to_disk(module_name, module_data)

    def _write_to_disk(self, module_name, module_data):
        file = os.path.join(self._base_directory, f"{module_name}.csv")
        write_mode, header = ("a", False) if os.path.isfile(file) else ("w", True)

        if len(module_data) > 0:
            pd.DataFrame(module_data).to_csv(
                path_or_buf=file,
                index=False,
                mode=write_mode,
                header=header,
                quoting=csv.QUOTE_MINIMAL,
            )

    def reset_data_lists(self):
        self._cluster_data_list = list()
        self._study_data_list = list()
        self._recipe_data_list = list()
        self._moment_data_list = list()
        self._moment_result_data_list = list()
        self._result_data_list = list()
        self._reliability_data_list = list()
        self._stats_data_list = list()
        self._item_data_list = list()

    def _parse_cluster_data(self, cluster_obj):
        """Parse cluster data from cluster object"""
        return OrderedDict(
            {
                "id": cluster_obj.rid,
                "name": cluster_obj.name,
                "record_create_timestamp": datetime.now(),
            }.items()
        )

    def _parse_study_data(self, study_obj):
        """Parse study data from study object"""
        return OrderedDict(
            {
                "id": study_obj.rid,
                "name": study_obj.name,
                "code": study_obj.code,
                "descr": study_obj.descr,
                "edition_name": study_obj.edition_name,
                "edition_descr": study_obj.edition_descr,
                "source_edition_id": study_obj.source_edition_id,
                "source_study_id": study_obj.source_study_id,
                "api_call_params_complete": study_obj.api_call_params_complete,
                "api_call_params_since": study_obj.api_call_params_since,
                "record_create_timestamp": datetime.now(),
            }.items()
        )

    def _parse_recipe_data(self, recipe_obj):
        """Parse recipe data from recipe object"""
        return OrderedDict(
            {
                "id": recipe_obj.rid,
                "name": recipe_obj.name,
                "code": recipe_obj.code,
                "study_id": recipe_obj.study_id,
                "category": recipe_obj.category,
                "status": recipe_obj.status,
                "type": recipe_obj.type,
                "exam_duration": recipe_obj.settings_exam_duration,
                # availalbe only from study/list full=True
                # "recipe_source_recipe_id" : recipe_obj.source_recipe_id,
                # "v": recipe_obj.settings_v,
                "max_retries": recipe_obj.settings_max_retries,
                "tools": recipe_obj.settings_tools,
                "practice_repeat_until": recipe_obj.settings_practice_repeat_until,
                "practice_continue_practice": recipe_obj.settings_practice_continue_practice,
                "practice_start_retry_by_candidate": recipe_obj.settings_practice_start_retry_by_candidate,
                "practice_start_retry_delay": recipe_obj.settings_practice_start_retry_delay,
                "exam_caesura": recipe_obj.settings_exam_caesura,
                "exam_round_grade_decimals": recipe_obj.settings_exam_round_grade_decimals,
                "show_result_given_answer": recipe_obj.settings_show_result_given_answer,
                "show_result_correct_answer": recipe_obj.settings_show_result_correct_answer,
                "show_result_score": recipe_obj.settings_show_result_score,
                "show_correct": recipe_obj.settings_show_correct,
                "show_grade": recipe_obj.settings_show_grade,
                "passed": recipe_obj.settings_passed,
                "bonuspoints": recipe_obj.settings_settings_bonuspoints,
                "extra_time": recipe_obj.settings_settings_extra_time,
                "api_call_params_recipe_id": recipe_obj.api_call_params_recipe_id,
                "api_call_params_study_id": recipe_obj.api_call_params_study_id,
                "api_call_params_since": recipe_obj.api_call_params_since,
                "api_call_params_full": recipe_obj.api_call_params_full,
                "create_timestamp": datetime.now(),
            }.items()
        )

    def _parse_moment_data(self, moment_obj):
        """Parse moment data from moment object"""
        return OrderedDict(
            {
                "id": moment_obj.rid,
                "name": moment_obj.name,
                "caesura": moment_obj.caesura,
                "code": moment_obj.code,
                "datasource_id": moment_obj.datasource_id,
                "date_end": moment_obj.date_end,
                "date_start": moment_obj.date_start,
                "duration": moment_obj.duration,
                "extra_time": moment_obj.extra_time,
                "limit_ips": moment_obj.limit_ips,
                "recipe_id": moment_obj.recipe_id,
                "recipe_type": moment_obj.recipe_type,
                "requires_approval": moment_obj.requires_approval,
                "study_id": moment_obj.study_id,
                "study_name": moment_obj.study_name,
                "time_end": moment_obj.time_end,
                "time_start": moment_obj.time_start,
                "type": moment_obj.type,
                "show_result": moment_obj.show_result,
                "show_result_date": moment_obj.show_result_date,
                "show_result_delay": moment_obj.show_result_delay,
                "show_result_delay_type": moment_obj.show_result_delay_type,
                "show_result_time": moment_obj.show_result_time,
                "status": moment_obj.status,
                "api_call_params_recipe_ids": moment_obj.api_call_params_recipe_ids,
                "api_call_params_from": moment_obj.api_call_params_from,
                "record_create_timestamp": datetime.now(),
            }.items()
        )

    def _parse_moment_result_data(self, moment_obj):
        """Parse moment data from moment result object"""
        return OrderedDict(
            {
                "subscription_id": moment_obj.subscription_id,
                "result_id": moment_obj.result_id,
                "user_id": moment_obj.user_id,
                "user_code": moment_obj.user_code,
                "recipe_id": moment_obj.recipe_id,
                "recipe_type": moment_obj.recipe_type,
                "recipe_name": moment_obj.recipe_name,
                "recipe_code": moment_obj.recipe_code,
                "recipe_category": moment_obj.recipe_category,
                "recipe_source_id": moment_obj.recipe_source_id,
                "study_id": moment_obj.study_id,
                "study_name": moment_obj.study_name,
                "status": moment_obj.status,
                "start_time": moment_obj.start_time,
                "end_time": moment_obj.end_time,
                "max_score": moment_obj.max_score,
                "score": moment_obj.score,
                "grade": moment_obj.grade,
                "try_count": moment_obj.try_count,
                "i_count": moment_obj.i_count,
                "i_right": moment_obj.i_right,
                "i_answered": moment_obj.i_answered,
                "i_review": moment_obj.i_review,
                "i_correct": moment_obj.i_correct,
                "i_incorrect": moment_obj.i_incorrect,
                "i_mostlycorrect": moment_obj.i_mostlycorrect,
                "i_mostlyincorrect": moment_obj.i_mostlyincorrect,
                "show_given_answer": moment_obj.show_given_answer,
                "show_score": moment_obj.show_score,
                "show_correct": moment_obj.show_correct,
                "show_grade": moment_obj.show_grade,
                "show_passed": moment_obj.show_passed,
                "report_data": moment_obj.report_data,
                "passed": moment_obj.passed,
                "area_name": moment_obj.area_name,
                "area_feedback": moment_obj.area_feedback,
                "score_type": moment_obj.score_type,
                "grade_formatted": moment_obj.grade_formatted,
                "can_change": moment_obj.can_change,
                "api_call_moment_id": moment_obj.api_call_params_id,
                "record_create_timestamp": datetime.now(),
            }.items()
        )

    def _parse_reliability_result_data(self, reliability_obj):
        """Parse reliability data from reliability result object"""
        return OrderedDict(
            {
                "alpha": reliability_obj.alpha,
                "sem": reliability_obj.sem,
                "notes": reliability_obj.notes,
                "missing_count": reliability_obj.missing_count,
                "answer_count": reliability_obj.answer_count,
                "stdev": reliability_obj.stdev,
                "average": reliability_obj.average,
                "max": reliability_obj.max,
                "api_call_params_recipe_id": reliability_obj.api_call_params_recipe_id,
                "api_call_params_moment_id": reliability_obj.api_call_params_moment_id,
                "record_create_timestamp": datetime.now(),
            }.items()
        )

    def _parse_stats_data(self, stats_obj):
        """Parse stats data from stats result object"""
        return OrderedDict(
            {
                "item_identifier": stats_obj.item_identifier,
                "code": stats_obj.code,
                "type": stats_obj.type,
                "language": stats_obj.language,
                "max_score": stats_obj.max_score,
                "interaction_count": stats_obj.interaction_count,
                "difficulty": stats_obj.difficulty,
                "section": stats_obj.section,
                "question_position": stats_obj.question_position,
                "p": stats_obj.p,
                "std": stats_obj.std,
                "rir": stats_obj.rir,
                "total": stats_obj.total,
                "answered": stats_obj.answered,
                "api_call_params_recipe_id": stats_obj.api_call_params_recipe_id,
                "api_call_params_moment_id": stats_obj.api_call_params_moment_id,
                "record_create_timestamp": datetime.now(),
            }.items()
        )

    def _parse_item_data(self, item_obj):
        """Parse item data from item result object"""
        return OrderedDict(
            {
                "item_identifier": item_obj.item_identifier,
                "num_attempts": item_obj.num_attempts,
                "duration": item_obj.duration,
                "status": item_obj.status,
                "score": item_obj.score,
                "passed": item_obj.passed,
                "max_score": item_obj.max_score,
                "flagged": item_obj.flagged,
                "check_manually": item_obj.check_manually,
                "weight": item_obj.weight,
                "subscription_id": item_obj.subscription_id,
                "position_item": item_obj.position_item,
                "response_cardinality": item_obj.response_cardinality,
                "response_baseType": item_obj.response_baseType,
                "response_choiceSequence": item_obj.response_choiceSequence,
                "response_candidateResponse": item_obj.response_candidateResponse,
                "response_correctResponse": item_obj.response_correctResponse,
                "api_call_params_recipe_id": item_obj.api_call_params_recipe_id,
                "api_call_params_moment_id": item_obj.api_call_params_moment_id,
                "record_create_timestamp": datetime.now(),
            }.items()
        )
