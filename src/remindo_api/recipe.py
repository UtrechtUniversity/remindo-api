# src/remindo_api/recipe.py
"""Class implementation for Remindo recipe."""
from dataclasses import dataclass


from remindo_api import utils


@dataclass
class RemindoRecipe:
    """Remindo Recipe object.

    Args:
        _recipe_dict (dict) : Dictionary containing the recipe information.
    """

    _recipe_dict: dict

    @property
    def rid(self):
        """Return the recipe id."""
        return utils.safeget(self._recipe_dict, "id")

    @property
    def name(self):
        """Return the recipe name."""
        return utils.safeget(self._recipe_dict, "name")

    @property
    def code(self):
        """Return the recipe code."""
        return utils.safeget(self._recipe_dict, "code")

    @property
    def study_id(self):
        """Return the recipe study id.

        Notes:
            Only available in the list_recipe() call.
        """
        return utils.safeget(self._recipe_dict, "study_id")

    @property
    def category(self):
        """Return the recipe category."""
        return utils.safeget(self._recipe_dict, "category")

    @property
    def status(self):
        """Return the recipe status."""
        return utils.safeget(self._recipe_dict, "status")

    @property
    def type(self):
        """Return the recipe type.

        Notes:
            Only available in the list_studies_recipes() call.
        """
        return utils.safeget(self._recipe_dict, "type")

    @property
    def source_recipe_id(self):
        """Return the recipe `source recipe id`.

        Notes:
            Only available in the list_studies_recipes() call.
        """
        return utils.safeget(self._recipe_dict, "source_recipe_id")

    @property
    def settings_v(self):
        """Return the recipe `settings-v` id."""
        return utils.safeget(self._recipe_dict, "settings", "v")

    @property
    def settings_max_retries(self):
        """Return the recipe `max_retries id`."""
        return utils.safeget(self._recipe_dict, "settings", "max_retries")

    @property
    def settings_tools(self):
        """Return the recipe `settings-tools`."""
        return utils.safeget(self._recipe_dict, "settings", "tools")

    # Settings: practice

    @property
    def settings_practice_repeat_until(self):
        """Return repeat_until for the recipe."""
        return utils.safeget(self._recipe_dict, "settings", "practice", "repeat_until")

    @property
    def settings_practice_continue_practice(self):
        """Return continue_practice for the recipe."""
        return utils.safeget(
            self._recipe_dict, "settings", "practice", "continue_practice"
        )

    @property
    def settings_practice_start_retry_by_candidate(self):
        """Return start_retry_by_candidate for the recipe."""
        return utils.safeget(
            self._recipe_dict, "settings", "practice", "start_retry_by_candidate"
        )

    @property
    def settings_practice_start_retry_delay(self):
        """Return retry_delay for the recipe."""
        return utils.safeget(self._recipe_dict, "settings", "practice", "retry_delay")

    @property
    def settings_practice(self):
        """Return practice settings for the recipe."""
        return {
            "repeat_until": utils.safeget(
                self._recipe_dict, "settings", "practice", "repeat_until"
            ),
            "continue_practice": utils.safeget(
                self._recipe_dict, "settings", "practice", "continue_practice"
            ),
            "start_retry_by_candidate": utils.safeget(
                self._recipe_dict, "settings", "practice", "start_retry_by_candidate"
            ),
            "retry_delay": utils.safeget(
                self._recipe_dict, "settings", "practice", "retry_delay"
            ),
        }

    # Settings: exam

    @property
    def settings_exam_caesura(self):
        """Return exam-caesura for the recipe."""
        return utils.safeget(self._recipe_dict, "settings", "exam", "caesura")

    @property
    def settings_exam_round_grade_decimals(self):
        """Return exam-round_grade_decimals for the recipe."""
        return utils.safeget(
            self._recipe_dict, "settings", "exam", "round_grade_decimals"
        )

    @property
    def settings_exam_duration(self):
        """Return exam-duration for the recipe."""
        return utils.safeget(self._recipe_dict, "settings", "exam", "duration")

    @property
    def settings_exam(self):
        """Return exam settings for the recipe."""
        return {
            "caesura": utils.safeget(self._recipe_dict, "settings", "exam", "caesura"),
            "round_grade_decimals": utils.safeget(
                self._recipe_dict, "settings", "exam", "round_grade_decimals"
            ),
            "duration": utils.safeget(
                self._recipe_dict, "settings", "exam", "duration"
            ),
        }

    # Settings: show_result

    @property
    def settings_show_result_given_answer(self):
        """Return show_result-given_answer for the recipe."""
        return utils.safeget(
            self._recipe_dict, "settings", "show_result", "given_answer"
        )

    @property
    def settings_show_result_correct_answer(self):
        """Return show_result: correct_answer for the recipe."""
        return utils.safeget(
            self._recipe_dict, "settings", "show_result", "correct_answer"
        )

    @property
    def settings_show_result_score(self):
        """Return show_result-score for the recipe."""
        return utils.safeget(self._recipe_dict, "settings", "show_result", "score")

    @property
    def settings_show_correct(self):
        """Return correct-score for the recipe."""
        return utils.safeget(self._recipe_dict, "settings", "show_result", "correct")

    @property
    def settings_show_grade(self):
        """Return correct-grade for the recipe."""
        return utils.safeget(self._recipe_dict, "settings", "show_result", "grade")

    @property
    def settings_passed(self):
        """Return correct-passed for the recipe."""
        return utils.safeget(self._recipe_dict, "settings", "show_result", "passed")

    @property
    def settings_show_result(self):
        """Return show_result for the recipe."""
        return {
            "given_answer": utils.safeget(
                self._recipe_dict, "settings", "show_result", "given_answer"
            ),
            "correct_answer": utils.safeget(
                self._recipe_dict, "settings", "show_result", "correct_answer"
            ),
            "score": utils.safeget(
                self._recipe_dict, "settings", "show_result", "score"
            ),
            "correct": utils.safeget(
                self._recipe_dict, "settings", "show_result", "correct"
            ),
            "grade": utils.safeget(
                self._recipe_dict, "settings", "show_result", "grade"
            ),
            "passed": utils.safeget(
                self._recipe_dict, "settings", "show_result", "passed"
            ),
        }

    # Settings: settings

    @property
    def settings_settings_edit_caesura(self):
        """Return settings-edit_caesura for the recipe."""
        return utils.safeget(self._recipe_dict, "settings", "settings", "edit_caesura")

    @property
    def settings_settings_bonuspoints(self):
        """Return bonuspoints for the recipe."""
        return utils.safeget(self._recipe_dict, "settings", "settings", "bonuspoints")

    @property
    def settings_settings_extra_time(self):
        """Return extra_time for the recipe."""
        return utils.safeget(self._recipe_dict, "settings", "settings", "extra_time")

    @property
    def settings_settings_edit_show_result(self):
        """Return edit_show_result for the recipe."""
        return utils.safeget(
            self._recipe_dict, "settings", "settings", "edit_show_result"
        )

    @property
    def settings_settings_edit_retry_delay(self):
        """Return edit_retry_delay for the recipe."""
        return utils.safeget(
            self._recipe_dict, "settings", "settings", "edit_retry_delay"
        )

    @property
    def settings_settings_edit_continue_practice(self):
        """Return edit_continue_practice for the recipe."""
        return utils.safeget(
            self._recipe_dict, "settings", "settings", "edit_continue_practice"
        )

    @property
    def settings_settings(self):
        """Return settings for the recipe."""
        return {
            "edit_caesura": utils.safeget(
                self._recipe_dict, "settings", "settings", "edit_caesura"
            ),
            "bonuspoints": utils.safeget(
                self._recipe_dict, "settings", "settings", "bonuspoints"
            ),
            "extra_time": utils.safeget(
                self._recipe_dict, "settings", "settings", "extra_time"
            ),
            "edit_show_result": utils.safeget(
                self._recipe_dict, "settings", "settings", "edit_show_result"
            ),
            "edit_retry_delay": utils.safeget(
                self._recipe_dict, "settings", "settings", "edit_retry_delay"
            ),
            "edit_continue_practice": utils.safeget(
                self._recipe_dict, "settings", "settings", "edit_continue_practice"
            ),
        }

    @property
    def api_call_params_recipe_id(self):
        """Return the parameter recipe_id used in the api call."""
        return utils.safeget(self._recipe_dict, "api_call_params", "recipe_id")

    @property
    def api_call_params_code(self):
        """Return the parameter code used in the api call."""
        return utils.safeget(self._recipe_dict, "api_call_params", "code")

    @property
    def api_call_params_category(self):
        """Return the parameter category used in the api call."""
        return utils.safeget(self._recipe_dict, "api_call_params", "category")

    @property
    def api_call_params_study_id(self):
        """Return the parameter study_id used in the api call."""
        return utils.safeget(self._recipe_dict, "api_call_params", "study_id")

    @property
    def api_call_params_filtr(self):
        """Return the parameter study_id used in the api call."""
        return utils.safeget(self._recipe_dict, "api_call_params", "filtr")

    @property
    def api_call_params_datasource_uuid(self):
        """Return the parameter study_id used in the api call."""
        return utils.safeget(self._recipe_dict, "api_call_params", "datasource_uuid")

    @property
    def api_call_params_since(self):
        """Return the parameter since used in the api call."""
        return utils.safeget(self._recipe_dict, "api_call_params", "since")

    @property
    def api_call_params_full(self):
        """Return the parameter full used in the api call."""
        return utils.safeget(self._recipe_dict, "api_call_params", "full")
