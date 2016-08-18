import re


# def words(input):


def phone_number(x):
    match = re.search(r'\(*([\d]{3})\)*[-\s\.]*([\d]{3})[-\s\.]*([\d]{4})', x)
    if match:
        area_code, num1, num2 = match.groups()
        return {"area_code": area_code, "number": num1 + '-' + num2}


def money(x):
    match = re.search(r'^\$\d{1,}(,\d{3})*[.]?(\d{2})?$', x)
    if match:
        currency, amount = match.groups()
        return {"currency": currency, "number": amount}
