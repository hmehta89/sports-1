from dataclasses import dataclass, field
from typing import List
from .booking import Booking
from .seat import Seat
from .showtime import ShowTime

@dataclass
class Customer:
    name: str
    email: str
    phone: str
    bookings: List[Booking] = field(default_factory=list)

    def book_tickets(self, show_time: ShowTime, seats: List[Seat]) -> Booking:
        """Reserve seats and return a Booking. Raises ValueError if any seat is already booked."""
        if not all(not seat.is_booked for seat in seats):
            raise ValueError("Some seats are already booked")
        for seat in seats:
            seat.is_booked = True
        booking = Booking(customer=self, show_time=show_time, seats=seats)
        self.bookings.append(booking)
        return booking
