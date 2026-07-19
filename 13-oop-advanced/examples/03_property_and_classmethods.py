# @property, @classmethod, and @staticmethod in a small BankAccount model.


class BankAccount:
    interest_rate = 0.02  # class attribute, shared unless overridden

    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    @property
    def balance(self):
        """Read-only view of the balance -- can't be set directly."""
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Insufficient funds.")
        self._balance -= amount

    @property
    def balance_with_interest(self):
        """Computed property: what the balance would be after one year."""
        return round(self._balance * (1 + self.interest_rate), 2)

    @classmethod
    def open_with_bonus(cls, owner):
        """Alternative constructor: new accounts start with a signup bonus."""
        return cls(owner, balance=50)

    @staticmethod
    def is_valid_owner_name(name):
        """A helper that belongs conceptually to BankAccount but needs no state."""
        return isinstance(name, str) and len(name.strip()) > 0


if __name__ == "__main__":
    acc = BankAccount("Priya", balance=1000)
    acc.deposit(250)
    acc.withdraw(100)
    print(f"{acc.owner}'s balance: {acc.balance}")
    print(f"After one year at {acc.interest_rate:.0%}: {acc.balance_with_interest}")

    bonus_acc = BankAccount.open_with_bonus("New Customer")
    print(f"{bonus_acc.owner} starts with: {bonus_acc.balance}")

    print(BankAccount.is_valid_owner_name("Priya"))  # True
    print(BankAccount.is_valid_owner_name(""))        # False

    try:
        acc.balance = 1_000_000  # AttributeError: no setter defined
    except AttributeError as e:
        print(f"Blocked direct assignment: {e}")
