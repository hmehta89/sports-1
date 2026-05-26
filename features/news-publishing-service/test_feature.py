import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from src.news import News, NewsService
from src.player import Player, PlayerMatchStats
from src.player_stats import PlayerStats
from src.scorecard import Scorecard, Innings
from src.team import Team
from src.venue import Venue
from src.match import OdiMatch
from src.series import Series
from src.schedule import Schedule
from src.points_table import PointsTable, TeamStat
from src.tournament import Tournament
import datetime


def main():
    # NewsService demo
    service = NewsService()
    n1 = News(1, "India wins series", "India beat England 3-0.", "2024-11-01", "Deepak", "cricket")
    n2 = News(2, "Kohli scores century", "Virat Kohli hits 105* in final ODI.", "2024-11-02", "Anita", "cricket")
    n3 = News(3, "IPL 2025 schedule out", "BCCI releases schedule.", "2024-11-03", "Raj", "IPL")
    service.publish_news(n1)
    service.publish_news(n2)
    service.publish_news(n3)

    print("=== All latest news ===")
    for n in service.get_latest_news():
        print(f"  [{n.category}] {n.title} by {n.author} on {n.publish_date}")

    print("\n=== Cricket category ===")
    for n in service.get_latest_news("cricket"):
        print(f"  {n.title}")

    # Player stats demo
    p = Player(1, "Virat Kohli", "batsman", "right-handed", "right-arm medium")
    stats = PlayerMatchStats(p)
    stats.update(runs=105, balls_faced=98, catches=2)
    print()
    stats.display()

    ps = PlayerStats(player_id=1, matches=250, runs=12000, wickets=4, average=55.0)
    print(ps.get_summary())

    # Scorecard demo
    team1 = Team(1, "India", "IND", "")
    team2 = Team(2, "England", "ENG", "")
    venue = Venue(1, "Lord's", "London", "England", 30000, 100)
    match = OdiMatch(match_id=1, teams=[team1, team2], venue=venue, date="2024-11-01", start_time="10:00")
    inn1 = Innings(innings_id=1, batting_team=team1, bowling_team=team2, total_runs=320, wickets=5)
    inn2 = Innings(innings_id=2, batting_team=team2, bowling_team=team1, total_runs=280, wickets=10)
    scorecard = Scorecard(scorecard_id=1, match=match, innings=[inn1, inn2])
    print(f"\nScorecard: {scorecard.get_match_summary()}")


if __name__ == "__main__":
    main()
