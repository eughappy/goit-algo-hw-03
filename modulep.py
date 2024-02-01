import re
a = "+380 44 123 4567"
b = r"[\+\d+]"
print(''.join(re.findall(b,a)))