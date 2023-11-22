import random #Выполнет декоративную роль для генерации случайного номера заказа в итоговом чеке

valid_promo = "testing_promo" #Валидный промокод
basket = 0 #Корзина
order_num = random.randint(2500, 3750) #Номер заказа в чеке

print("Добро пожаловать на сайт ресторана быстрого питания!\nУ нас не предусмотрено оформление заказов для незарегистрированных пользователей, поэтому Вам необходимо пройти процедуру регистрации на нашем сайте.\n")

# РЕГИСТРАЦИЯ ПОЛЬЗОВАТЕЛЯ

#1)Ввод имени
user_name = input("Ваше имя: ")
while not user_name.isalpha():
    print("Ваше имя должно содержать только буквы")
    user_name = input("Ваше имя: ")
    if user_name.isalpha():
        break

#2)Ввод возраста

user_age = input("Ваш возраст: ")
while not user_age.isnumeric():
    print("Возраст должен содержать в себе только цифры.")
    user_age = input("Ваш возраст: ")
    if user_age.isnumeric():
        user_age = int(user_age)
        break

#3)Ввод логина/e-mail
print("Введите ваш адрес электронной почты.\n*E-mail адрес является Вашим логином на сайте. Наша система принимает только адреса yandex и gmail.")
while True:
    try:
        user_email = input("Введите адрес электронной почты: ")
        if "@" not in user_email:
            raise ValueError("Ошибка: отсутствует символ @ в адресе электронной почты")

        username, domain = user_email.split("@")
        if domain != "gmail.com" and domain != "yandex.ru":
            raise ValueError("Ошибка: неподдерживаемый домен электронной почты")
        break
    except ValueError as ve:
        print(ve)

#4)Ввод пароля
print("Придумайте пароль. *Пароль должен быть более 10 символов, содержать прописные и заглавные буквы, а также цифры или символы.")
user_password = input("Ваш пароль: ")
while len(user_password) <10:
    print("Слишком короткий пароль")
    user_password = input("Ваш пароль: ")

#5) Ввод номера телефона
print("Введите номер Вашего телефона")
user_phone = input("Номер телефона: ")
while not user_phone.isnumeric():
    print("Номер телефона может содержать только цифры.")
    user_phone = input("Номер телефона: ")
    if user_phone.isnumeric():
        break

#Выводим все введённые данные о клиенте:
print("\n\t- ДАННЫЕ О КЛИЕНТЕ: \n")
print(f"\t- Имя: {user_name}")
print(f"\t- Возраст: {user_age}")
print(f"\t- Адрес электронной почты: {user_email}")
print(f"\t- Пароль: {'*' * len(user_password)}")
print("\t- Показать пароль? 1 - да, показать пароль, 2 - нет, оставить скрытым: ", end="")
show_password = False
show_Password = int(input(""))
if show_Password == 1:
    print(f"\t- Пароль: {user_password}")
    show_password = True
elif show_password == 2:
    print(f"Пароль: {'*' * len(user_password)}")
print(f"\t- Телефон - {user_phone}")

#ВЫБОР ЛАПШИ

print("\nТеперь Вы можете оформить заказ.\nНа этой странице доступен выбор лапши.")

#Прайс на лапшу
noodles = 200
sauce = 50
vegetables = 40
meat = 100
mushrooms = 60
noodles_total_ingredients_price = []

print("""
Меню:
1) Лапша с соусом и мясом - 350 руб.
2) Лапша с мясом и грибами - 360 руб.
3) Лапша с соусом и грибами - 310 руб.
4) Лапша с соусом и овощами - 290 руб.
5) Лапша с овощами и грибами - 300 руб.
""")

user_action = input("Выберите лапшу в меню в соответствии с номером (ввод от 1 до 5)\nЧтобы пропустить выбор лапши, нажмите 0: ")
#Выбор лапши
while True:
    try:
        user_action = int(user_action)
        if user_action < 0 or user_action > 5:
            raise ValueError
        if user_action == 1:
            noodles_total_ingredients_price = [noodles, sauce, meat]
            print("Лапша с соусом и мясом.\nЦена -", (sum(noodles_total_ingredients_price)))
            #************************************* Выбор количества порций *************************************
            noodles_amount = input("\nВыберите количество единиц порций лапши, если оно равно нулю, то это значит, что Вы пропускаете заказ лапши: ")
            while True:
                try:
                    if not noodles_amount.isnumeric():
                        raise ValueError
                    noodles_amount = int(noodles_amount)
                    if noodles_amount == 0:
                        print("Вы ввели 0 и пропускаете этап заказа лапши.")
                        noodles_total_ingredients_price = 0
                        basket += 0
                        break
                    elif noodles_amount > 0:
                        print(f"Вы выбрали {noodles_amount} ед. порций лапши. Цена за {noodles_amount} ед. порций лапши - {sum(noodles_total_ingredients_price) * noodles_amount} руб.")
                        basket += (sum(noodles_total_ingredients_price) * noodles_amount)
                        break
                except ValueError:
                    print("Некорректный запрос")
                    noodles_amount = input("\nВыберите количество единиц порций лапши, если оно равно нулю, то это значит, что Вы пропускаете заказ лапши: ")
            break
        elif user_action == 2:
            noodles_total_ingredients_price = [noodles, meat, mushrooms]
            print("Лапша с мясом и грибами.\nЦена -", (sum(noodles_total_ingredients_price)))
            # ************************************* Выбор количества порций *************************************
            noodles_amount = input(
                "\nВыберите количество единиц порций лапши, если оно равно нулю, то это значит, что Вы пропускаете заказ лапши: ")
            while True:
                try:
                    if not noodles_amount.isnumeric():
                        raise ValueError
                    noodles_amount = int(noodles_amount)
                    if noodles_amount == 0:
                        print("Вы ввели 0 и пропускаете этап заказа лапши.")
                        noodles_total_ingredients_price = 0
                        break
                    elif noodles_amount > 0:
                        print(f"Вы выбрали {noodles_amount} ед. порций лапши. Цена за {noodles_amount} ед. порций лапши - {sum(noodles_total_ingredients_price) * noodles_amount} руб.")
                        basket += (sum(noodles_total_ingredients_price) * noodles_amount)
                        break
                except ValueError:
                    print("Некорректный запрос")
                    noodles_amount = input(
                        "\nВыберите количество единиц порций лапши, если оно равно нулю, то это значит, что Вы пропускаете заказ лапши: ")
            break
        elif user_action == 3:
            noodles_total_ingredients_price = [noodles, sauce, mushrooms]
            print("Лапша с соусом и грибами.\nЦена -", (sum(noodles_total_ingredients_price)))
            # ************************************* Выбор количества порций *************************************
            noodles_amount = input(
                "\nВыберите количество единиц порций лапши, если оно равно нулю, то это значит, что Вы пропускаете заказ лапши: ")
            while True:
                try:
                    if not noodles_amount.isnumeric():
                        raise ValueError
                    noodles_amount = int(noodles_amount)
                    if noodles_amount == 0:
                        print("Вы ввели 0 и пропускаете этап заказа лапши.")
                        noodles_total_ingredients_price = 0
                        break
                    elif noodles_amount > 0:
                        print(
                            f"Вы выбрали {noodles_amount} ед. порций лапши. Цена за {noodles_amount} ед. порций лапши - {sum(noodles_total_ingredients_price) * noodles_amount} руб.")
                        basket += (sum(noodles_total_ingredients_price) * noodles_amount)
                        break
                except ValueError:
                    print("Некорректный запрос")
                    noodles_amount = input(
                        "\nВыберите количество единиц порций лапши, если оно равно нулю, то это значит, что Вы пропускаете заказ лапши: ")
            break
        elif user_action == 4:
            noodles_total_ingredients_price = [noodles, sauce, vegetables]
            print("Лапша с соусом и овощами.\nЦена -", (sum(noodles_total_ingredients_price)))
            # ************************************* Выбор количества порций *************************************
            noodles_amount = input(
                "\nВыберите количество единиц порций лапши, если оно равно нулю, то это значит, что Вы пропускаете заказ лапши: ")
            while True:
                try:
                    if not noodles_amount.isnumeric():
                        raise ValueError
                    noodles_amount = int(noodles_amount)
                    if noodles_amount == 0:
                        print("Вы ввели 0 и пропускаете этап заказа лапши.")
                        noodles_total_ingredients_price = 0
                        break
                    elif noodles_amount > 0:
                        print(f"Вы выбрали {noodles_amount} ед. порций лапши. Цена за {noodles_amount} ед. порций лапши - {sum(noodles_total_ingredients_price) * noodles_amount} руб.")
                        basket += (sum(noodles_total_ingredients_price) * noodles_amount)
                        break
                except ValueError:
                    print("Некорректный запрос")
                    noodles_amount = input(
                        "\nВыберите количество единиц порций лапши, если оно равно нулю, то это значит, что Вы пропускаете заказ лапши: ")
            break
        elif user_action == 5:
            noodles_total_ingredients_price = [noodles, vegetables, mushrooms]
            print("Лапша с овощами и грибами.\nЦена -", (sum(noodles_total_ingredients_price)))
            # ************************************* Выбор количества порций *************************************
            noodles_amount = input(
                "\nВыберите количество единиц порций лапши, если оно равно нулю, то это значит, что Вы пропускаете заказ лапши: ")
            while True:
                try:
                    if not noodles_amount.isnumeric():
                        raise ValueError
                    noodles_amount = int(noodles_amount)
                    if noodles_amount == 0:
                        print("Вы ввели 0 и пропускаете этап заказа лапши.")
                        noodles_total_ingredients_price = 0
                        break
                    elif noodles_amount > 0:
                        print(f"Вы выбрали {noodles_amount} ед. порций лапши. Цена за {noodles_amount} ед. порций лапши - {sum(noodles_total_ingredients_price) * noodles_amount} руб.")
                        basket += (sum(noodles_total_ingredients_price) * noodles_amount)
                        break
                except ValueError:
                    print("Некорректный запрос")
                    noodles_amount = input(
                        "\nВыберите количество единиц порций лапши, если оно равно нулю, то это значит, что Вы пропускаете заказ лапши: ")
            break
        if user_action == 0:
            print("Вы отказались от покупки лапши и перешли к дальнейшему выбору блюд.")
            noodles_total_ingredients_price = 0
            break
    except ValueError:
        print("Некорректный ввод. Попробуйте снова.")
        user_action = input("Выберите лапшу в меню в соответствии с номером (ввод от 1 до 5)\nЧтобы пропустить выбор лапши, нажмите 0: ")


#ВЫБОР БУРГЕРОВ

print("\nНа этой странице доступен конструктор бургера.")

#Цены на ингредиенты
scone = 40  # булочка
cutlet_chicken = 50  # котлета куриная
cutlet_beef = 70  # котлета из говядины
salad = 10  # салат
cucumbers = 15  # огурчики
tomatoes = 20  # помидоры
sauce_1 = 5  # острый соус
sauce_2 = 7  # томатный соус
sauce_3 = 8  # чесночный соус

print("""
Меню:\n
Вы можете сами собрать свой бургер из следующих ингредиентов:
- булочка - цена 40 руб.(код 1)
- куриная - цена 50 руб. котлета (код 2)
- котлета из говядины - цена 70 руб. (код 3)
- салат - цена 10 руб. (код 4)
- маринованые огурчики - цена 15 руб. (код 5)
- помидоры - цена 20 руб. (код 6)
- острый соус - цена 5 руб. (код 7)
- томатный соус - цена 7 руб. (код 8)
- чесночный соус - цена 8 руб. (код 9)
\n""")

print("\nСистема принимает только значения от 1 до 9. Вы не сможете оформить заказ, если будете использовать числа меньше 1 и больше 9.\nВведённые Вами данные в диапазоне от 1 до 9 сохранятся и заказ сформируется, исходя из них.\n")
user_decision = input("Хотите приступить к заказу бургера и хотите пропустить этот этап?\nНажмите 1, если хотите приступить к заказу бургера и 0, если хотите пропустить этот этап: ")
while True:
    try:
        user_decision = int(user_decision)
        if user_decision < 0 or user_decision > 1:
            raise ValueError
        if user_decision == 1:
            # Конструктор бургера
            burger = []
            total_burger = sum(burger)
            total_burger = str(total_burger)
            n = int(input("Выберите из меню и введите в форму количество желаемых ингредиентов для Вашего бургера: "))
            if n == 0:
                print("Введённое Вами количество ингредиентов равно нулю, заказ бургера отменён")
                break
            for i in range(n):
                ingredient = int(input("Ингредиент: "))
                if ingredient == 1:
                    burger.append(scone)
                    print(" - булочка")
                elif ingredient == 2:
                    burger.append(cutlet_chicken)
                    print(" - куриная котлета")
                elif ingredient == 3:
                    burger.append(cutlet_beef)
                    print(" - котлета из говядины")
                elif ingredient == 4:
                    burger.append(salad)
                    print(" - салат")
                elif ingredient == 5:
                    burger.append(cucumbers)
                    print(" - огурцы")
                elif ingredient == 6:
                    burger.append(tomatoes)
                    print(" - помидоры")
                elif ingredient == 7:
                    burger.append(sauce_1)
                    print(" - соус острый")
                elif ingredient == 8:
                    burger.append(sauce_2)
                    print(" - соус томатный")
                elif ingredient == 9:
                    burger.append(sauce_3)
                    print(" - соус чесночный")
            print(f"Цена за бургер - {sum(burger)} руб.")
            #************************************* Выбор количества бургеров *************************************
            burger_amount = input("\nВыберите количество единиц бургеров, если оно равно нулю, то это значит, что Вы пропускаете заказ бургеров: ")
            while True:
                try:
                    if not burger_amount.isnumeric():
                        raise ValueError
                    burger_amount = int(burger_amount)
                    if burger_amount > 0:
                        burger_total_price = sum(burger) * burger_amount
                        print(f"Вы выбрали {burger_amount} ед. бургеров. Цена за {burger_amount} ед. бургеров - {burger_total_price} руб.")
                        basket += (sum(burger) * burger_amount)
                        break
                    elif burger_amount == 0:
                        print("Вы ввели 0 и пропускаете этап заказа бургеров.")
                        basket += 0
                        break
                except ValueError:
                    print("Некорректный запрос")
                    burger_amount = input("\nВыберите количество единиц бургеров, если оно равно нулю, то это значит, что Вы пропускаете заказ бургеров: ")
            break
        elif user_decision == 0:
            #Пропустить этап заказа бургера
            print("Вы пропустили этап заказа бургера.")
            break
    except ValueError:
        print("Некорректный запрос")
        user_decision = input("Нажмите 1, если хотите приступить к заказу бургера и 0, если хотите пропустить этот этап: ")


#ВЫБОР НАПИТКОВ
user_age = int(user_age)
#Цены на напитки
cola_033 = 45
cola_05 = 70
coffee = 40
beer = 80

print('\nНа этой странице вы можете заказать напиток - колу, кофе или пиво.\nПиво Вы сможете заказать, только если Вы старше 18 лет.\nЕсли вы хотите пропустить выбор напитка, введите 0')
print("""
 Напитки:
 - Кола объём 0,33 л.- цена 45 руб (код 1)
 - Кола объём 0,5 л. - цена 70 руб. (код 2)
 - Кофе - цена 40 руб. (код 3)
 - Пиво - 80 руб. (код 4)
""")

#Выбор напитка

user_decision_drink = input("Выберите напиток. Если Вы хотите пропустить выбор напитка, введите 0: ")
while True:
    try:
        user_decision_drink = int(user_decision_drink)
        if user_decision_drink <0 or user_decision_drink >4:
            raise ValueError
        user_decision_drink = int(user_decision_drink)
        if user_decision_drink == 0:
            print("Вы пропустили выбор напитка.")
            basket += 0
            break
        drinks = []
        if user_decision_drink == 1:
            print(f"Вы выбрали напиток Кола, цена - {cola_033} руб, объём 0,33 л.")
            drinks.append(cola_033)
            #************************************* Выбор количества порций *************************************
            drinks_amount = input("Выберите количество единиц напитка, если оно равно нулю, то это значит, что Вы пропускаете заказ напитка: ")
            while True:
                try:
                    if not drinks_amount.isnumeric():
                        raise ValueError
                    drinks_amount = int(drinks_amount)
                    if drinks_amount > 0:
                        drinks_total_price = sum(drinks) * drinks_amount
                        print(f"Вы выбрали {drinks_amount} ед. напитка. Цена за {drinks_amount} ед. напитка - {drinks_total_price} руб.")
                        drinks_total_price = []
                        drinks_total_price.append(sum(drinks) * drinks_amount)
                        basket += sum(drinks_total_price)
                        break
                    elif drinks_amount == 0:
                        print("Вы ввели 0 и пропускаете этап заказа напитка.")
                        drinks_total_price = 0
                        basket += 0
                        break
                except ValueError:
                    print("Некорректный запрос")
                    drinks_amount = input("Выберите количество единиц напитка, если оно равно нулю, то это значит, что Вы пропускаете заказ напитка: ")
            break
        elif user_decision_drink == 2:
            print(f"Вы выбрали напиток Кола, цена - {cola_05} руб, объём 0,5 л.")
            drinks.append(cola_05)
            #************************************* Выбор количества порций *************************************
            drinks_amount = input("Выберите количество единиц напитка, если оно равно нулю, то это значит, что Вы пропускаете заказ напитка: ")
            while True:
                try:
                    if not drinks_amount.isnumeric():
                        raise ValueError
                    drinks_amount = int(drinks_amount)
                    if drinks_amount > 0:
                        drinks_total_price = sum(drinks) * drinks_amount
                        print(f"Вы выбрали {drinks_amount} ед. напитка. Цена за {drinks_amount} ед. напитка - {drinks_total_price} руб.")
                        drinks_total_price = []
                        drinks_total_price.append(sum(drinks) * drinks_amount)
                        basket += sum(drinks_total_price)
                        break
                    elif drinks_amount == 0:
                        print("Вы ввели 0 и пропускаете этап заказа напитка.")
                        drinks_total_price = 0
                        basket += 0
                        break
                except ValueError:
                    print("Некорректный запрос")
                    drinks_amount = input("Выберите количество единиц напитка, если оно равно нулю, то это значит, что Вы пропускаете заказ напитка: ")
            break
        elif user_decision_drink == 3:
            print(f"Вы выбрали Кофе, цена - {coffee} руб.")
            drinks.append(coffee)
            # ************************************* Выбор количества порций *************************************
            drinks_amount = input(
                "Выберите количество единиц напитка, если оно равно нулю, то это значит, что Вы пропускаете заказ напитка: ")
            while True:
                try:
                    if not drinks_amount.isnumeric():
                        raise ValueError
                    drinks_amount = int(drinks_amount)
                    if drinks_amount > 0:
                        drinks_total_price = sum(drinks) * drinks_amount
                        print(
                            f"Вы выбрали {drinks_amount} ед. напитка. Цена за {drinks_amount} ед. напитка - {drinks_total_price} руб.")
                        drinks_total_price = []
                        drinks_total_price.append(sum(drinks) * drinks_amount)
                        basket += sum(drinks_total_price)
                        break
                    elif drinks_amount == 0:
                        print("Вы ввели 0 и пропускаете этап заказа напитка.")
                        drinks_total_price = 0
                        basket += 0
                        break
                except ValueError:
                    print("Некорректный запрос")
                    drinks_amount = input(
                        "Выберите количество единиц напитка, если оно равно нулю, то это значит, что Вы пропускаете заказ напитка: ")
            break
        elif user_decision_drink == 4 and user_age >= 18:
            print(f"Вы выбрали пиво, цена - {beer} руб.")
            drinks.append(beer)
            # ************************************* Выбор количества порций *************************************
            drinks_amount = input(
                "Выберите количество единиц напитка, если оно равно нулю, то это значит, что Вы пропускаете заказ напитка: ")
            while True:
                try:
                    if not drinks_amount.isnumeric():
                        raise ValueError
                    drinks_amount = int(drinks_amount)
                    if drinks_amount > 0:
                        drinks_total_price = sum(drinks) * drinks_amount
                        print(
                            f"Вы выбрали {drinks_amount} ед. напитка. Цена за {drinks_amount} ед. напитка - {drinks_total_price} руб.")
                        drinks_total_price = []
                        drinks_total_price.append(sum(drinks) * drinks_amount)
                        basket += sum(drinks_total_price)
                        break
                    elif drinks_amount == 0:
                        print("Вы ввели 0 и пропускаете этап заказа напитка.")
                        drinks_total_price = 0
                        basket += 0
                        break
                except ValueError:
                    print("Некорректный запрос")
                    drinks_amount = input("Выберите количество единиц напитка, если оно равно нулю, то это значит, что Вы пропускаете заказ напитка: ")
            break
        elif user_decision_drink == 4 and user_age < 18:
            drinks = []
            print("Ваш возраст менее 18 лет, поэтому Вы не можете заказать пиво.")
            user_decision_drink = input("Выберите напиток. Если Вы хотите пропустить выбор напитка, введите 0: ")
            if user_decision_drink == 0:
                print("Вы пропустили выбор напитка.")
                break
    except ValueError:
        print("Некорректный запрос.")
        user_decision_drink = input("Выберите напиток. Если Вы хотите пропустить выбор напитка, введите 0: ")


#КОРЗИНА

print("""
ИТОГО:
""")
print(f"Заказ №{order_num}: \n*******************")
if user_action > 0 and noodles_amount > 0:
    print(f"Лапша {noodles_amount} ед. порций - {(sum(noodles_total_ingredients_price) * noodles_amount)}  руб.")
if user_decision > 0 and burger_amount > 0:
    print(f"Бургер {burger_amount} шт. - {burger_total_price} руб.")
if user_decision_drink > 0 and drinks_amount > 0:
    print(f"Напитки {drinks_amount} шт. - {sum(drinks_total_price)} руб.")
print(f"Общая сумма заказа - {basket} руб.")
if basket > 0:
    #Промокод
    print("Промокод дарит скиду 7% на весь заказ. Если у Вас есть валидный промокод, введите его в форме ниже.\nЕсли у Вас нет промокода, введите - (минус) и заказ оформится по цене без учёта скидки.")
    while True:
        try:
            #Промокод применён
            user_promo = input("Введите промокод: ")
            promo_action = basket - basket / 100 * 7
            if user_promo != valid_promo and user_promo != "-":
                raise ValueError
            if user_promo == valid_promo:
                print("""
            Сумма заказа с учётом скидки 7% по промокоду:
                """)
                print(f"Заказ №{order_num}: \n*******************")
                print(f"Общая сумма заказа - {promo_action} руб.")
                print(f"Спасибо за заказ! :)\nВ течении нескольких минут по номеру {user_phone} с Вами свяжется наш менеджер для уточнения деталей заказа.")
                break
            #Промокод не применён
            elif user_promo == "-":
                print("""
            Промокод не применён, сумма заказа:
                """)
                print(f"Заказ №{order_num}: \n*******************")
                print(f"Общая сумма заказа - {basket} руб.")
                print(f"Спасибо за заказ! :)\nВ течении нескольких минут по номеру {user_phone} с Вами свяжется наш менеджер для уточнения деталей заказа.")
                break
        except ValueError:
            print("Некорректный промокод.\nЕсли у Вас есть валидный промокод, введите его в форме ниже.\nЕсли у Вас нет промокода, введите - (минус) и заказ оформится по цене без учёта скидки.")
            continue

elif basket == 0:
    print("Вы попытались оформить пустой заказ.")


