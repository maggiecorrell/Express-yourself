import re


def binary(x):
    return re.search(r'\A[0-1]+\Z', x)


def binary_even(x):
    return re.search(r'[0-1]*[0]\Z', x)


def hex(x):
    return re.search(r'\A[0-9A-F]+\Z', x)


def word(x):
    return re.search(r'^\w[A-Za-z\-0-9]+[A-Za-z]+$', x)


# def words(x, count=0):


def phone_number(x):
    return re.search(r'\(?(\d{3})\)?[-.]?\s*(\d{3})[-.]?(\d{4})', x)


def money(x):
    return re.search(r'^\$\d{1,}(,\d{3})*[.]?(\d{2})?$', x)


def zipcode(x):
    return re.search(r'^(\d{5})(-\d{4})?$', x)


def date(x):
    date_regex = [r'(\d{1,2})/(\d{1,2})/(\d{4}|\d{2})',
                  r'(\d{4})-?(\d{2})-?(\d{2})',
                  r'(\d{1,2})\s*([A-Za-z])\s*(\d{4})',
                  r'([A-Za-z]{3})\s*(\d{1,2})\s*,?\s*(\d{4})']
    for regex in date_regex:
        search = re.search(regex, x)
        if search:
            return search
