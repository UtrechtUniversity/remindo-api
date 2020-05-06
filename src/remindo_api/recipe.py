"""Class implementation for Remindo recipe"""


class RemindoRecipe:
    def __init__(self, recipe_dict):
        self._recipe_dict = recipe_dict

    @property
    def rid(self):
        """Return the Remindo id for the recipe"""
        return self._recipe_dict["id"]

    @property
    def name(self):
        """Return the Remindo name for the recipe"""
        return self._recipe_dict["name"]

    @property
    def code(self):
        """Return the Remindo code for the recipe"""
        return self._recipe_dict["code"]

    @property
    def study_id(self):
        """Return the Remindo study id for the recipe

        Only available in the list_recipe() call.
        """
        return self._recipe_dict["study_id"]

    @property
    def category(self):
        """Return the Remindo category for the recipe"""
        return self._recipe_dict["category"]

    @property
    def status(self):
        """Return the Remindo status for the recipe"""
        return self._recipe_dict["status"]

    @property
    def type(self):
        """Return the Remindo type for the recipe

        Only available in the list_studies_recipes() call.
        """
        return self._recipe_dict["type"]

    @property
    def source_recipe_id(self):
        """Return the Remindo source recipe id for the recipe

        Only available in the list_studies_recipes() call.
        """
        return self._recipe_dict["source_recipe_id"]

    @property
    def settings_v(self):
        """Return the Remindo settings:v id for the recipe"""
        return self._recipe_dict["settings"]["v"]

    @property
    def settings_max_retries(self):
        """Return the Remindo settings: max_retries id for the recipe"""
        return self._recipe_dict["settings"]["max_retries"]

    @property
    def settings_tools(self):
        """Return the Remindo settings: tools for the recipe"""
        return self._recipe_dict["settings"]["tools"]

    # Settings: practice

    @property
    def settings_practice_repeat_until(self):
        """Return the Remindo settings:
        practice: repeat_until for the recipe"""
        return self._recipe_dict["settings"]["practice"]["repeat_until"]

    @property
    def settings_practice_continue_practice(self):
        """Return the Remindo settings:
        practice: continue_practice for the recipe"""
        return self._recipe_dict["settings"]["practice"]["continue_practice"]

    @property
    def settings_practice_start_retry_by_candidate(self):
        """Return the Remindo settings:
        practice: start_retry_by_candidate for the recipe"""
        return self._recipe_dict["settings"]["practice"]["start_retry_by_candidate"]

    @property
    def settings_practice_start_retry_delay(self):
        """Return the Remindo settings:
        practice: retry_delay for the recipe"""
        return self._recipe_dict["settings"]["practice"]["retry_delay"]

    @property
    def settings_practice(self):
        """Return the Remindo settings:
        practice for the recipe"""
        return {
            "repeat_until": self._recipe_dict["settings"]["practice"]["repeat_until"],
            "continue_practice": self._recipe_dict["settings"]["practice"][
                "continue_practice"
            ],
            "start_retry_by_candidate": self._recipe_dict["settings"]["practice"][
                "start_retry_by_candidate"
            ],
            "retry_delay": self._recipe_dict["settings"]["practice"]["retry_delay"],
        }

    # Settings: exam

    @property
    def settings_exam_caesura(self):
        """Return the Remindo settings:
        exam: caesura for the recipe"""
        return self._recipe_dict["settings"]["exam"]["caesura"]

    @property
    def settings_exam_round_grade_decimals(self):
        """Return the Remindo settings:
        exam: round_grade_decimals for the recipe"""
        return self._recipe_dict["settings"]["exam"]["round_grade_decimals"]

    @property
    def settings_exam_duration(self):
        """Return the Remindo settings:
        exam: duration for the recipe"""
        return self._recipe_dict["settings"]["exam"]["duration"]

    @property
    def settings_exam(self):
        """Return the Remindo settings:
        exam for the recipe"""
        return {
            "caesura": self._recipe_dict["settings"]["exam"]["caesura"],
            "round_grade_decimals": self._recipe_dict["settings"]["exam"][
                "round_grade_decimals"
            ],
            "duration": self._recipe_dict["settings"]["exam"]["duration"],
        }

    # Settings: show_result

    @property
    def settings_show_result_given_answer(self):
        """Return the Remindo settings:
        show_result: given_answer for the recipe"""
        return self._recipe_dict["settings"]["show_result"]["given_answer"]

    @property
    def settings_show_result_correct_answer(self):
        """Return the Remindo settings:
        show_result: correct_answer for the recipe"""
        return self._recipe_dict["settings"]["show_result"]["correct_answer"]

    @property
    def settings_show_result_score(self):
        """Return the Remindo settings:
        show_result: score for the recipe"""
        return self._recipe_dict["settings"]["show_result"]["score"]

    @property
    def settings_show_correct(self):
        """Return the Remindo settings:
        correct: score for the recipe"""
        return self._recipe_dict["settings"]["show_result"]["correct"]

    @property
    def settings_show_grade(self):
        """Return the Remindo settings:
        correct: grade for the recipe"""
        return self._recipe_dict["settings"]["show_result"]["grade"]

    @property
    def settings_passed(self):
        """Return the Remindo settings:
        correct: passed for the recipe"""
        return self._recipe_dict["settings"]["show_result"]["passed"]

    @property
    def settings_show_result(self):
        """Return the Remindo settings:
        show_result for the recipe"""
        return {
            "given_answer": self._recipe_dict["settings"]["show_result"][
                "given_answer"
            ],
            "correct_answer": self._recipe_dict["settings"]["show_result"][
                "correct_answer"
            ],
            "score": self._recipe_dict["settings"]["show_result"]["score"],
            "correct": self._recipe_dict["settings"]["show_result"]["correct"],
            "grade": self._recipe_dict["settings"]["show_result"]["grade"],
            "passed": self._recipe_dict["settings"]["show_result"]["passed"],
        }

    # Settings: settings

    @property
    def settings_settings_edit_caesura(self):
        """Return the Remindo settings:
        settings: edit_caesura for the recipe"""
        return self._recipe_dict["settings"]["settings"]["edit_caesura"]

    @property
    def settings_settings_bonuspoints(self):
        """Return the Remindo settings:
        settings: bonuspoints for the recipe"""
        return self._recipe_dict["settings"]["settings"]["bonuspoints"]

    @property
    def settings_settings_extra_time(self):
        """Return the Remindo settings:
        settings: extra_time for the recipe"""
        return self._recipe_dict["settings"]["settings"]["extra_time"]

    @property
    def settings_settings_edit_show_result(self):
        """Return the Remindo settings:
        settings: edit_show_result for the recipe"""
        return self._recipe_dict["settings"]["settings"]["edit_show_result"]

    @property
    def settings_settings_edit_retry_delay(self):
        """Return the Remindo settings:
        settings: edit_retry_delay for the recipe"""
        return self._recipe_dict["settings"]["settings"]["edit_retry_delay"]

    @property
    def settings_settings_edit_continue_practice(self):
        """Return the Remindo settings:
        settings: edit_continue_practice for the recipe"""
        return self._recipe_dict["settings"]["settings"]["edit_continue_practice"]

    @property
    def settings_settings(self):
        """Return the Remindo settings:
        settings for the recipe"""
        return {
            "edit_caesura": self._recipe_dict["settings"]["settings"]["edit_caesura"],
            "bonuspoints": self._recipe_dict["settings"]["settings"]["bonuspoints"],
            "extra_time": self._recipe_dict["settings"]["settings"]["extra_time"],
            "edit_show_result": self._recipe_dict["settings"]["settings"][
                "edit_show_result"
            ],
            "edit_retry_delay": self._recipe_dict["settings"]["settings"][
                "edit_retry_delay"
            ],
            "edit_continue_practice": self._recipe_dict["settings"]["settings"][
                "edit_continue_practice"
            ],
        }
