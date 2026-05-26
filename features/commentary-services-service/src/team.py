from dataclasses import dataclass
from typing import List, Optional
from .player import Player

@dataclass
class Team:
    team_id: int
    name: str
    short_name: str
    flag_url: str
    players: Optional[List[Player]] = None

    def add_player(self, player: Player):
        if self.players is None:
            self.players = []
        self.players.append(player)
