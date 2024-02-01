import re

def normalize_phone(phone_number):
    pattern = r"[\+\d+]"
    num = ''.join(re.findall(pattern, phone_number))
    if len(num) == 12:
        return "+" + num
    elif len(num) == 10:
        return "+38" + num
    else:
        return num

raw_numbers = [ "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   "]

sanitized_numbers = [normalize_phone(number) for number in raw_numbers]
print(sanitized_numbers)
