class Table:
    def __init__(self, players) -> None:
        self.players = players
        self.table_limit = 7
        self.pot = 0
        self.bets = {}
        self.lost_players = []
        self.won_players = []