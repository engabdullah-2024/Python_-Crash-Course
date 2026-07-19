# Inheritance, method overriding, and super() in action.


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def describe(self):
        return f"{self.name} earns ${self.salary:,.2f}"

    def annual_bonus(self):
        return self.salary * 0.05


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)  # reuse the parent's setup
        self.team_size = team_size

    def describe(self):
        base = super().describe()       # extend, don't replace
        return f"{base} and manages {self.team_size} people"

    def annual_bonus(self):
        # managers get the standard bonus plus a per-report bonus
        return super().annual_bonus() + self.team_size * 200


if __name__ == "__main__":
    staff = [
        Employee("Ada", 90_000),
        Manager("Grace", 120_000, team_size=6),
    ]

    for person in staff:
        print(person.describe())
        print(f"  bonus: ${person.annual_bonus():,.2f}")
