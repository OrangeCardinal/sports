from datetime import date


class NBA_Season_2016(object):
    def __init__(self):
        self.description    = "2016–17 NBA season"
        self.start_date     = date(year=2016,month=10, day=31)
        self.end_date       = date(year=2017, month=4, day=18)

        self.playoff_start_date = date(year=2017, month=4, day=21)
        self.playoff_end_date   = date(year=2017, month=6, day=15)

        self.finals_start_date = date(year=2017, month=6, day=8)
        self.finals_end_date = date(year=2017, month=6, day=20)
