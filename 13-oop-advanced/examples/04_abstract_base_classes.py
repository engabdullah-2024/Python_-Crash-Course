# Enforcing a subclass contract with abc.ABC, plus composition vs inheritance.

from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        """Every payment method must implement pay()."""

    def receipt(self, amount):
        # a concrete (non-abstract) method that subclasses inherit for free
        return f"Charged ${amount:.2f} via {type(self).__name__}"


class CreditCard(PaymentMethod):
    def pay(self, amount):
        return f"Approved ${amount:.2f} on credit card"


class PayPal(PaymentMethod):
    def pay(self, amount):
        return f"Sent ${amount:.2f} via PayPal"


class Checkout:
    """Composition: Checkout HAS-A PaymentMethod, it doesn't inherit from one."""

    def __init__(self, payment_method: PaymentMethod):
        self.payment_method = payment_method

    def complete(self, amount):
        print(self.payment_method.pay(amount))
        print(self.payment_method.receipt(amount))


if __name__ == "__main__":
    for method in (CreditCard(), PayPal()):
        Checkout(method).complete(49.99)
        print("-" * 30)

    try:
        PaymentMethod()  # cannot instantiate an abstract class
    except TypeError as e:
        print(f"Blocked: {e}")
