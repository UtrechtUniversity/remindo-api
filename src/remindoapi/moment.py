"""Class implementation for Remindo moment"""
from remindoapi import utils


class RemindoMoment:
    def __init__(self, moment_dict):
        self._moment_dict = moment_dict

    @property
    def rid(self):
        """Return the Remindo id for the moment"""
        return utils.safeget(self._moment_dict, "id")

    @property
    def caesura(self):
        """Return the Remindo caesura for the moment"""
        return utils.safeget(self._moment_dict, "caesura")

    @property
    def code(self):
        """Return the Remindo code for the moment"""
        return utils.safeget(self._moment_dict, "code")

    @property
    def datasource_id(self):
        """Return the Remindo datasource id for the moment"""
        return utils.safeget(self._moment_dict, "datasource_id")

    @property
    def date_end(self):
        """Return the Remindo end date for the moment"""
        return utils.safeget(self._moment_dict, "date_end")

    @property
    def date_start(self):
        """Return the Remindo start date for the moment"""
        return utils.safeget(self._moment_dict, "date_start")

    @property
    def duration(self):
        """Return the Remindo duration for the moment"""
        return utils.safeget(self._moment_dict, "duration")

    @property
    def extra_time(self):
        """Return the Remindo extra time for the moment"""
        return utils.safeget(self._moment_dict, "extra_time")

    @property
    def limit_ips(self):
        """Return the Remindo limit ips attribute for the moment"""
        return utils.safeget(self._moment_dict, "limit_ips")

    @property
    def name(self):
        """Return the Remindo name for the moment"""
        return utils.safeget(self._moment_dict, "name")

    @property
    def recipe_id(self):
        """Return the Remindo recipe id for the moment"""
        return utils.safeget(self._moment_dict, "recipe_id")

    @property
    def recipe_type(self):
        """Return the Remindo recipe type for the moment"""
        return utils.safeget(self._moment_dict, "recipe_type")

    @property
    def requires_approval(self):
        """Return the Remindo require approval bool for the moment"""
        return utils.safeget(self._moment_dict, "requires_approval")

    @property
    def show_result(self):
        """Return the Remindo show result attribute for the moment"""
        return utils.safeget(self._moment_dict, "show_result")

    @property
    def show_result_date(self):
        """Return the Remindo show result date for the moment"""
        return utils.safeget(self._moment_dict, "show_result_date")

    @property
    def show_result_delay(self):
        """Return the Remindo show result delay attribute for the moment"""
        return utils.safeget(self._moment_dict, "show_result_delay")

    @property
    def show_result_delay_type(self):
        """Return the Remindo show result delay type attribute for the moment"""
        return utils.safeget(self._moment_dict, "show_result_delay_type")

    @property
    def show_result_time(self):
        """Return the Remindo show result time for the moment"""
        return utils.safeget(self._moment_dict, "show_result_time")

    @property
    def status(self):
        """Return the Remindo status for the moment"""
        return utils.safeget(self._moment_dict, "status")

    @property
    def study_id(self):
        """Return the Remindo study id for the moment"""
        return utils.safeget(self._moment_dict, "study_id")

    @property
    def study_name(self):
        """Return the Remindo study name for the moment"""
        return utils.safeget(self._moment_dict, "study_name")

    @property
    def time_end(self):
        """Return the Remindo end time for the moment"""
        return utils.safeget(self._moment_dict, "time_end")

    @property
    def time_start(self):
        """Return the Remindo start time for the moment"""
        return utils.safeget(self._moment_dict, "time_start")

    @property
    def type(self):
        """Return the Remindo type attribute for the moment"""
        return utils.safeget(self._moment_dict, "type")

    @property
    def subscription_settings_exam_duration(self):
        """Return the Remindo duration attribute for the moment"""
        return utils.safeget(
            self._moment_dict, "subscription_settings", "exam", "duration"
        )

    @property
    def subscription_settings(self):
        """Return the Remindo subscription settings for the moment"""
        return {
            "areas": utils.safeget(
                self._moment_dict, "subscription_settings", "exam", "areas"
            ),
            "caesura_point": utils.safeget(
                self._moment_dict, "subscription_settings", "exam", "caesura"
            ),
            "points": utils.safeget(
                self._moment_dict, "subscription_settings", "exam", "caesura"
            ),
            "roundprecision": utils.safeget(
                self._moment_dict, "subscription_settings", "exam", "roundprecision"
            ),
            "score_type": utils.safeget(
                self._moment_dict, "subscription_settings", "exam", "score_type"
            ),
            "max_retries": utils.safeget(
                self._moment_dict, "subscription_settings", "max_retries"
            ),
            "continue_practice": utils.safeget(
                self._moment_dict,
                "subscription_settings",
                "practice",
                "continue_practice",
            ),
            "repeat_until": utils.safeget(
                self._moment_dict, "subscription_settings", "practice", "repeat_until"
            ),
            "retry_delay": utils.safeget(
                self._moment_dict, "subscription_settings", "practice", "retry_delay"
            ),
            "start_retry_by_candidate": utils.safeget(
                self._moment_dict,
                "subscription_settings",
                "practice",
                "start_retry_by_candidate",
            ),
            "block_answer_text": utils.safeget(
                self._moment_dict,
                "subscription_settings",
                "security",
                "block_answer_text",
            ),
            "block_question_text": utils.safeget(
                self._moment_dict,
                "subscription_settings",
                "security",
                "block_question_text",
            ),
            "block_right_click": utils.safeget(
                self._moment_dict,
                "subscription_settings",
                "security",
                "block_right_click",
            ),
            "bonuspoints": utils.safeget(
                self._moment_dict, "subscription_settings", "settings", "bonuspoints"
            ),
            "edit_caesura": utils.safeget(
                self._moment_dict, "subscription_settings", "settings", "edit_caesura"
            ),
            "edit_continue_practice": utils.safeget(
                self._moment_dict,
                "subscription_settings",
                "settings",
                "edit_continue_practice",
            ),
            "edit_retry_delay": utils.safeget(
                self._moment_dict,
                "subscription_settings",
                "settings",
                "edit_retry_delay",
            ),
            "edit_show_result": utils.safeget(
                self._moment_dict,
                "subscription_settings",
                "settings",
                "edit_show_result",
            ),
            "extra_time": utils.safeget(
                self._moment_dict, "subscription_settings", "settings", "extra_time"
            ),
            "correct": utils.safeget(
                self._moment_dict, "subscription_settings", "show_result", "correct"
            ),
            "correct_answer": utils.safeget(
                self._moment_dict,
                "subscription_settings",
                "show_result",
                "correct_answer",
            ),
            "given_answer": utils.safeget(
                self._moment_dict,
                "subscription_settings",
                "show_result",
                "given_answer",
            ),
            "grade": utils.safeget(
                self._moment_dict, "subscription_settings", "show_result", "grade"
            ),
            "passed": utils.safeget(
                self._moment_dict, "subscription_settings", "show_result", "passed"
            ),
            "score": utils.safeget(
                self._moment_dict, "subscription_settings", "show_result", "score"
            ),
            "tools": utils.safeget(self._moment_dict, "subscription_settings", "tools"),
            "v": utils.safeget(self._moment_dict, "subscription_settings", "v"),
        }
