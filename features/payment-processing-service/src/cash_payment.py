from .payment_method import PaymentMethod

class CashPayment(PaymentMethod):
    def process_payment(self, amount: float) -> bool:
        print(f"Processing cash payment of {amount}")
        return True
