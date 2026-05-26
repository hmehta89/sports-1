# OOP Design Patterns — Extracted Features

This repository contains nine self-contained feature modules extracted from the open-source [`grokking-the-object-oriented-design-interview`](https://github.com/piyushmani/grokking-the-object-oriented-design-interview) reference repository. Each feature demonstrates a core OOP design pattern — abstract base classes, factories, observers, dataclasses — isolated into a runnable, test-verified Python package. The extraction was performed by the Kompressa extraction-agent (job `7711ded3-xxxx`) using Phase 5 scope discovery to identify cohesive class clusters across multiple subsystems.

---

## Feature 1 — commentary-services-service

Live cricket commentary management: attaches commentators to matches, accumulates comment logs, and retrieves the latest comment.

### Source Files

| File | Source Path in Original Repo | Lines |
|------|-------------------------------|-------|
| `match_type.py` | `Cricinfo/code/enums/match_type.py` | 8 |
| `run_type.py` | `Cricinfo/code/enums/run_type.py` | 7 |
| `match.py` | `Cricinfo/code/models/match.py` | 57 |
| `commentator.py` | `Cricinfo/code/models/commentator.py` | 30 |
| `commentary_service.py` | `Cricinfo/code/services/commentary_service.py` | 10 |

### Key Classes and Methods

- `MatchType` (Enum) — ODI / TEST / T20 constants
- `Match` (ABC) — abstract match base; concrete subclasses `OdiMatch`, `TestMatch`, `T20Match`
- `Commentator` (dataclass) — name, specialization, `increment_matches_commented()`
- `Commentary` (dataclass) — holds a `Match` reference and a list of comment strings; `add_comment()`
- `CommentaryService` — `add_commentary(commentary, commentator, comment)`, `get_latest_commentary(commentary)`

### Test Output

```
Match: India vs Australia at Eden Gardens
Match type: ODI
Commentator: Harsha Bhogle (matches commented: 202)
All commentary:
  Harsha Bhogle: What a magnificent shot!
  Harsha Bhogle: India need 6 off 3 balls.
Latest: Harsha Bhogle: India need 6 off 3 balls.
```

### Extraction Info

- **Job ID:** `7711ded3-xxxx`
- **Extraction phase:** Phase 5 — scope discovery
- **Tool:** Kompressa extraction-agent

---

## Feature 2 — news-publishing-service

Cricket news publication and retrieval service, plus player match statistics and scorecard summaries.

### Source Files

| File | Source Path in Original Repo | Lines |
|------|-------------------------------|-------|
| `news.py` | `Cricinfo/code/models/news.py` | 22 |
| `player.py` | `Cricinfo/code/models/player.py` | 50 |
| `player_stats.py` | `Cricinfo/code/models/player_stats.py` | 15 |
| `scorecard.py` | `Cricinfo/code/models/scorecard.py` | 21 |
| `series.py` | `Cricinfo/code/models/series.py` | 17 |
| `tournament.py` | `Cricinfo/code/models/tournament.py` | 27 |

### Key Classes and Methods

- `News` (dataclass) — title, content, publish_date, author, category
- `NewsService` — `publish_news(news)`, `get_latest_news(category=None)` → returns last 5
- `Player` / `PlayerMatchStats` — player profile + per-match run/wicket/catch stats; `update()`, `display()`
- `PlayerStats` (dataclass) — career aggregates; `get_summary()`
- `Scorecard` (dataclass) — list of `Innings`; `get_match_summary()`
- `Series` / `Tournament` — competition containers with schedule and points table

### Test Output

```
=== All latest news ===
  [cricket] India wins series by Deepak on 2024-11-01
  [cricket] Kohli scores century by Anita on 2024-11-02
  [IPL] IPL 2025 schedule out by Raj on 2024-11-03

=== Cricket category ===
  India wins series
  Kohli scores century

Match Statistics for Virat Kohli:
Runs: 105 (98 balls)
Bowling: 0/0 in 0.0 overs
Catches: 2, Stumpings: 0
Player 1 - Matches: 250, Runs: 12000, Wickets: 4, Average: 55.00

Scorecard: Innings 1: India scored 320/5 | Innings 2: England scored 280/10
```

### Extraction Info

- **Job ID:** `7711ded3-xxxx`
- **Extraction phase:** Phase 5 — scope discovery
- **Tool:** Kompressa extraction-agent

---

## Feature 3 — payment-processing-service

Strategy-pattern payment processing: an abstract `PaymentMethod` base with concrete cash and credit-card implementations.

### Source Files

| File | Source Path in Original Repo | Lines |
|------|-------------------------------|-------|
| `payment_method.py` | `Movie Ticket Booking System/code/payment/payment_method.py` | 6 |
| `cash_payment.py` | `Movie Ticket Booking System/code/payment/cash_payment.py` | 7 |
| `credit_card_payment.py` | `Movie Ticket Booking System/code/payment/credit_card_payment.py` | 7 |

### Key Classes and Methods

- `PaymentMethod` (ABC) — `process_payment(amount: float) -> bool`
- `CashPayment(PaymentMethod)` — prints cash receipt, returns `True`
- `CreditCardPayment(PaymentMethod)` — prints card receipt, returns `True`

### Test Output

```
Processing cash payment of 250.0
Cash payment successful: True
Processing credit card payment of 250.0
Credit card payment successful: True

Polymorphic payment processing:
Processing cash payment of 99.99
  CashPayment: True
Processing credit card payment of 99.99
  CreditCardPayment: True
```

### Extraction Info

- **Job ID:** `7711ded3-xxxx`
- **Extraction phase:** Phase 5 — scope discovery
- **Tool:** Kompressa extraction-agent

---

## Feature 4 — notification-sending-service

Minimal notification dataclass that delivers a message to a named recipient.

### Source Files

| File | Source Path in Original Repo | Lines |
|------|-------------------------------|-------|
| `notification.py` | `Movie Ticket Booking System/code/notification/notification.py` | 8 |

### Key Classes and Methods

- `Notification` (dataclass) — `message: str`; `send(recipient: str)` prints delivery confirmation

### Test Output

```
Sending notification to alice@example.com: Your booking is confirmed!
Sending notification to bob@example.com: Payment of $120.00 received.
Sending notification to carol@example.com: Your show starts in 30 minutes.
All notifications sent.
```

### Extraction Info

- **Job ID:** `7711ded3-xxxx`
- **Extraction phase:** Phase 5 — scope discovery
- **Tool:** Kompressa extraction-agent

---

## Feature 5 — showtime-booking-service

Movie theatre booking system: cinema/hall/seat hierarchy, showtime scheduling, ticket reservation, and double-booking prevention.

### Source Files

| File | Source Path in Original Repo | Lines |
|------|-------------------------------|-------|
| `cinema.py` | `Movie Ticket Booking System/code/cinema/cinema.py` | 19 |
| `city.py` | `Movie Ticket Booking System/code/cinema/city.py` | 11 |
| `hall.py` | `Movie Ticket Booking System/code/cinema/hall.py` | 8 |
| `movie.py` | `Movie Ticket Booking System/code/cinema/movie.py` | 17 |
| `seat.py` | `Movie Ticket Booking System/code/cinema/seat.py` | 6 |
| `showtime.py` | `Movie Ticket Booking System/code/cinema/showtime.py` | 6 |
| `booking.py` | `Movie Ticket Booking System/code/customer/booking.py` | 10 |
| `customer.py` | `Movie Ticket Booking System/code/customer/customer.py` | 28 |
| `ticket.py` | `Movie Ticket Booking System/code/customer/ticket.py` | 11 |

### Key Classes and Methods

- `Seat` (dataclass) — `number`, `is_booked`
- `ShowTime` (dataclass) — `start_time`, `end_time`
- `Hall` (dataclass) — `number`, list of `Seat`
- `Movie` (dataclass) — `title`, `language`, `genre`, list of `ShowTime`; `get_showtimes_in_city()`
- `Cinema` (dataclass) — `get_showtimes(movie_title)`
- `City` (dataclass) — `get_cinemas_showing_movie(movie_title)`
- `Booking` (dataclass) — customer + showtime + seats
- `Customer` (dataclass) — `book_tickets(show_time, seats)` — marks seats booked, raises on conflict
- `MovieTicket` (dataclass) — `__str__` formats seat + time

### Test Output

```
Cinema: PVR Cinemas in Mumbai
Showtimes for Interstellar: ['14:00', '19:00']
Cinemas showing Interstellar in Mumbai: ['PVR Cinemas']

Booking created for Alice
  Show: 14:00 - 16:30
  Seats: [1, 2, 3]
  Tickets:
    Ticket for 14:00 at Seat 1
    Ticket for 14:00 at Seat 2
    Ticket for 14:00 at Seat 3

Seat 1 is_booked: True
Seat 4 is_booked: False

Double-booking blocked: Some seats are already booked
```

### Extraction Info

- **Job ID:** `7711ded3-xxxx`
- **Extraction phase:** Phase 5 — scope discovery
- **Tool:** Kompressa extraction-agent

---

## Feature 6 — library-lending-service

Full library management system with book checkout, return, and fine tracking, using enums for book status and account lifecycle.

### Source Files

| File | Source Path in Original Repo | Lines |
|------|-------------------------------|-------|
| `library_management_system.py` | `Library Management System/code/library_management_system.py` | 264 |

### Key Classes and Methods

- `BookStatus` (Enum) — AVAILABLE / RESERVED / LOANED / LOST
- `AccountStatus` (Enum) — ACTIVE / CLOSED / CANCELED / BLACKLISTED
- `BookItem(Book)` — `checkout(member_id, due_date)`, `update_book_item_status()`
- `BookLending` — static `lend_book(barcode, member_id, due_date)`, `fetch_lending_details()`
- `BookReservation` — static `fetch_reservation_details(barcode)`
- `Librarian(Account)` — `add_book_item()`, `block_member()`, `un_block_member()`
- `Member(Account)` — `checkout_book_item()`, `return_book_item()`, `increment_total_books_checkedout()`
- `Constants` — `MAX_BOOKS_ISSUED_TO_A_USER = 5`, `MAX_LENDING_DAYS = 10`

### Test Output

```
Member: Alice, books checked out: 0
Book: 'Clean Code' status: AVAILABLE
Checkout result: True
Book status after checkout: LOANED
Total books checked out: 1
Book status after return: AVAILABLE
Total books checked out after return: 0
Reference-only checkout result: False
Lending barcode: BC003, due: 2026-06-05
Max books per user: 5
```

### Extraction Info

- **Job ID:** `7711ded3-xxxx`
- **Extraction phase:** Phase 5 — scope discovery
- **Tool:** Kompressa extraction-agent

---

## Feature 7 — member-profile-service

Stack Overflow-style member profile: account identity, reputation, badge collection, and tag creation.

### Source Files

| File | Source Path in Original Repo | Lines |
|------|-------------------------------|-------|
| `account.py` | `Stack Overflow/code/models/account.py` | 18 |
| `member.py` | `Stack Overflow/code/models/member.py` | 22 |
| `badge.py` | `Stack Overflow/code/models/badge.py` | 7 |
| `tag.py` | `Stack Overflow/code/models/tag.py` | 9 |

### Key Classes and Methods

- `AccountStatus` (Enum) — ACTIVE / CLOSED / CANCELED / BLACKLISTED / BLOCKED
- `Account` (dataclass) — id, password, name, email, address, phone, status, reputation; `reset_password()`
- `Badge` (dataclass) — name, description
- `Tag` (dataclass) — name, description, daily/weekly asked frequency
- `Member` (dataclass) — wraps `Account` + badge list; `get_reputation()`, `get_email()`, `create_tag()`

### Test Output

```
Member: John Doe
Email: john@example.com
Reputation: 1500
Status: ACTIVE
Badges: ['Gold', 'Famous Question']
Tag 'python' created by John Doe.
Tag 'python': 50 questions/day
Password for account U001 reset to newpass456.
Password updated: newpass456
```

### Extraction Info

- **Job ID:** `7711ded3-xxxx`
- **Extraction phase:** Phase 5 — scope discovery
- **Tool:** Kompressa extraction-agent

---

## Feature 8 — product-management-service

E-commerce product catalogue: categories, products with inventory, customer accounts, and product reviews.

### Source Files

| File | Source Path in Original Repo | Lines |
|------|-------------------------------|-------|
| `product.py` | `Online Shopping System/code/products/product.py` | 11 |
| `category.py` | `Online Shopping System/code/products/category.py` | 5 |
| `review.py` | `Online Shopping System/code/products/review.py` | 10 |
| `account.py` | `Online Shopping System/code/users/account.py` | 35 |
| `customer.py` | `Online Shopping System/code/users/customer.py` | 13 |

### Key Classes and Methods

- `ProductCategory` (dataclass) — name, description
- `Product` (dataclass) — product_id, name, description, price, category, available_item_count
- `Address` / `Account` (dataclass) — shipping address, status, credit cards; `add_product()`, `reset_password()`
- `Customer` (dataclass) — wraps Account + cart + orders; `add_item_to_cart()`, `place_order()`
- `ProductReview` (dataclass) — rating, review text, product reference, reviewer

### Test Output

```
=== Products ===
  [Electronics] Laptop Pro 15 - $1299.99 (stock: 10)
  [Books] Clean Code - $34.99 (stock: 50)

Customer: Alice Smith
Cart items: ['Laptop Pro 15', 'Clean Code']

Review for 'Laptop Pro 15': 5/5 — Excellent laptop, very fast!
Reviewer: Alice Smith
```

### Extraction Info

- **Job ID:** `7711ded3-xxxx`
- **Extraction phase:** Phase 5 — scope discovery
- **Tool:** Kompressa extraction-agent

---

## Feature 9 — cricket-operations-service

Complete cricket match operations: ball-by-ball innings recording, over management, team/player state, match factory, points table, umpire tracking, and schedule.

### Source Files

| File | Source Path in Original Repo | Lines |
|------|-------------------------------|-------|
| `ball.py` | `Cricinfo/code/models/ball.py` | 14 |
| `innings.py` | `Cricinfo/code/models/innings.py` | 22 |
| `over.py` | `Cricinfo/code/models/over.py` | 17 |
| `playing11.py` | `Cricinfo/code/models/playing11.py` | 13 |
| `points_table.py` | `Cricinfo/code/models/points_table.py` | 23 |
| `run.py` | `Cricinfo/code/models/run.py` | 8 |
| `schedule.py` | `Cricinfo/code/models/schedule.py` | 33 |
| `team.py` | `Cricinfo/code/models/team.py` | 44 |
| `umpire.py` | `Cricinfo/code/models/umpire.py` | 10 |
| `venue.py` | `Cricinfo/code/models/venue.py` | 13 |
| `wicket.py` | `Cricinfo/code/models/wicket.py` | 10 |
| `match_controller.py` | `Cricinfo/code/controllers/match_controller.py` | 38 |
| `match_factory.py` | `Cricinfo/code/services/match_factory.py` | 14 |

### Key Classes and Methods

- `Run` (dataclass) — runs, extras, extra_type
- `Wicket` (dataclass) — batsman, bowler, wicket_type, fielder, wicket_number
- `Ball` (dataclass) — ball_number, run, optional wicket/batsman/bowler, commentary
- `Over` (dataclass) — `add_ball(ball)` accumulates runs and wickets
- `Innings` (dataclass) — `add_over(over)` totals runs/wickets across overs; `update_extras()`
- `Team` / `TeamStat` (dataclass) — `add_player()`, `update_stats(result, run_rate_change)`
- `Playing11` (dataclass) — `substitute_player(out, in)`
- `PointsTable` (dataclass) — `update_team_stats()`, `get_rankings()` sorted by points+NRR
- `Umpire` (dataclass) — `increment_matches_officiated()`
- `Schedule` (dataclass) — `get_schedule_info()`, `get_matches_for_team()`
- `MatchFactory` — static `create_match(match_type, ...)` returns the appropriate `Match` subclass
- `MatchController` — `setup_match(match_type)`, `start_match(match)` — demo orchestrator

### Test Output

```
MCG, Melbourne - Capacity: 100024, Hosted Matches: 50

Match: T20 — India vs Australia
Toss: India elected to Bat

Innings 1 — India
  After over 1: 14 runs, 1 wicket(s)
  Total: 14/1

Playing 11 after sub: ['KL Rahul', 'Jasprit Bumrah']

Points table rankings:
  India: 4 pts, NRR 0.5
  Australia: 2 pts, NRR -0.3

Umpire: Aleem Dar, matches officiated: 201
Match is starting...
Match ID: m001 between Team A and Team B
Venue: Stadium A, Date: 2025-01-01

Schedule:
  2024-12-01: India vs Australia at MCG
  2024-12-05: India vs Australia at MCG
India's matches: 2

Final result: India won by 15 runs
```

### Extraction Info

- **Job ID:** `7711ded3-xxxx`
- **Extraction phase:** Phase 5 — scope discovery
- **Tool:** Kompressa extraction-agent
