# ninetydf

90 Day Fiancé dataframes

## Example usage

```python
from ninetydf import couples, seasons


def main():
    print(couples.head())
    print(seasons.head())


if __name__ == "__main__":
    main()

```

**Output**:

```bash
  show_id      show_name  season      couple_name
0    90df  90 Day Fiancé       1     Russ & Paola
1    90df  90 Day Fiancé       1   Alan & Kirlyam
2    90df  90 Day Fiancé       1      Louis & Aya
3    90df  90 Day Fiancé       1     Mike & Aziza
4    90df  90 Day Fiancé       2  Chelsea & Yamir
  show_id      show_name  season  start_date    end_date
0    90df  90 Day Fiancé       1  2014-01-12  2014-02-23
1    90df  90 Day Fiancé       2  2014-10-19  2014-12-28
2    90df  90 Day Fiancé       3  2015-10-11  2015-12-06
3    90df  90 Day Fiancé       4  2016-08-22  2016-11-20
4    90df  90 Day Fiancé       5  2017-10-08  2017-12-18
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