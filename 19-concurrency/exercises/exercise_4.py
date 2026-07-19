"""
Exercise 4 (Hard): Fix the Race Condition

Multiple threads deposit and withdraw from a shared bank account
concurrently. As written, this program has a race condition: the final
balance is unpredictable and usually wrong.

TODO:
1. Add a threading.Lock to the Account class.
2. Use the lock (e.g. via `with self._lock:`) inside `deposit` and
   `withdraw` so each balance update is atomic.
3. Confirm that after your fix, running this file repeatedly always
   prints the same, mathematically-correct final balance.

Expected final balance: starting_balance + (num_threads * net_change_per_thread)
"""
import threading


class Account:
    def __init__(self, starting_balance: float) -> None:
        self.balance = starting_balance
        # TODO: create a threading.Lock() here and use it in deposit/withdraw

    def deposit(self, amount: float) -> None:
        current = self.balance
        current += amount
        self.balance = current

    def withdraw(self, amount: float) -> None:
        current = self.balance
        current -= amount
        self.balance = current


def worker(account: Account, iterations: int) -> None:
    for _ in range(iterations):
        account.deposit(10)
        account.withdraw(7)  # net +3 per iteration


def main() -> None:
    starting_balance = 1000
    num_threads = 8
    iterations = 5_000
    net_change_per_iteration = 3

    account = Account(starting_balance)
    threads = [
        threading.Thread(target=worker, args=(account, iterations))
        for _ in range(num_threads)
    ]

    for t in threads:
        t.start()
    for t in threads:
        t.join()

    expected = starting_balance + num_threads * iterations * net_change_per_iteration
    print(f"Expected balance: {expected}")
    print(f"Actual balance:   {account.balance}")
    print("Match!" if account.balance == expected else "MISMATCH -- race condition!")


if __name__ == "__main__":
    main()
