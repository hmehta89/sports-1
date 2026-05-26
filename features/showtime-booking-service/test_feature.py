import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from src.seat import Seat
from src.showtime import ShowTime
from src.movie import Movie
from src.hall import Hall
from src.cinema import Cinema
from src.city import City
from src.customer import Customer
from src.ticket import MovieTicket


def main():
    # Build cinema structure
    show1 = ShowTime(start_time="14:00", end_time="16:30")
    show2 = ShowTime(start_time="19:00", end_time="21:30")
    movie = Movie(title="Interstellar", language="English", genre="Sci-Fi",
                  release_date="2014-11-07", shows=[show1, show2])

    seats = [Seat(number=i) for i in range(1, 11)]
    hall = Hall(number=1, seats=seats)
    cinema = Cinema(name="PVR Cinemas", city="Mumbai", halls=[hall], movies=[movie])
    city = City(name="Mumbai", cinemas=[cinema])

    print(f"Cinema: {cinema.name} in {cinema.city}")
    showtimes = cinema.get_showtimes("Interstellar")
    print(f"Showtimes for Interstellar: {[s.start_time for s in showtimes]}")

    cinemas_showing = city.get_cinemas_showing_movie("Interstellar")
    print(f"Cinemas showing Interstellar in {city.name}: {[c.name for c in cinemas_showing]}")

    # Book tickets
    customer = Customer(name="Alice", email="alice@example.com", phone="9999999999")
    selected_seats = seats[:3]  # seats 1, 2, 3
    booking = customer.book_tickets(show_time=show1, seats=selected_seats)
    print(f"\nBooking created for {customer.name}")
    print(f"  Show: {booking.show_time.start_time} - {booking.show_time.end_time}")
    print(f"  Seats: {[s.number for s in booking.seats]}")

    # Issue tickets
    tickets = [MovieTicket(booking=booking, seat=s) for s in booking.seats]
    print("  Tickets:")
    for t in tickets:
        print(f"    {t}")

    # Verify seats marked booked
    print(f"\nSeat 1 is_booked: {seats[0].is_booked}")
    print(f"Seat 4 is_booked: {seats[3].is_booked}")

    # Attempt double-booking
    try:
        customer.book_tickets(show_time=show2, seats=selected_seats)
    except ValueError as e:
        print(f"\nDouble-booking blocked: {e}")


if __name__ == "__main__":
    main()
