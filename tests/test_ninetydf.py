import pandas as pd

from ninetydf import couples, seasons
from ninetydf.data import _load_data


def _validate_dataframe(df, expected_columns):
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    for column in expected_columns:
        assert column in df.columns


def test_load_couples():
    _validate_dataframe(
        couples,
        [
            "show_id",
            "show_name",
            "season",
            "season_id",
            "couple_name",
            "couple_id",
            "appearance_id",
        ],
    )
    expected_len = 129
    assert couples.shape[0] == expected_len

    first_row = couples.iloc[0]
    assert first_row["show_id"] == "90df"
    assert first_row["show_name"] == "90 Day Fiancé"
    assert first_row["appearance_id"] == "russ_paola_90df_1"

    last_row = couples.iloc[expected_len - 1]
    assert last_row["show_id"] == "tow"
    assert last_row["show_name"] == "90 Day Fiancé: The Other Way"
    assert last_row["appearance_id"] == "shekinah_sarper_tow_5"


def test_load_seasons():
    _validate_dataframe(
        seasons, ["show_id", "season", "season_id", "start_date", "end_date"]
    )

    assert seasons.loc[0, "show_id"] == "90df"
    assert seasons.loc[0, "season"] == 1
    assert seasons.loc[0, "season_id"] == "90df_1"
    assert seasons.loc[0, "start_date"] == "2014-01-12"
    assert seasons.loc[0, "end_date"] == "2014-02-23"


def test_load_data_function():
    df = _load_data("seasons.csv")
    _validate_dataframe(df, ["show_id", "season", "start_date", "end_date"])
