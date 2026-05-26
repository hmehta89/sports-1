import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from src.account_status import AccountStatus
from src.account import Account
from src.badge import Badge
from src.tag import Tag
from src.member import Member


def main():
    account = Account(
        id="U001",
        password="pass123",
        name="John Doe",
        email="john@example.com",
        address="123 Main St, NYC",
        phone=5551234567,
        status=AccountStatus.ACTIVE,
        reputation=1500
    )

    badge1 = Badge(name="Gold", description="Awarded for 1000 upvotes")
    badge2 = Badge(name="Famous Question", description="Asked a question with 10k views")

    member = Member(account=account, badges=[badge1, badge2])

    print(f"Member: {member.account.name}")
    print(f"Email: {member.get_email()}")
    print(f"Reputation: {member.get_reputation()}")
    print(f"Status: {member.account.status.name}")
    print(f"Badges: {[b.name for b in member.badges]}")

    # Add a tag
    tag = Tag(name="python", description="Python programming language",
              daily_asked_frequency=50, weekly_asked_frequency=300)
    member.create_tag(tag)
    print(f"Tag '{tag.name}': {tag.daily_asked_frequency} questions/day")

    # Reset password
    account.reset_password("newpass456")
    print(f"Password updated: {account.password}")


if __name__ == "__main__":
    main()
