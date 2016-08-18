import re


def phone_numbers(x):
    numbers = []
    numbers = re.findall(r'\(?(\d{3})\)?[-.]?\s*(\d{3})[-.]?(\d{4})', x)
    return numbers
