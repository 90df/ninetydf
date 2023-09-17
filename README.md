# ninetydf

90 Day Fiancé dataframes

## Example usage

```python
from ninetydf import couples, seasons


def main():
    print(couples.head(10))
    print(seasons.head(10))


if __name__ == "__main__":
    main()

```

**Output**:

```bash
  show_id      show_name  season season_id         couple_name         couple_id            appearance_id
0    90DF  90 Day Fiancé       1    90DF_1        Russ & Paola        russ_paola        russ_paola_90DF_1
1    90DF  90 Day Fiancé       1    90DF_1      Alan & Kirlyam      alan_kirlyam      alan_kirlyam_90DF_1
2    90DF  90 Day Fiancé       1    90DF_1         Louis & Aya         louis_aya         louis_aya_90DF_1
3    90DF  90 Day Fiancé       1    90DF_1        Mike & Aziza        mike_aziza        mike_aziza_90DF_1
4    90DF  90 Day Fiancé       2    90DF_2     Chelsea & Yamir     chelsea_yamir     chelsea_yamir_90DF_2
5    90DF  90 Day Fiancé       2    90DF_2  Danielle & Mohamed  danielle_mohamed  danielle_mohamed_90DF_2
6    90DF  90 Day Fiancé       2    90DF_2     Justin & Evelin     justin_evelin     justin_evelin_90DF_2
7    90DF  90 Day Fiancé       2    90DF_2        Brett & Daya        brett_daya        brett_daya_90DF_2
8    90DF  90 Day Fiancé       2    90DF_2      Jason & Cássia      jason_cássia      jason_cássia_90DF_2
9    90DF  90 Day Fiancé       2    90DF_2         Danny & Amy         danny_amy         danny_amy_90DF_2
  show_id                          show_name  season season_id  start_date    end_date
0    90DF                      90 Day Fiancé       1    90DF_1  2014-01-12  2014-02-23
1    90DF                      90 Day Fiancé       2    90DF_2  2014-10-19  2014-12-28
2    90DF                      90 Day Fiancé       3    90DF_3  2015-10-11  2015-12-06
3    90DF                      90 Day Fiancé       4    90DF_4  2016-08-22  2016-11-20
4    90DF                      90 Day Fiancé       5    90DF_5  2017-10-08  2017-12-18
5    90DF                      90 Day Fiancé       6    90DF_6  2018-10-21  2019-01-13
6    90DF                      90 Day Fiancé       7    90DF_7  2019-11-03  2020-02-17
7    90DF                      90 Day Fiancé       8    90DF_8  2020-12-06  2021-02-21
8    90DF                      90 Day Fiancé       9    90DF_9  2022-04-17  2022-08-21
9     B90  90 Day Fiancé: Before the 90 Days       1     B90_1  2017-08-06  2017-10-30
```

## Disclaimer

The data provided in this repository related to "90 Day Fiancé" (the "Data")
is intended for educational and research purposes only. The Data might be
copyrighted and/or subject to other legal protections.
By using the Data, users agree:

1. Not to use the Data for commercial purposes.
2. To use the Data in a fair and ethical manner, respecting the rights of the original creators and copyright holders.
3. That they are solely responsible for any legal implications or violations arising from their use of the Data.
4. Not to distribute or reproduce the Data without explicit permission from the original copyright holders.
5. To provide proper attribution when referencing the Data in any publications or outputs.

**This repository and its maintainers are not affiliated with, endorsed by,
or sponsored by the creators or copyright holders of "90 Day Fiancé".**
Any use of the Data is at the user's own risk, and the maintainers
of this repository disclaim any and all liability related thereto.
