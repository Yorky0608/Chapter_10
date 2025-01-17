from pathlib import Path

path = Path('guest.txt')
name = input('What is your name?  ')

path.write_text(name)