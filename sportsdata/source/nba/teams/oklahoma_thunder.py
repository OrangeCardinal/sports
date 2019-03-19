from sportsdata.source.nba.team import NBA_Team


class OklahomaThunder(NBA_Team):
    """
    NBA Golden State Warriors Static Information

    """

    def __init__(self):
        """
        """
        super().__init__()
        self.full_name  = "Oklahoma Thunder"
        self.name       = "Thunder"
        self.team_id    = None