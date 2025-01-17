from pathlib import Path

#file_reader.py
path = Path('pi_digits.txt')
contents = path.read_text()

for line in contents.splitlines():
 print(line)

#pi_string.py
contents = path.read_text()

pi_string = ''
for line in contents.splitlines():
    pi_string += line.lstrip()

print(pi_string)
print(len(pi_string))

#pi_birthday.py
contents = path.read_text()

pi_string = ''
for line in contents.splitlines():
    pi_string += line.lstrip()
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
 print("Your birthday appears in the first million digits of pi!")
else:
 print("Your birthday does not appear in the first million digits of pi.")
