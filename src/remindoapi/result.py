"""Class implementation for Remindo result"""
from remindoapi import utils


class RemindoResult:
    def __init__(self, result_dict):
        self._result_dict = result_dict

    def list_results(self):
        """Return Remindo results"""
        return {key: value for key, value in self._result_dict.items()}

    @property
    def subscription_id(self):
        """Return the Remindo subscription id for the result"""
        return utils.safeget(self._result_dict, "subscription_id")

    @property
    def user_id(self):
        """Return the Remindo user id id for the result"""
        return utils.safeget(self._result_dict, "user_id")

    @property
    def user_code(self):
        """Return the Remindo user code for the result"""
        return utils.safeget(self._result_dict, "user_code")

    @property
    def cluster_ids(self):
        """Return the Remindo cluster ids for the result"""
        return utils.safeget(self._result_dict, "cluster_ids")

    @property
    def area_feedback(self):
        """Return the Remindo area feedback for the result"""
        return utils.safeget(self._result_dict, "area_feedback")

    @property
    def area_name(self):
        """Return the Remindo area name for the result"""
        return utils.safeget(self._result_dict, "area_name")

    @property
    def try_count(self):
        """Return the Remindo try count for the result"""
        return utils.safeget(self._result_dict, "try_count")

    @property
    def result_id(self):
        """Return the Remindo result id for the result"""
        return utils.safeget(self._result_dict, "result_id")

    @property
    def recipe_id(self):
        """Return the Remindo recipe id for the result"""
        return utils.safeget(self._result_dict, "recipe_id")

    @property
    def recipe_type(self):
        """Return the Remindo recipe type for the result"""
        return utils.safeget(self._result_dict, "recipe_type")

    @property
    def recipe_name(self):
        """Return the Remindo recipe name for the result"""
        return utils.safeget(self._result_dict, "recipe_name")

    @property
    def recipe_code(self):
        """Return the Remindo recipe code for the result"""
        return utils.safeget(self._result_dict, "recipe_code")

    @property
    def recipe_category(self):
        """Return the Remindo recipe category for the result"""
        return utils.safeget(self._result_dict, "recipe_category")

    @property
    def recipe_source_id(self):
        """Return the Remindo recipe source id for the result"""
        return utils.safeget(self._result_dict, "recipe_source_id")

    @property
    def study_id(self):
        """Return the Remindo study id for the result"""
        return utils.safeget(self._result_dict, "study_id")

    @property
    def study_name(self):
        """Return the Remindo study name for the result"""
        return utils.safeget(self._result_dict, "study_name")

    @property
    def status(self):
        """Return the Remindo status for the result"""
        return utils.safeget(self._result_dict, "status")

    @property
    def start_time(self):
        """Return the Remindo start time for the result"""
        return utils.safeget(self._result_dict, "start_time")

    @property
    def end_time(self):
        """Return the Remindo end time for the result"""
        return utils.safeget(self._result_dict, "end_time")

    @property
    def max_score(self):
        """Return the Remindo max score for the result"""
        return utils.safeget(self._result_dict, "max_score")

    @property
    def score(self):
        """Return the Remindo score for the result"""
        return utils.safeget(self._result_dict, "score")

    @property
    def grade(self):
        """Return the Remindo grade for the result"""
        return utils.safeget(self._result_dict, "grade")

    @property
    def i_count(self):
        """Return the Remindo item count for the result"""
        return utils.safeget(self._result_dict, "i_count")

    @property
    def i_right(self):
        """Return the Remindo item answered right for the result"""
        return utils.safeget(self._result_dict, "i_right")

    @property
    def i_answered(self):
        """Return the Remindo item count for the result"""
        return utils.safeget(self._result_dict, "i_answered")

    @property
    def i_review(self):
        """Return the Remindo item in review for the result"""
        return utils.safeget(self._result_dict, "i_review")

    @property
    def i_correct(self):
        """Return the Remindo item correct for the result"""
        return utils.safeget(self._result_dict, "i_correct")

    @property
    def i_incorrect(self):
        """Return the Remindo item incorrect for the result"""
        return utils.safeget(self._result_dict, "i_incorrect")

    @property
    def i_mostlycorrect(self):
        """Return the Remindo item mostly correct for the result"""
        return utils.safeget(self._result_dict, "i_mostlycorrect")

    @property
    def i_mostlyincorrect(self):
        """Return the Remindo item mostly incorrect for the result"""
        return utils.safeget(self._result_dict, "i_mostlyincorrect")

    @property
    def show_given_answer(self):
        """Return the Remindo show given answer bool for the result"""
        return utils.safeget(self._result_dict, "show_given_answer")

    @property
    def show_score(self):
        """Return the Remindo show score bool for the result"""
        return utils.safeget(self._result_dict, "show_score")

    @property
    def show_correct(self):
        """Return the Remindo show correct bool for the result"""
        return utils.safeget(self._result_dict, "show_correct")

    @property
    def show_grade(self):
        """Return the Remindo show grade bool for the result"""
        return utils.safeget(self._result_dict, "show_grade")

    @property
    def show_passed(self):
        """Return the Remindo show passed bool for the result"""
        return utils.safeget(self._result_dict, "show_passed")

    @property
    def report_data(self):
        """Return the Remindo report data bool for the result"""
        return utils.safeget(self._result_dict, "report_data")

    @property
    def passed(self):
        """Return the Remindo passed bool for the result"""
        return utils.safeget(self._result_dict, "passed")

    @property
    def score_type(self):
        """Return the Remindo score type for the result"""
        return utils.safeget(self._result_dict, "score_type")

    @property
    def grade_formatted(self):
        """Return the Remindo grade formatted for the result"""
        return utils.safeget(self._result_dict, "grade_formatted")

    @property
    def can_change(self):
        """Return the Remindo can change bool for the result"""
        return utils.safeget(self._result_dict, "can_change")
