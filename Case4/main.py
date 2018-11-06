text = input()
counter = 0
word_counter = 1

# Я рассчитала количество предложений, количество слов. Операторы if для правильного вывода(в правильной форме).

for i in text:
    if i == '.' or i == '!' or i == '?' or i == '...':
        counter += 1
if 5 <= counter % 10 <= 20:
    print('В тексте {} предложений.'.format(counter))
elif counter % 10 == 1:
    print('В тексте {} предложение.'.format(counter))
elif counter % 10 == 2 or counter % 10 == 3 or counter % 10 == 4:
    print('В тексте {} предложения.'.format(counter))


for i in text:
    if i == ' ':
        word_counter += 1
if 5 <= word_counter % 10 <= 20:
    print('В тексте {} слов.'.format(word_counter))
elif word_counter % 10 == 1:
    print('В тексте {} слово.'.format(word_counter))
elif word_counter % 10 == 2 or word_counter % 10 == 3 or word_counter % 10 == 4:
    print('В тексте {} слова.'.format(word_counter))

text = text.lower()
vowers = list(text)
w1 = vowers.count('а')
w2 = vowers.count('о')
w3 = vowers.count('и')
w4 = vowers.count('е')
w5 = vowers.count('ё')
w6 = vowers.count('э')
w7 = vowers.count('ы')
w8 = vowers.count('у')
w9 = vowers.count('ю')
w10 = vowers.count('я')
syllables = w1 + w2 + w3 + w4 + w5 + w6 + w7 + w8 + w9 + w10
print('В тексте {} слогов.'.format(syllables))

ASL = word_counter / counter
print(ASL)

ASW = syllables / word_counter
print(ASW)
# Даша: рассчитать количество слогов, среднюю длину предложения в словах, среднюю длину слова в слогах.

# Арина: рассчить индекс удобочитаемости, вывести уровень сложности.

