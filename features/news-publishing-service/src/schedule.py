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
