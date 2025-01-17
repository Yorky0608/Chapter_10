num_one = input('Num one to be added.  ')
num_two = input('Num two to be added.  ')

try:
    num_one = int(num_one)
    num_two = int(num_two)
except ValueError:
    print("Please provide integers and not strings!")
else:
    print(num_one + num_two)