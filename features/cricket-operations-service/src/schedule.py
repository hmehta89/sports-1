from dataclasses import dataclass
from typing import List
from datetime import date
from .match import Match

@dataclass
class Schedule:
    tournament_name: str
    start_date: date
    end_date: date
    matches: List[Match]

    def get_schedule_info(self):
        info = []
        for m in self.matches:
            left = m.teams[0].name if hasattr(m.teams[0], "name") else m.teams[0]["name"]
            right = m.teams[1].name if hasattr(m.teams[1], "name") else m.teams[1]["name"]
            info.append(f"{m.date}: {left} vs {right} at {m.venue.name}")
        return info

    def get_matches_for_team(self, team_name: str):
        relevant = []
        for match in self.matches:
            names = [t.name for t in match.teams] if hasattr(match.teams[0], "name") else [t["name"] for t in match.teams]
            if team_name in names:
                relevant.append(match)
        return relevant
