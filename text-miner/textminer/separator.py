import re


def words(x):
    words = re.findall(r'\b[A-Za-z\-0-9]*-?[A-Za-z]+\b', x)
    if words:
        return words
    else:
        None


def phone_number(x):
    match = re.search(r'\(*([\d]{3})\)*[-\s\.]*([\d]{3})[-\s\.]*([\d]{4})', x)
    if match:
        area_code, num1, num2 = match.groups()
        return {"area_code": area_code, "number": num1 + '-' + num2}


def money(x):
    match = re.search(r'^(\$)((\d{1,})+(,\d{3})*(\.\d{2})?)$', x)
    if match:
        groups = match.groups()
        currency = groups[0]
        amount = float(re.sub(r',', '', groups[1]))
        # groups = match.groups()
        # currency = groups[0]
        # amount = float(groups[1].replace(',', ''))
        return {"currency": currency, "amount": amount}
    else:
        return None


def zipcode(x):
    match = re.search(r'^(\d{5})\-?(\d{4})?$', x)
    if match:
        zip, plus4 = match.groups()
        return {"zip": zip, "plus4": plus4}


def date(x):
    match = re.search(r'(?P<year1>(\d{1,2})\/(\d{1,2})\/(\d{4}))|(?P<year2>(\d{4})\-(\d{2})\-(\d{2}))', x)
    if match:
        if match.group('year1'):
            month, day, year = match.group(2, 3, 4)
            return {"month": int(month), "day": int(day), "year": int(year)}
        elif match.group('year2'):
            year, month, day = match.group(6, 7, 8)
            return {"month": int(month), "day": int(day), "year": int(year)}
        else:
            return
    else:
        return None
