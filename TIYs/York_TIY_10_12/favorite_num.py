import json

def favorite_num(name):
    nums = {}
    num = int(input('What is your favorite number?  '))

    nums[name] = num
    nums = json.dumps(nums)

    make_file(nums)


def make_file(nums):
    with open('favorite_numbers.json', 'a') as file:
        file.write(f"\n{nums}")


def scan_file(name, run):
    with open('favorite_numbers.json', 'r') as file:
        for i, line in enumerate(file):
            if name in line:
                num_list = []
                number = ""
                for num in line:
                    try:
                        num = int(num)
                    except ValueError:
                        pass
                    else:
                        num_list.append(num)
                for num in num_list:
                    number += str(num)
                run = False
                print(f"\nI know your favorite number! It's {number}.")
            elif run == False:
                break
        if run == True:
            print(f'\nNo name was found. \nPlease add your favorite number.')
            favorite_num(name)


def read_favorite_numbers(name):
    run = True
    try:
        scan_file(name, run)
    except FileNotFoundError:
        print('\nNo one has added their favorite number yet. \nPlease add your favorite number.')
        favorite_num(name)

read_favorite_numbers(input('What is your name?  '))