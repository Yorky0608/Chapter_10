from pathlib import Path

files = ['file_1.txt', 'file_23.txt', 'file_3.txt']

def count_the(file):
    path = Path(file)
    try:
        content = path.read_text(encoding='utf-8').count('the ')
    except FileNotFoundError:
        print('File not found.')
    else:
        return content

for file in files:
    if count_the(file) is not None:
        print(count_the(file))