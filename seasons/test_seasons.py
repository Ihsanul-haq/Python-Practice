from seasons.seasons import season_of_birth
def test_season_of_birth():
    assert season_of_birth(1) == "winter"
    assert season_of_birth(7) == "summer"
    assert season_of_birth(4) == "spring"