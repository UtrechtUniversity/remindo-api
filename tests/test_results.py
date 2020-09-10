# content of ./test_result.py
"""Tests for RemindoResult."""
from remindo_api.result import RemindoResult


def test_isInstanceRemindoResult(rclient):
    """Test function to retrieve an instance of RemindoResult."""
    results = rclient.list_results(recipe_ids=2335)
    assert isinstance(results[0], RemindoResult)


def test_isRemindoRemindoResult(rclient):
    """Test function to check the validity of RemindoResult."""
    results = rclient.list_results(recipe_ids=2335)
    r = results[0]
    assert r.subscription_id == 31531
    assert r.user_id == 4522
    assert r.user_code == ""
    assert r.cluster_ids is list()
    assert r.area_feedback == ""
    assert r.area_name == "Onvoldoende"
    assert r.try_count == 0
    assert r.result_id == 29536
    assert r.recipe_id == 2335
    assert r.recipe_type == "graded practice"
    assert r.recipe_name == "[20200210] BMW11405 - Evolutiebiologie - FT6_Fylogenie"
    assert r.recipe_code == ""
    assert r.recipe_category is None
    assert r.recipe_source_id == "bd7b5216-4786-4e93-a298-d0334d12b016-107-0-3325"
    assert r.study_id == 86
    assert r.study_name == "BETA project LearningLytics"
    assert r.status == "closed"
    assert r.start_time == "2020-02-03 20:02:20"
    assert r.end_time == "2020-02-04 06:45:12"
    assert r.max_score == 14
    assert r.score == 0
    assert r.grade == 1
    assert r.i_count == 14
    assert r.i_right == 0
    assert r.i_answered == 0
    assert r.i_review == 0
    assert r.i_correct == 0
    assert r.i_incorrect == 0
    assert r.i_mostlycorrect == 0
    assert r.i_mostlyincorrect == 0
    assert r.show_given_answer == "none"
    assert r.show_score is False
    assert r.show_correct is True
    assert r.show_grade is False
    assert r.show_passed is False
    assert r.report_data is False
    assert r.passed is False
