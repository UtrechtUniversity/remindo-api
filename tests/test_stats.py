# content of ./test_stats.py
from remindo_api.stats import RemindoStats


def test_isInstanceRemindoStats(rclient):
    stats = rclient.list_stats(recipe_id=2323)
    assert isinstance(stats[0], RemindoStats)


def test_isRemindoStats(rclient):
    stats = rclient.list_stats(recipe_id=2323)
    s = stats[0]
    assert s.item_identifier == "f34647b3-80e6-4854-967d-7766cfeba90e"
    assert s.code == "Fylogenie-14"
    assert s.type == "choice"
    assert s.language == "nl-NL"
    assert s.max_score == 1
    assert s.interaction_count == 1
    assert s.difficulty == 0
    assert s.section == ""
    assert s.p == 0.37037037037037035
    assert s.std == 0.48290388186686284
    assert s.rir == 0.24668183349749834
    assert s.total == 27
    assert s.answered == 27
    assert s.api_call_params_recipe_id == 2323
    assert s.api_call_params_moment_id == 3487
