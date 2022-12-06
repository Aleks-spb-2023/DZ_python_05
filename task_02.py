
from random import randint

candies = 2021
take_candies = 0
player_1_sweet = 0
player_2_sweet = 0

def random_cast():
    random_number = randint(1, 2)
    if random_number == 1:
        player_1_F()
    else:
        player_2_F()

def player_1_F():
    global candies
    global take_candies
    global player_1_sweet
    print(f"Ваш ход , берите конфеты ! на столе их {candies} штук ")
    take_candies = int(input("Сколько конфет вы хотите взять?"))
    while take_candies > 28 or take_candies < 0 or take_candies > candies:
        take_candies = int(input("Вы берете слишком много конфет попробуйте снова"))
    candies -= take_candies
    player_1_sweet += take_candies
    if candies > 0:
        player_2_F()
    else:
        print("Вы победили")


def player_2_F():
    global candies
    global take_candies
    global player_2_sweet
    take_candies = candies % 29 if candies % 29 != 0 else randint(1, 28)
    candies -= take_candies
    player_2_sweet += take_candies
    print(f"Бот взял {take_candies} конфет . Осталось {candies} конфет")
    if candies > 0:
        player_1_F()
    else:
        print("Бот победил")






print(random_cast())
