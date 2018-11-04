from random import sample
print('Загадано четырехбуквенное слово из букв "А", "Е", "Н", "О", "С", "Т"')
letters =['А', 'Е', 'Н', 'О', 'С', 'Т']
w = sample(letters, 4)
word = (''.join(w))

counter = 1
a_word = []
t = 0
r = 0
while word != a_word:
    a_word = input('{} {} '.format('Попытка №', counter))
    a_word = a_word.upper()
    y = 0
    counter += 1
    for w in a_word:
        if w == word[0] or w == word[1] or w == word[2] or w == word[3]:
            y += 1
        t = 0
        r = 0

        if counter > 10:
            print('Вы проиграли =(')
            print('Было загадано: ', word)
            break
        if word[0] == a_word[0]:
            t += 1
        else:
            r += 1
        if word[1] == a_word[1]:
            t += 1
        else:
            r += 1
        if word[2] == a_word[2]:
            t += 1
        else:
            r += 1
        if word[3] == a_word[3]:
            t += 1
        else:
            r += 1
    print('На "своем месте"', t)
    print('На "чужом месте"', r)

if word == a_word:
    print('Вы выиграли! =)')

