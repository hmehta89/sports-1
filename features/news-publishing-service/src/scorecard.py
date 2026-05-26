from dataclasses import dataclass
from typing import List
from .match import Match

@dataclass
class Innings:
    innings_id: int
    batting_team: "Team"
    bowling_team: "Team"
    total_runs: int = 0
    wickets: int = 0

@dataclass
class Scorecard:
    scorecard_id: int
    match: Match
    innings: List[Innings]

    def add_innings(self, innings: Innings):
        self.innings.append(innings)

    def get_match_summary(self) -> str:
        parts = []
        for i, inn in enumerate(self.innings, start=1):
            parts.append(
                f"Innings {i}: {inn.batting_team.name} "
                f"scored {inn.total_runs}/{inn.wickets}"
            )
        return " | ".join(parts)
