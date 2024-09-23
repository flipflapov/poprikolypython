Комаров Андрей Николаевич

# 23.09.2024??
# Словарь Dict(dict): {"key1":"value1"...{keyN}:{valueN}}

import random

print('----------геншин----------')

name = input('Введите имя: ')
HERO = {
    "name": name
}

CHRS = {
    "Сила" : random.randint(15, 45),
    "Выносливость": random.randint(15, 45)
}

MODEL_HERO = '$'

HERO["Хар-ки"] = CHRS
HERO["МОДЕЛЬ"] = MODEL_HERO

MAP = ["0","0","0","0","0"] # [1 , "2" , True, [], ]

i = 0
MAP[i] = MODEL_HERO
#print(MAP)

#while MAP.index(MODEL_HERO) < len(MAP) > 0:
 #   tmp = i
 #   i = MAP.index(MODEL_HERO) + 1
 #   MAP[i] = MODEL_HERO
#    MAP[tmp] = '0'
#    print(MAP)
    
#while MAP.index(MODEL_HERO) == len(MAP) - 1:
#    tmp = i
#    i = MAP.index(MODEL_HERO) - 4
#    MAP[i] = MODEL_HERO
#    MAP[tmp] = '0'
#    print(MAP)

inventory = {
    "Броня": 15,
    "Зелье Здоровья": 1,
    "Лопата": 50
}

HERO["И"] = inventory
HERO["Базовый урон"] = 25

ENEMY = {
    "DMG": 50,
    "Картошка": 30
}

herohp = 150
enemyhp = 80

again=input(('Впереди враг! Напишите "y" если вы хотите напасть или "n" если хотите сбежать'))
while again == "y":
    if random.randint(1,6) in [1,2,3]:
        enemyhp = enemyhp - (HERO["Базовый урон"] + inventory["Лопата"])
        herohp = herohp - ((ENEMY["DMG"] + ENEMY["Картошка"])-inventory["Броня"])
        if herohp > 0:
            if enemyhp > 0:
                print('Ваша битва не окончена! У врага ', enemyhp, ' здоровья,  у вас ', herohp)
                again = input('Желаете продолжить? (y/n)')
            else:
                print('Вы победили врага!!! У вас осталось', herohp)
                break
        else:
            print('увы, вы погибли в жестокой схватке. Ваше имя записано в летописях, однако вряд-ли кто-то их увидит')
            break
    if random.randint(1,6) in [4,5]:
        print('Вы очень неуклюже попытались атаковать и выронили лопату. Вы нанесли удар без неё')
        enemyhp = enemyhp - HERO["Базовый урон"]
        herohp = herohp - ((ENEMY["DMG"] + ENEMY["Картошка"])-inventory["Броня"])
        if herohp > 0:
            if enemyhp > 0:
                print('Ваша битва не окончена! У врага ', enemyhp, ' здоровья,  у вас ', herohp)
                again = input('Желаете продолжить? (y/n)')
            else:
                print('Вы победили врага!!! У вас осталось', herohp)
        else:
            print('увы, вы погибли в жестокой схватке. Ваше имя записано в летописях, однако вряд-ли кто-то их увидит')
            break
    else:
        print('Вы промахнулись')
        herohp = herohp - ((ENEMY["DMG"] + ENEMY["Картошка"])-inventory["Броня"])
        if herohp > 0:
            if enemyhp > 0:
                print('Ваша битва не окончена! У врага ', enemyhp, ' здоровья,  у вас ', herohp)
                again = input('Желаете продолжить? (y/n)')
            else:
                print('Вы победили врага!!! У вас осталось', herohp)
        else:
            print('увы, вы погибли в жестокой схватке. Ваше имя записано в летописях, однако вряд-ли кто-то их увидит')
            break
while again == "n":
    again = input('Вы можете попробовать сбежать "r", вылечить себя "h" или вернуться в бой "y".')
    if again == "r":
        if random.randint(1,6) in [2,5]:
            print('С трудом, но вам удалось сбежать. Судьба этого мира больше неизвестна')
            break
        else:
            print('Побег неудался, вы вновь сражаетесь')
            again == "y"
    if again == "h":
        if HERO["И"]["Зелье Здоровья"] < 1:
            print('У вас нету зелья Здоровья')
            again == "n"
        else:
            herohp = herohp + 80
            print('Выпив зелье вам стало намного легче. У вас теперь ', herohp,' Здоровья' )
            again == "n"
