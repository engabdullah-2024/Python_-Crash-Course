"""Solution 4: Profile Builder with **kwargs"""


def build_profile(first, last, **extra_info):
    profile = {"first_name": first, "last_name": last}
    profile.update(extra_info)
    return profile


if __name__ == "__main__":
    profile = build_profile("Ada", "Lovelace", field="mathematics", country="UK")
    print(profile)
