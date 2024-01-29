import random
def get_numbers_ticket(min, max, quantity):
    lottery_list = []
    while len(lottery_list) != quantity:
        randnum = random.randint(min,max)
        if randnum not in lottery_list:
            lottery_list.append(randnum)
    return sorted(lottery_list)


while True:
    try:
        min_num = int(input("Введіть значення, від якого будуть формуватися числа: "))
        break
    except:
        print("Ви неправильно ввели значення від якого будуть формуватися числа, введіть ціле число!")

while True:
    try:
        max_num = int(input("Введіть значення, до якого будуть формуватися числа: "))
        break
    except:
        print("Ви неправильно ввели значення до якого будуть формуватися числа, введіть ціле число!")

while True:
    try:
        quant = int(input("Введіть кількість значень, які хочете сформувати: "))
        break
    except:
        print("Ви неправильно ввели кількість значень, які хочете сформувати, введіть ціле число!")

lottery_numbers = get_numbers_ticket(min_num, max_num, quant)
print(f"Ваші лотерейні числа: {lottery_numbers}")