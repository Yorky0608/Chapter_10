import json

def favorite_num():
    print("Enter q to quit.")
    while True:
        nums = {}
        name = input("What is your name?  ")
        if name == 'q':
            break
        num = int(input('What is your favorite number?  '))
        if num == 'q':
            break
        nums[name] = num
        nums = json.dumps(nums)
        make_file(nums)


def make_file(nums):

    with open('favorite_numbers.json', 'a') as file:
        file.write(f"{nums}\n")


favorite_num()


def read_favorite_numbers(name):
    with open('favorite_numbers.json', 'r') as file:
        for line in file:
            if name in line:
                print(line)