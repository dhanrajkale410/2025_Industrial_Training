# Task 2: Abstraction
# 1. Import ABC and abstractmethod from abc.
# * Create an abstract class PaymentMethod with an abstract method pay(amount).
# * Create two child classes: CreditCard and UPI, each implementing their version of pay().
# * Instantiate each class and call pay() to show different payment methods.

from abc import ABC, abstractmethod

# Abstract class
class PaymentMethod(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

# Concrete class: CreditCard
class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card.")

# Concrete class: UPI
class UPI(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI.")

# Instantiate each class and call pay()
credit_card_payment = CreditCard()
upi_payment = UPI()

credit_card_payment.pay(1500)
upi_payment.pay(750)
