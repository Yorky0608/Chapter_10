from pathlib import Path

path = Path('guest_book.txt')

names = ''

while True:
    name = input('What is your name? If all guests have entered their name, enter x.  ')
    if name.lower() == 'x':
        break
    else:
        names += name + '\n'

path.write_text(names)
