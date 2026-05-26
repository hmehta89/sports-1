import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from src.player import Player
from src.team import Team, TeamStat
from src.venue import Venue
from src.run import Run
from src.wicket import Wicket
from src.ball import Ball
from src.over import Over
from src.innings import Innings
from src.match import OdiMatch, T20Match
from src.match_type import MatchType
from src.match_factory import MatchFactory
from src.match_controller import MatchController
from src.playing11 import Playing11
from src.points_table import PointsTable
from src.umpire import Umpire
from src.schedule import Schedule
import datetime


def main():
    # Teams and players
    rohit = Player(1, "Rohit Sharma", "batsman", "right-handed", "right-arm medium")
    bumrah = Player(2, "Jasprit Bumrah", "bowler", "right-handed", "right-arm fast")
    team_india = Team(1, "India", "IND", "")
    team_india.add_player(rohit)
    team_india.add_player(bumrah)

    smith = Player(3, "Steve Smith", "batsman", "right-handed", "right-arm leg-break")
    starc = Player(4, "Mitchell Starc", "bowler", "left-handed", "left-arm fast")
    team_aus = Team(2, "Australia", "AUS", "")
    team_aus.add_player(smith)
    team_aus.add_player(starc)

    # Venue
    venue = Venue(1, "MCG", "Melbourne", "Australia", 100024, 50)
    print(venue.get_venue_info())

    # Match via factory
    match = MatchFactory.create_match(
        MatchType.T20,
        match_id="T20-001",
        teams=[team_india, team_aus],
        venue=venue,
        date="2024-12-01",
        start_time="19:30"
    )
    print(f"\nMatch: {match.get_match_type()} — {team_india.name} vs {team_aus.name}")
    match.set_toss_winner(team_india)
    match.set_toss_decision("Bat")
    print(f"Toss: {match.toss_winner.name} elected to {match.toss_decision}")

    # Build an innings with overs and balls
    innings = Innings(innings_id=1, batting_team=team_india, bowling_team=team_aus)
    over1 = Over(over_number=1, bowler=starc)
    over1.add_ball(Ball(1, Run(4), batsman=rohit, bowler=starc, commentary="Boundary!"))
    over1.add_ball(Ball(2, Run(6), batsman=rohit, bowler=starc, commentary="Six!"))
    over1.add_ball(Ball(3, Run(1)))
    wicket = Wicket(batsman=rohit, bowler=starc, wicket_type="bowled", wicket_number=1)
    over1.add_ball(Ball(4, Run(0), wicket=wicket, commentary="Wicket!"))
    over1.add_ball(Ball(5, Run(2)))
    over1.add_ball(Ball(6, Run(1)))
    innings.add_over(over1)

    print(f"\nInnings 1 — {innings.batting_team.name}")
    print(f"  After over {over1.over_number}: {over1.runs_conceded} runs, {over1.wickets_taken} wicket(s)")
    print(f"  Total: {innings.total_runs}/{innings.wickets}")

    # Playing 11
    playing11 = Playing11(team=team_india, players=[rohit, bumrah])
    sub = Player(5, "KL Rahul", "batsman", "right-handed", "right-arm medium")
    playing11.substitute_player(rohit, sub)
    print(f"\nPlaying 11 after sub: {[p.name for p in playing11.players]}")

    # Points table
    stat_ind = TeamStat(team_india, 3, 2, 1, 0, 4, 0.5)
    stat_aus = TeamStat(team_aus, 3, 1, 2, 0, 2, -0.3)
    pt = PointsTable(points_table_id=1, team_stats=[stat_ind, stat_aus])
    print("\nPoints table rankings:")
    for s in pt.get_rankings():
        print(f"  {s.team.name}: {s.points} pts, NRR {s.net_run_rate}")

    # Umpire
    ump = Umpire(1, "Aleem Dar", "Pakistan", 200)
    ump.increment_matches_officiated()
    print(f"\nUmpire: {ump.name}, matches officiated: {ump.matches_officiated}")

    # MatchController
    ctrl = MatchController()
    setup_match = ctrl.setup_match(MatchType.ODI)
    ctrl.start_match(setup_match)

    # Schedule
    match2 = MatchFactory.create_match(
        MatchType.ODI, match_id="ODI-001",
        teams=[team_india, team_aus], venue=venue,
        date="2024-12-05", start_time="09:30"
    )
    schedule = Schedule(
        tournament_name="India vs Australia Series",
        start_date=datetime.date(2024, 12, 1),
        end_date=datetime.date(2024, 12, 10),
        matches=[match, match2]
    )
    print("\nSchedule:")
    for info in schedule.get_schedule_info():
        print(f"  {info}")
    ind_matches = schedule.get_matches_for_team("India")
    print(f"India's matches: {len(ind_matches)}")

    match.update_result("India won by 15 runs")
    print(f"\nFinal result: {match.result}")


if __name__ == "__main__":
    main()
