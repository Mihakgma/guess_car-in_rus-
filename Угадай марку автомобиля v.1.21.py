#!/usr/bin/env python
# coding: utf-8

# In[4]:

import random

def guess_car():
    
    
    doc_str = """
    Данная программка загадывает случайным образом 3 
    из 69 марок машин международно известных брендов.
    
    Марки машин хранятся как значения в словаре.
    При этом ключами к ним являются названия
    стран-производителей.
    
    Важное замечание:
    МАРКИ АВТОМОБИЛЕЙ И СТРАНЫ-ПРОИЗВОДИТЕЛИ
    НАПИСАНЫ НА АНГЛИЙСКОМ ЯЗЫКЕ!!!
    НЕОБХОДИМО ВВОДИТЬ НАЗВАНИЕ МАРКИ АВТО
    НА АНГЛИЙСКОМ ЯЗЫКЕ!
    Регистр букв значения не имеет только в том случае, 
    если в загаданном списке отсутствуют составные названия, 
    состоящие из двух слов, разделенных пробелом или дефисом!
    Например, Ssang Young, Alfa Romeo etc
    
    Пользователь имеет 3 попытки угадать одну из загаданных 3-х марок автомобилей.
        
    Условная группировка стран-производителей следующая:
    
    Восток (East):
     - Япония (Japan)
     - Китай (China)
     - Южная Корея (Korea)
     - Россия (Russia)
     - Узбекистан (Uzbekistan)
     
    Запад (West):
     - США (USA)
     - Великобритания (GB)
     - Германия (Germany)
     - Италия (Italy)
     - Франция (France)
     - Швеция (Sweden)
     - Чехия (Czech)
     - Испания (Spain)
    
    """
    print(doc_str)
    def regul_register_of_letters(x: str, cars: list):
        if (('BYD' in cars) or
        ('FAW' in cars) or
        ('GM' in cars) or
        ('BMW' in cars) or
        ('GAZ' in cars) or
        ('UAZ' in cars) or
        ('VAZ' in cars) or
        ('MG' in cars)):
            x = x.upper()
        
        else:
            x = x.lower()
            x = x.capitalize()
        return(x)
    
    def podskazka_1(cars: list):
        first_car = cars[0]
        hint = first_car[0]
        for i in first_car[1:]:
            if (i == " ") or (i == "-"):
                hint += i
            else:
                hint += "*"
        return(hint)
    
    def podskazka_2(cars: list):
        first_car = cars[2]
        hint = first_car[0]
        for i in first_car[1:len(first_car)]:
            if (i == " ") or (i == "-"):
                hint += i
            else:
                hint += "*"
        hint = hint[:-1] + first_car[-1]
        return(hint)
    
    def get_key(d, value):
        for k, v in d.items():
            if value in v:
                return k
            
    def East_or_West(my_stroka: str):
        if ((my_stroka == "USA") or
        (my_stroka == "GB") or
        (my_stroka == "Germany") or
        (my_stroka == "Italy") or
        (my_stroka == "France") or
        (my_stroka == "Sweden") or
        (my_stroka == "Czech") or
        (my_stroka == "Spain")):
            return("Марка от Западного производителя")
        else:
            return("Марка от Восточного производителя")
       
    
    my_dict = {
        "Japan": ['Acura',
                  'Daihatsu',
                  'Datsun',
                  'Honda',
                  'Infiniti',
                  'Isuzu',
                  'Lexus',
                  'Mazda',
                  'Mitsubishi',
                  'Nissan',
                  'Scion',
                  'Subaru',
                  'Suzuki',
                  'Toyota'],

        "China": ['BYD',
                  'Brilliance',
                  'Changan',
                  'Chery',
                  'Dongfeng',
                  'FAW',
                  'Lifan'],

        "USA": ['Buick',
                'Cadillac',
                'Chevrolet',
                'Chrysler',
                'Dodge',
                'GM',
                'Jeep',
                'Lincoln',
                'Mercury',
                'Plymouth',
                'Pontiac',
                'Saturn',
                'Tesla'],

        "Germany": ['Audi',
                    'BMW',
                    'Maybach',
                    'Mercedes',
                    'Opel',
                    'Porsche',
                    'Smart',
                    'Volkswagen'],

        "Russia": ['GAZ',
                   'Marussia',
                   'UAZ',
                   'VAZ'],

        "Italy": ['Alfa Romeo',
                  'Ferrari',
                  'Fiat',
                  'Lamborghini',
                  'Lancia',
                  'Maserati'],

        "GB": ['Aston Martin',
               'Bentley',
               'Jaguar',
               'Land Rover',
               'Lotus',
               'MG',
               'McLaren',
               'Mini',
               'Rolls-Royce',
               'Rover'],

        "France": ['Citroen',
                   'Peugeot',
                   'Renault'],

        "Korea": ['Daewoo',
                  'Hyundai',
                  'Kia',
                  'Ssang Yong'],

        "Spain": ['Seat'],

        "Sweden": ['Saab',
                   'Volvo'],

        "Uzbekistan": ['Ravon'],

        "Czech": ['Skoda']

    }

    my_marki = []

    for i in my_dict.values():
        for j in i:
            my_marki.append(j)

    my_stop_index = len(my_marki)-1
    
    my_index_of_car_list_1 = random.randint(0,my_stop_index)
   
    cars = []
    cars.append(my_marki[my_index_of_car_list_1])
    
    while True:
        my_index_of_car_list_2 = random.randint(0,my_stop_index)
        if my_index_of_car_list_2 != my_index_of_car_list_1:
            break
      
    cars.append(my_marki[my_index_of_car_list_2])
    
    while True:
        my_index_of_car_list_3 = random.randint(0,my_stop_index)
        if ((my_index_of_car_list_3 != my_index_of_car_list_1) and 
        (my_index_of_car_list_3 != my_index_of_car_list_2)):
            break
      
    cars.append(my_marki[my_index_of_car_list_3])
    # УБРАТЬ!!!
    #print(cars)
    
    for i in cars:
        for j in i:
            if j == " " or j == "-":
                print("ВНИМАНИЕ! Как минимум одна из загаданных марок авто - составное (содержит 'пробел' или '-')")
                break
            
    podskazka = 0
    i = len(cars)
    print("Угадайте автомобиль из моего списка!")
    while i > 0:
        if i == 1:
            print("Последняя попытка!")
            try:
                podskazka = int(input("""
                ПОДСКАЗКА!
                Выберите тип подсказки (ВВЕДИТЕ ЦЕЛОЕ ЧИСЛО!):
                1 - Страна-изготовитель + первая буква названия марки первой в списке авто:
                2 - Восток/Запад + первая и последняя буквы названия марки последней в списке авто:
                
                """))
            except ValueError:
                print("Не было выбрано ни одной из предложенных подсказок...")
                pass
        i -= 1
        
        if podskazka == 1:
            print("Первый вариант подсказки :-)")
            print("Страна-производитель:",get_key(my_dict, cars[0]))
            print("Наименование марки:", podskazka_1(cars))
            
        if podskazka == 2:
            print("Второй вариант подсказки :-)")
            print(East_or_West(get_key(my_dict, cars[2])))
            print("Наименование марки:", podskazka_2(cars))
        
        my_guess = input("Напишите марку автомобиля: ")
        
        my_guess1 = regul_register_of_letters(my_guess, cars)
        
        my_guess2= my_guess.lower()
        my_guess2 = my_guess2.capitalize()
            
        if (my_guess in cars) or (my_guess1 in cars) or (my_guess2 in cars):
            
            if my_guess in cars:
                my_guess_final = my_guess
            
            elif my_guess1 in cars:
                my_guess_final = my_guess1
                
            elif my_guess2 in cars:
                my_guess_final = my_guess2
            
            print("""
            \m/
            """)
            print("Ура! Угадали! Действительно,", my_guess_final, "есть в моем списке автомобилей.")
            break
        elif i == 0:
            print("Неправильно!")
        else:
            print("Неправильно! Попробуйте еще раз!")
    else:
        
        print("""
           Все попытки кончились!     
        """)
        
        print("""
    ================== ================ 
    =================  ================  
    ===============   ==================   
    =============    ====================    
    ============     ====================     
    ===========     ======================     
    ==========      ======================      
    ==========       ==                ==       
    ==========
    ===========
    ============        ====      ====
    === ========       ======    ======
    === =======        === =     == ==
    ==   ======         ====      ====
    ==   =====
    =     ====                              ==
    =     ====   ==                        ==
    ===  =====   ==                       ==
    ===  ======   =====                =====
    ====  ======  ========          =======
    =====  ======   =======================
    =====  ========  ====           ======
    ======  ========   =====           ==
    =======  ==========   =====
    =========  ===========     ==
    =============================
    ==============================
    ===============================         """)
        
        print("К сожалению, Вам не удалось угадать ни одну из марок автомобилей. ^_^")
    print("Мой список марок автомобилей: ")
    print("")
    print(cars)
    input("Для завершения нажмите клавишу ENTER")

guess_car()


# In[ ]:




