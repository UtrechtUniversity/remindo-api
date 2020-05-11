# content of ./test_moments.py
from remindo_api.moment import RemindoMoment
from remindo_api.result import RemindoResult


def test_isInstanceRemindoRecipe(rclient):
    moments = rclient.list_moments(recipe_ids=2323)
    assert isinstance(moments[0], RemindoMoment)
    assert [3472 == m.rid for m in moments]


def test_isRecipe(rclient):
    moment = rclient.list_moments(recipe_ids=2323)[0]
    assert moment.rid == 3472
    assert moment.code == "ONTKOPPELD"
    assert moment.datasource_id == 2
    assert moment.date_end == "2020-02-24"
    assert moment.date_start == "2020-02-21"
    assert moment.duration == 120
    assert moment.extra_time is None
    assert moment.limit_ips is False
    assert moment.name == "[20200205] BMW11405 - Evolutiebiologie - FT1_BCI"
    assert moment.recipe_id == 2323
    assert moment.recipe_type == "graded practice"
    assert moment.requires_approval is False
    assert moment.recipe_type == "graded practice"
    assert moment.show_result_date is None
    assert moment.show_result_delay == 0
    assert moment.show_result_delay_type == "none"
    assert moment.show_result_time is None
    assert moment.status == "active"
    assert moment.study_id == 86
    assert moment.study_name == "BETA project LearningLytics"
    assert moment.time_end == "2020-02-24 12:30:00"
    assert moment.time_start == "2020-02-21 14:00:00"
    assert moment.type == "period"
    assert moment.api_call_params_recipe_ids == 2323


def test_momentResult(rclient):
    result = rclient.list_moments_results(id=3472)
    for r in result:
        assert isinstance(r, RemindoResult)
    assert [31615 == r.subscription_id for r in result]
    assert [7759 == r.user_code for r in result]
    assert ["[2890, 1781, 2899]" == r.area_feedback for r in result]
    assert [31615 == r.subscription_id for r in result]
    assert result[0].api_call_params_id == 3472
