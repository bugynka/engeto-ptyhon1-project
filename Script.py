"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Kateřinq Bálint
email: k.svobodova.8@seznam.cz
discord: katerinabalint_41161
"""

import task_template

names = ['bob', 'ann', 'mike', 'liz']
passwords = ['123', 'pass123', 'password123', 'pass123']
user = input('Username: ')
password = input('Password: ')
lenght = list()
occurence = dict()
index_user = names.index(user.lower()) if user.lower() in names else -1

if passwords[index_user] != password:
    exit("Unregistered user, terminating the program")

print('-' * 43, '\n' f'Welcome to the app, {user.capitalize()}!' '\n',
      'We have 3 texts to be analyzed' '\n',
      '-' * 43, sep="")

text_number = int(input('Enter a number between 1 and 3 to select: '))

if text_number not in range(1, len(task_template.TEXTS) + 1):
    exit('Incorrect input, terminating program')

selected_text = task_template.TEXTS[text_number - 1]
split_text = selected_text.split()

print('-' * 43)
print(f'There are {len(split_text)} words in the selected text.')

titlecase_words = 0
uppercase_words = 0
lowercase_words = 0
numeric_words = 0
sum_numbers = 0

for word in split_text:
    if word.istitle() and word.isalpha():
        titlecase_words += 1
    if word.isupper() and word.isalpha():
        uppercase_words += 1
    if word.islower() and word.isalpha():
        lowercase_words += 1
    if word.isnumeric():
        numeric_words += 1
    if word.isnumeric():
        sum_numbers += int(word)
    lenght.append(len(word))

print(f'There are {titlecase_words} titlecase words.')
print(f'There are {uppercase_words} uppercase words.')
print(f'There are {lowercase_words} lowercase words.')
print(f'There are {numeric_words} numeric strings.')
print(f'The sum of all the numbers is {sum_numbers}.')
print('-' * 43)

for element in lenght:
    occurence[element] = lenght.count(element)

sorted_occurence = dict(sorted(occurence.items()))
outcome = str()

for key in sorted_occurence:
    indent1 = (3 - len(str(key))) * ' '
    indent2 = ((max(sorted_occurence.keys()) + 5) - len('*' * sorted_occurence.get(key))) * ' '
    outcome += indent1 + str(key) + '|' + '*' * sorted_occurence.get(key) + indent2 + '|' + str(sorted_occurence.get(key)) + '\n'

indent3 = ((max(sorted_occurence.keys()) + 5 - len('OCCURENCES')) // 2)* ' '
print('LEN|' + indent3 + 'OCCURENCES' + indent3 + '|NR.')
print('-' * 43)
print(outcome)