"""
Exercise 4: Profile Builder with **kwargs (Medium)

Write a function `build_profile(first, last, **extra_info)` that returns
a dictionary containing "first_name", "last_name", and any additional
keyword arguments merged in as-is.

Example:
    build_profile("Ada", "Lovelace", field="mathematics", country="UK")
    -> {
        "first_name": "Ada",
        "last_name": "Lovelace",
        "field": "mathematics",
        "country": "UK",
    }
"""


def build_profile(first, last, **extra_info):
    # TODO: build and return the profile dictionary
    pass


if __name__ == "__main__":
    profile = build_profile("Ada", "Lovelace", field="mathematics", country="UK")
    print(profile)
