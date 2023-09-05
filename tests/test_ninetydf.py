import pandas as pd

from ninetydf import couples, seasons
from ninetydf.data import _load_data


def test_load_couples():
    assert isinstance(couples, pd.DataFrame)
    assert not couples.empty
    assert "show_id" in couples.columns
    assert "couple_name" in couples.columns
    assert couples["show_id"].notnull().all()
    assert couples["couple_name"].notnull().all()


def test_load_seasons():
    assert isinstance(seasons, pd.DataFrame)
    assert not seasons.empty
    assert "show_id" in seasons.columns
    assert "season" in seasons.columns
    assert seasons["show_id"].notnull().all()
    assert seasons["season"].notnull().all()


def test_load_data_function():
    df = _load_data("seasons.csv")
    assert not df.empty
    assert isinstance(df, pd.DataFrame)
