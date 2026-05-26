from dataclasses import dataclass, field
from .account import Account
from .badge import Badge
from .tag import Tag

@dataclass
class Member:
    account: Account
    badges: list = field(default_factory=list)

    def get_reputation(self):
        return self.account.reputation

    def get_email(self):
        return self.account.email

    def create_question(self, question):
        print(f"Question '{question.title}' created by {self.account.name}.")

    def create_tag(self, tag: Tag):
        print(f"Tag '{tag.name}' created by {self.account.name}.")
