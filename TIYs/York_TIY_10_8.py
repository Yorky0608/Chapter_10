from pathlib import Path

path_cats = Path('cats.txt')

try:
    contents_cats = path_cats.read_text()
except FileNotFoundError:
    print(f"The file {path_cats} is nowhere to be found.")
else:
    print(contents_cats)

path_dogs = Path('dogs.txt')

try:
    contents_dogs = path_dogs.read_text()
except FileNotFoundError:
    print(f"The file {path_dogs} is nowhere to be found.")
else:
    print(contents_dogs)