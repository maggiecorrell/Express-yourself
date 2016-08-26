import re


# def words(input):


def phone_number(x):
    match = re.search(r'\(*([\d]{3})\)*[-\s\.]*([\d]{3})[-\s\.]*([\d]{4})', x)
    if match:
        area_code, num1, num2 = match.groups()
        return {"area_code": area_code, "number": num1 + '-' + num2}

#
# def money(x):
#     match = re.search(r'^\$\d{1,}(,\d{3})*[.]?(\d{2})?$', x)
#     if match:
#         currency, amount = match.groups()
#         return {"currency": currency, "number": amount}


def zipcode(x):
    match = re.search(r'^(\d{5})\-?(\d{4})?$', x)
    if match:
        zip, plus4 = match.groups()
        return {"zip": zip, "plus4": plus4}


# def date(x):
#     date_regex = [r'(\d{1,2})/(\d{1,2})/(\d{4}|\d{2})',
#                   r'(\d{4})-?(\d{2})-?(\d{2})',
#                   r'(\d{1,2})\s*([A-Za-z])\s*(\d{4})',
#                   r'([A-Za-z]{3})\s*(\d{1,2})\s*,?\s*(\d{4})']
#     for regex in date_regex:
#         match = re.search(regex, x)
#         if match:
#             month, day, year = match.groups()
#             return {"month": month, "day": day, "year": year}
