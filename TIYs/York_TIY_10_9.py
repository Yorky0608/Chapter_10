from pathlib import Path

path_cats = Path('cats.txt')

try:
    contents_cats = path_cats.read_text()
except FileNotFoundError:
   pass
else:
    print(contents_cats)

path_dogs = Path('dogs.txt')

try:
    contents_dogs = path_dogs.read_text()
except FileNotFoundError:
    pass
else:
    print(contents_dogs)