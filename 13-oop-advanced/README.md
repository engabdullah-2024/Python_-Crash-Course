# Lesson 13: OOP Advanced

You already know how to define a class, give it an `__init__`, and attach instance and class attributes. This lesson takes that foundation and builds the rest of Python's object model on top of it: inheritance and `super()`, polymorphism, composition, the dunder methods that make your objects behave like built-in types, `@property` for controlled attribute access, `@classmethod`/`@staticmethod`, and abstract base classes. These are the tools that let you design object models instead of just writing classes — the difference matters once a codebase grows past a few hundred lines.

## Key Concepts

- Inheritance (`class Child(Parent)`) and method overriding
- `super()` — calling the parent implementation
- Polymorphism — same interface, different behavior
- Multiple inheritance and the Method Resolution Order (MRO)
- Composition vs inheritance ("has-a" vs "is-a")
- Dunder methods: `__repr__`, `__str__`, `__eq__`, `__len__`, `__iter__`
- `@property` — computed attributes that look like plain attributes
- `@classmethod` and `@staticmethod`
- Abstract base classes with the `abc` module

## Explanation

### Inheritance and `super()`

A child class inherits every attribute and method from its parent. It can override any of them, and it can call the parent's original version with `super()`.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # let Animal set self.name
        self.breed = breed

    def speak(self):             # override
        return f"{self.name} barks."


generic = Animal("Creature")
rex = Dog("Rex", "Labrador")
print(generic.speak())  # Creature makes a sound.
print(rex.speak())      # Rex barks.
```

`super().__init__(name)` avoids repeating the parent's setup logic. If `Animal.__init__` later grows a validation step, `Dog` gets it for free.

### Polymorphism

Polymorphism means code written against a common interface works with any object that honors it, regardless of concrete type.

```python
class Cat(Animal):
    def speak(self):
        return f"{self.name} meows."


for pet in (rex, Cat("Whiskers")):
    print(pet.speak())   # each object supplies its own behavior
```

The calling code (`pet.speak()`) never checks `isinstance`. It trusts that any `Animal` has a `speak` method — that trust is the whole point.

### Multiple inheritance and MRO

Python allows a class to inherit from more than one parent. When two parents define the same method, Python resolves the call order using the **Method Resolution Order** (MRO), computed with the C3 linearization algorithm. You rarely need to compute it by hand — `ClassName.__mro__` or `ClassName.mro()` shows it.

```python
class Flyer:
    def move(self):
        return "flies"


class Swimmer:
    def move(self):
        return "swims"


class Duck(Flyer, Swimmer):
    pass


print(Duck().move())        # "flies" — Flyer comes first in the MRO
print(Duck.__mro__)
# (<class 'Duck'>, <class 'Flyer'>, <class 'Swimmer'>, <class 'object'>)
```

Multiple inheritance is powerful but easy to misuse. Reach for it sparingly — mixins (small classes that add one capability) are the most common legitimate use case.

### Composition vs inheritance

Inheritance models "is-a" relationships. Composition models "has-a" relationships — an object holds another object and delegates to it. Composition is usually more flexible: it avoids deep, fragile hierarchies and lets you swap parts independently.

```python
class Engine:
    def start(self):
        return "Engine started"


class Car:
    def __init__(self):
        self.engine = Engine()   # Car HAS an engine, it isn't one

    def start(self):
        return self.engine.start()


print(Car().start())  # Engine started
```

Rule of thumb: prefer composition unless you genuinely need the child to be substitutable everywhere the parent is used (the Liskov substitution idea).

### Dunder methods

"Dunder" (double underscore) methods let your objects plug into Python's built-in syntax — `print()`, `==`, `len()`, `for` loops, and more.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        # unambiguous, for developers — ideally eval()-able
        return f"Point({self.x!r}, {self.y!r})"

    def __str__(self):
        # readable, for end users
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return (self.x, self.y) == (other.x, other.y)

    def __len__(self):
        # distance from the origin, rounded — a contrived but valid example
        return round((self.x ** 2 + self.y ** 2) ** 0.5)

    def __iter__(self):
        yield self.x
        yield self.y


p = Point(3, 4)
print(p)            # (3, 4)               -> uses __str__
print(repr(p))       # Point(3, 4)          -> uses __repr__
print(p == Point(3, 4))  # True             -> uses __eq__
print(len(p))        # 5                    -> uses __len__
x, y = p             # unpacking works because __iter__ exists
```

If you define `__eq__`, Python disables the default `__hash__` (object identity), so instances become unhashable unless you also define `__hash__`. Only add `__hash__` if the object is meant to be immutable and used in sets/dict keys.

### `@property`

`@property` lets a method be accessed like a plain attribute, which is useful for validation or computed values without breaking the `object.attribute` interface.

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Below absolute zero.")
        self._celsius = value

    @property
    def fahrenheit(self):          # read-only computed property
        return self._celsius * 9 / 5 + 32


t = Temperature(25)
print(t.fahrenheit)   # 77.0
t.celsius = 30        # goes through the setter's validation
print(t.celsius)      # 30
```

### `@classmethod` and `@staticmethod`

- `@classmethod` receives the class (`cls`) instead of the instance. Common use: alternative constructors.
- `@staticmethod` receives neither `self` nor `cls`. Use it for a function that logically belongs in the class's namespace but doesn't touch instance or class state.

```python
class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @classmethod
    def margherita(cls):
        return cls(["mozzarella", "basil"])   # alternative constructor

    @staticmethod
    def is_valid_topping(name):
        return isinstance(name, str) and len(name) > 0


p = Pizza.margherita()
print(p.toppings)                    # ['mozzarella', 'basil']
print(Pizza.is_valid_topping("ham"))  # True
```

### Abstract base classes

The `abc` module lets you define a class that cannot be instantiated directly and forces subclasses to implement certain methods.

```python
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        ...


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2


# Shape()          # TypeError: Can't instantiate abstract class
c = Circle(2)
print(c.area())     # 12.56636
```

This is how you communicate "every subclass must provide this" and have Python enforce it, instead of relying on a comment or a `NotImplementedError` that only fires at call time.

## Common Pitfalls

- **Forgetting `super().__init__()`** in a subclass `__init__`, silently leaving parent attributes unset.
- **Mutable default arguments in `__init__`** (e.g. `def __init__(self, items=[])`) — the list is shared across all instances. Use `None` and create the list inside the body instead.
- **Overusing multiple inheritance** to combine unrelated behaviors, producing MRO conflicts and code that's hard to trace. Prefer composition or small, single-purpose mixins.
- **Defining `__eq__` without `__hash__`** when the object needs to go in a set or be a dict key — it becomes unhashable and raises `TypeError`.
- **Confusing `@staticmethod` and `@classmethod`** — if the method needs to know which class it was called on (e.g., to construct an instance), it needs `cls`, not a plain staticmethod.

## Summary

- `super()` calls the parent's implementation; always use it in a subclass `__init__` unless you deliberately want to skip parent setup.
- Polymorphism lets calling code treat different types uniformly as long as they share an interface.
- Prefer composition over inheritance unless a true "is-a" relationship and substitutability are required.
- Dunder methods (`__repr__`, `__eq__`, `__len__`, `__iter__`, …) are how custom objects integrate with Python's built-in syntax.
- `@property` and `@classmethod`/`@staticmethod` give you fine control over how attributes and constructors work; `abc.ABC` lets you enforce a subclass contract.

## Next

[Next: 14 - Decorators & Closures →](../14-decorators-and-closures/)
[← Back to course overview](../README.md)
