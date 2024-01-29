import random
def get_numbers_ticket(min, max, quantity):
    lottery_list = []
    while len(lottery_list) != quantity:
        randnum = random.randint(min,max)
        if randnum not in lottery_list:
            lottery_list.append(randnum)
    return sorted(lottery_list)

try:
    min_num = int(input("Введіть значення, від якого будуть формуватися числа: "))
except:
    print("Ви неправильно ввели значення від якого будуть формуватися числа, введіть ціле число!")
    min_num = int(input())

try:
    max_num = int(input("Введіть значення, до якого будуть формуватися числа: "))
except:
    print("Ви неправильно ввели значення до якого будуть формуватися числа, введіть ціле число!")
    max_num = int(input("Введіть значення, до якого будуть формуватися числа: "))

try:
    quant = int(input("Введіть кількість значень, які хочете сформувати: "))
except:
    print("Ви неправильно ввели кількість значень, які хочете сформувати, введіть ціле число!")
    quant = int(input("Введіть кількість значень, які хочете сформувати: "))

lottery_numbers = get_numbers_ticket(min_num, max_num, quant)
print(f"Ваші лотерейні числа: {lottery_numbers}")