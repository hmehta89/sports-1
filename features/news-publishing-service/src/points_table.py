from dataclasses import dataclass
from typing import List
from .team import TeamStat

@dataclass
class PointsTable:
    points_table_id: int
    team_stats: List[TeamStat]

    def get_rankings(self) -> List[TeamStat]:
        return sorted(
            self.team_stats,
            key=lambda x: (x.points, x.net_run_rate),
            reverse=True
        )
