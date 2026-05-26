import sys
import os
import datetime
import logging
logging.disable(logging.CRITICAL)  # suppress logging noise in test output

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from src.library_management_system import (
    Address, Person, Account, AccountStatus,
    BookItem, BookStatus, BookLending, BookReservation,
    Rack, Librarian, Member, Constants
)


# Concrete subclass of Person (ABC requires all fields via dataclass)
from dataclasses import dataclass

@dataclass
class ConcretePerson(Person):
    pass


def make_member(mid, name):
    addr = Address("123 Main St", "Springfield", "IL", 62701, "USA")
    person = ConcretePerson(name=name, address=addr, email=f"{name.lower()}@lib.com", phone="555-1234")
    return Member(id=mid, password="secret", person=person)


def make_book_item(barcode, title, reference_only=False):
    rack = Rack(number=1, location_identifie="A1")
    return BookItem(
        ISBN="978-0-13-468599-1",
        title=title,
        subject="Computing",
        publisher="Addison-Wesley",
        language="English",
        number_of_pages=300,
        authors=["Author A"],
        barcode=barcode,
        is_reference_only=reference_only,
        borrowed=False,
        due_date=datetime.date.today() + datetime.timedelta(days=10),
        price=49.99,
        status=BookStatus.AVAILABLE,
        date_of_purchase=datetime.date(2020, 1, 1),
        publication_date=datetime.date(2019, 6, 1),
        placed_at=rack
    )


def main():
    member = make_member("M001", "Alice")
    book = make_book_item("BC001", "Clean Code")
    due = datetime.date.today() + datetime.timedelta(days=10)

    print(f"Member: {member.person.name}, books checked out: {member.total_books_checkedout}")
    print(f"Book: '{book.title}' status: {book.status.name}")

    # Checkout
    result = member.checkout_book_item(book, due)
    print(f"Checkout result: {result is not False}")
    print(f"Book status after checkout: {book.status.name}")
    print(f"Total books checked out: {member.total_books_checkedout}")

    # Return
    member.return_book_item(book)
    print(f"Book status after return: {book.status.name}")
    print(f"Total books checked out after return: {member.total_books_checkedout}")

    # Reference-only book checkout attempt
    ref_book = make_book_item("BC002", "Encyclopedia", reference_only=True)
    result2 = member.checkout_book_item(ref_book, due)
    print(f"Reference-only checkout result: {result2}")

    # BookLending direct test
    lending = BookLending.lend_book("BC003", "M001", due)
    print(f"Lending barcode: {lending.book_item_barcode}, due: {lending.due_date}")

    # Constants
    print(f"Max books per user: {Constants.MAX_BOOKS_ISSUED_TO_A_USER}")


if __name__ == "__main__":
    main()
