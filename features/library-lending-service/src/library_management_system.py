from abc import ABC
from dataclasses import dataclass
import datetime
from enum import Enum

import logging
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)


class BookFormat(Enum):
    HARDCOVER, PAPERBACK, AUDIO_BOOK, EBOOK, NEWSPAPER, MAGAZINE, JOURNAL = 1, 2, 3, 4, 5, 6, 7

class BookStatus(Enum):
    AVAILABLE, RESERVED, LOANED, LOST = 1, 2, 3, 4

class ReservationStatus(Enum):
    WAITING, PENDING, CANCELED, NONE = 1, 2, 3, 4

class AccountStatus(Enum):
    ACTIVE, CLOSED, CANCELED, BLACKLISTED, NONE = 1, 2, 3, 4, 5

@dataclass
class Address:
    street_address: str
    city: str
    state: str
    zip_code: int
    country: str

@dataclass
class Person(ABC):
    name: str
    address: Address
    email: str
    phone: str

@dataclass
class Constants:
    MAX_BOOKS_ISSUED_TO_A_USER: int = 5
    MAX_LENDING_DAYS: int = 10

@dataclass
class Account(ABC):
    id: str
    password: str
    person: Person
    status: AccountStatus = AccountStatus.ACTIVE

    def reset_password(self):
        None

@dataclass
class Rack:
    number: int
    location_identifie: str

@dataclass
class Book(ABC):
    ISBN: str
    title: str
    subject: str
    publisher: str
    language: str
    number_of_pages: int
    authors: list

@dataclass
class BookItem(Book):
    barcode: str
    is_reference_only: bool
    borrowed: bool
    due_date: datetime.date
    price: float
    status: BookStatus
    date_of_purchase: datetime.date
    publication_date: datetime.date
    placed_at: Rack

    def get_is_reference_only(self):
        return self.is_reference_only

    def get_is_available(self):
        return self.status == BookStatus.AVAILABLE

    def update_book_item_status(self, status):
        self.status = status

    def checkout(self, member_id, due_date):
        if self.get_is_reference_only():
            logging.info("This book is Reference only and can't be issued")
            return False
        if not self.get_is_available():
            logging.error("Book is already LOANED")
            return False
        lending = BookLending.lend_book(self.barcode, member_id, due_date)
        self.update_book_item_status(BookStatus.LOANED)
        return lending

@dataclass
class BookReservation:
    status: BookStatus
    book_item_barcode: str
    member_id: int
    creation_date: datetime.date = datetime.date.today()

    @staticmethod
    def fetch_reservation_details(barcode):
        return None

@dataclass
class BookLending:
    book_item_barcode: str
    member_id: int
    due_date: datetime.date
    return_date: datetime.date = None
    creation_date: datetime.date = datetime.date.today()

    @staticmethod
    def lend_book(barcode, member_id, due_date):
        return BookLending(barcode, member_id, due_date)

    @staticmethod
    def fetch_lending_details(barcode):
        return None

@dataclass
class Fine:
    book_item_barcode: str
    member_id: int
    creation_date: datetime.date = datetime.date.today()

    def collect_fine(self, member_id, days):
        None

@dataclass
class Librarian(Account):
    department: str = ""

    def add_book_item(self, book_item):
        None

    def block_member(self, member):
        None

    def un_block_member(self, member):
        None

@dataclass
class Member(Account):
    date_of_membership: datetime.date = datetime.date.today()
    total_books_checkedout: int = 0

    def get_total_books_checked_out(self):
        return self.total_books_checkedout

    def reserve_book_item(self, book_item):
        None

    def increment_total_books_checkedout(self):
        self.total_books_checkedout += 1

    def decrement_total_books_checkedout(self):
        self.total_books_checkedout -= 1

    def checkout_book_item(self, book_item, due_date):
        if self.get_total_books_checked_out() >= Constants.MAX_BOOKS_ISSUED_TO_A_USER:
            logging.error("The user has already checked-out maximum number of books")
            return False
        book_reservation = BookReservation.fetch_reservation_details(book_item.barcode)
        if book_reservation is not None and book_reservation.member_id != self.id:
            print("This book is reserved by another member")
            return False
        checkout_result = book_item.checkout(self.id, due_date)
        if not checkout_result:
            return False
        self.increment_total_books_checkedout()
        logging.info(f"member {self.id} loaned the book, {book_item.title}")
        return checkout_result

    def return_book_item(self, book_item):
        book_reservation = BookReservation.fetch_reservation_details(book_item.barcode)
        if book_reservation is not None:
            book_item.update_book_item_status(BookStatus.RESERVED)
        book_item.update_book_item_status(BookStatus.AVAILABLE)
        self.decrement_total_books_checkedout()
        logging.info(f"member {self.id} returned the book, {book_item.title}")
