from typing import List, Optional
from abc import ABC, abstractmethod
from .team import Team
from .venue import Venue

class Match(ABC):
    def __init__(self, match_id, teams, venue, date, start_time,
                 toss_winner=None, toss_decision=None, result=None, man_of_the_match=None):
        self.match_id = match_id
        self.teams = teams
        self.venue = venue
        self.date = date
        self.start_time = start_time
        self.toss_winner = toss_winner
        self.toss_decision = toss_decision
        self.result = result
        self.man_of_the_match = man_of_the_match

    @abstractmethod
    def get_match_type(self) -> str:
        pass

class OdiMatch(Match):
    def get_match_type(self) -> str:
        return "ODI"
