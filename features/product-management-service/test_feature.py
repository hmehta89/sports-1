import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from src.category import ProductCategory
from src.product import Product
from src.account import Account, AccountStatus, Address
from src.customer import Customer
from src.review import ProductReview


def main():
    # Categories
    electronics = ProductCategory(name="Electronics", description="Electronic gadgets")
    books = ProductCategory(name="Books", description="Printed and digital books")

    # Products
    p1 = Product(product_id=1, name="Laptop Pro 15", description="High-performance laptop",
                 price=1299.99, category=electronics, available_item_count=10)
    p2 = Product(product_id=2, name="Clean Code", description="Book by Robert C. Martin",
                 price=34.99, category=books, available_item_count=50)

    print("=== Products ===")
    for p in [p1, p2]:
        print(f"  [{p.category.name}] {p.name} - ${p.price:.2f} (stock: {p.available_item_count})")

    # Customer
    addr = Address("1 Infinite Loop", "Cupertino", "CA", 95014, "USA")
    account = Account(username="alice", password="s3cr3t", name="Alice Smith",
                      email="alice@shop.com", phone="555-0101",
                      shipping_address=addr, status=AccountStatus.ACTIVE)
    customer = Customer(account=account)

    customer.add_item_to_cart(p1)
    customer.add_item_to_cart(p2)
    print(f"\nCustomer: {customer.account.name}")
    print(f"Cart items: {[item.name for item in customer.cart]}")

    # Review
    review = ProductReview(rating=5, review="Excellent laptop, very fast!",
                           product=p1, reviewer=customer)
    print(f"\nReview for '{review.product.name}': {review.rating}/5 — {review.review}")
    print(f"Reviewer: {review.reviewer.account.name}")


if __name__ == "__main__":
    main()
