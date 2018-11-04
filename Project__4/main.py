from random import *
question = input('Хотите сыграть в игру? ')
while question == 'Да':
    print('Загадано четырехбуквенное слово из букв "А", "Е", "Н", "О", "С", "Т"')
    print('Отгадайте')
    L =[1040, 1045, 1053, 1054, 1057,1058]
    w1 = choice(L)
    w2 = choice(L)
    w3 = choice(L)
    w4 = choice(L)
    word = chr(w1) + chr(w2) + chr(w3) + chr(w4)

    counter = 1
    while counter < 11:
        a_word = input('{} {} '.format('Попытка №', counter))
        counter += 1
    if word == a_word:
        print('Вы выиграли! =)')
    else:
        print('Вы проиграли =(')
    print('Было загадано', word)
else:
    break