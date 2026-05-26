import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from src.match import OdiMatch
from src.venue import Venue
from src.team import Team
from src.commentator import Commentator, Commentary
from src.commentary_service import CommentaryService


def main():
    venue = Venue(venue_id=1, name="Eden Gardens", city="Kolkata", country="India",
                  capacity=66000, hosted_matches=25)
    team1 = Team(team_id=1, name="India", short_name="IND", flag_url="")
    team2 = Team(team_id=2, name="Australia", short_name="AUS", flag_url="")

    match = OdiMatch(match_id=101, teams=[team1, team2], venue=venue,
                     date="2024-11-10", start_time="09:30")

    commentary = Commentary(commentary_id=1, match=match)
    commentator = Commentator(commentator_id=1, name="Harsha Bhogle",
                               specialization="ODI", matches_commented=200)

    service = CommentaryService()
    service.add_commentary(commentary, commentator, "What a magnificent shot!")
    service.add_commentary(commentary, commentator, "India need 6 off 3 balls.")

    print(f"Match: {team1.name} vs {team2.name} at {venue.name}")
    print(f"Match type: {match.get_match_type()}")
    print(f"Commentator: {commentator.name} (matches commented: {commentator.matches_commented})")
    print("All commentary:")
    for c in commentary.comments:
        print(f"  {c}")
    latest = service.get_latest_commentary(commentary)
    print(f"Latest: {latest}")


if __name__ == "__main__":
    main()
