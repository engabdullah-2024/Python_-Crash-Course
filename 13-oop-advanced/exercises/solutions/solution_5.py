# Solution to Exercise 5: Abstract Notifier interface + composition

from abc import ABC, abstractmethod


class Notifier(ABC):
    @abstractmethod
    def send(self, message):
        ...


class EmailNotifier(Notifier):
    def send(self, message):
        return f"Email sent: {message}"


class SMSNotifier(Notifier):
    def send(self, message):
        return f"SMS sent: {message}"


class NotificationCenter:
    def __init__(self):
        self.notifiers = []

    def register(self, notifier):
        self.notifiers.append(notifier)

    def broadcast(self, message):
        return [notifier.send(message) for notifier in self.notifiers]


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
