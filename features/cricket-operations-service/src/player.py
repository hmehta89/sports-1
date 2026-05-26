from dataclasses import dataclass
from typing import Optional

@dataclass
class Player:
    player_id: int
    name: str
    role: str
    batting_style: str
    bowling_style: str
    date_of_birth: Optional[str] = None
    nationality: Optional[str] = None
