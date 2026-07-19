"""
Exercise 5 (Hard): Abstract Notifier interface + composition

Build a small notification system:

  - An abstract base class `Notifier(ABC)` with an abstract method
    `send(self, message)`.
  - Two concrete subclasses:
      - `EmailNotifier` whose send() returns f"Email sent: {message}"
      - `SMSNotifier` whose send() returns f"SMS sent: {message}"
  - A `NotificationCenter` class that:
      - is initialized with an empty list of notifiers (composition, NOT
        inheritance -- NotificationCenter does not inherit from Notifier)
      - has a method `register(self, notifier)` to add a Notifier to the list
      - has a method `broadcast(self, message)` that calls send(message) on
        every registered notifier and returns a list of the results

Try instantiating `Notifier()` directly at the bottom -- it should raise
a TypeError because it's abstract.
"""

from abc import ABC, abstractmethod


class Notifier(ABC):
    @abstractmethod
    def send(self, message):
        ...


class EmailNotifier(Notifier):
    def send(self, message):
        # TODO
        pass


class SMSNotifier(Notifier):
    def send(self, message):
        # TODO
        pass


class NotificationCenter:
    def __init__(self):
        # TODO: store an empty list of notifiers
        pass

    def register(self, notifier):
        # TODO
        pass

    def broadcast(self, message):
        # TODO: return a list of results from calling send() on each notifier
        pass


if __name__ == "__main__":
    center = NotificationCenter()
    center.register(EmailNotifier())
    center.register(SMSNotifier())

    results = center.broadcast("Server is down!")
    for r in results:
        print(r)

    try:
        Notifier()
    except TypeError as e:
        print(f"Correctly blocked: {e}")
