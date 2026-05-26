import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from src.payment_method import PaymentMethod
from src.cash_payment import CashPayment
from src.credit_card_payment import CreditCardPayment


def main():
    amount = 250.00

    cash = CashPayment()
    result = cash.process_payment(amount)
    print(f"Cash payment successful: {result}")

    card = CreditCardPayment()
    result = card.process_payment(amount)
    print(f"Credit card payment successful: {result}")

    # Demonstrate polymorphism
    methods = [CashPayment(), CreditCardPayment()]
    print("\nPolymorphic payment processing:")
    for method in methods:
        ok = method.process_payment(99.99)
        print(f"  {method.__class__.__name__}: {ok}")


if __name__ == "__main__":
    main()
