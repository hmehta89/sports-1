from dataclasses import dataclass, field
from typing import List, Optional
from .match import Match

@dataclass
class Commentator:
    commentator_id: int
    name: str
    specialization: str
    matches_commented: int

    def increment_matches_commented(self):
        self.matches_commented += 1

@dataclass
class Commentary:
    commentary_id: int
    match: Match
    comments: List[str] = field(default_factory=list)

    def add_comment(self, comment: str):
        self.comments.append(comment)
