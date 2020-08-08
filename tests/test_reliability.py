# content of ./test_reliability.py
"""Tests for reliability."""
from remindo_api.reliability import RemindoReliability


def test_isInstanceRemindoReliability(rclient):
    """Test function to retrieve an instance of RemindoReliability."""
    r = rclient.list_reliability(recipe_id=2335, moment_id=3487)
    assert isinstance(r, RemindoReliability)


# def test_isRemindoReliability(rclient):
#     r = rclient.list_reliability(recipe_id=2335, moment_id=3487)
#     assert r.alpha ==
#     assert r.sem ==
#     assert r.notes ==
#     assert r.missing_count ==
#     assert r.answer_count ==
#     assert r.stdev ==
#     assert r.average ==
#     assert r.max ==
#     assert r.api_call_params_recipe_id ==
#     assert r.api_call_params_moment_id ==
