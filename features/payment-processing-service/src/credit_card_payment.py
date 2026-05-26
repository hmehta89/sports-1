from .payment_method import PaymentMethod

class CreditCardPayment(PaymentMethod):
    def process_payment(self, amount: float) -> bool:
        print(f"Processing credit card payment of {amount}")
        return True
