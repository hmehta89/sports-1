from dataclasses import dataclass
from typing import List
from .seat import Seat
from .showtime import ShowTime

@dataclass
class Booking:
    customer: "Customer"
    show_time: ShowTime
    seats: List[Seat]
