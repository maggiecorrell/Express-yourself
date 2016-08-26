import re


def phone_numbers(x):
    return re.findall(r'(\d{3})(\d{3})[-](\d{4})', x)
