def read_favorite_numbers(name):
    with open('favorite_numbers.json', 'r') as file:
        for i,line in enumerate(file):
            lines = len(file.readlines())
            if name in line:
                for num in line:
                    try:
                        num = int(num)
                    except ValueError:
                        pass
                    else:
                        print(f"I know your favorite number! It's {num}.")
            elif i == lines-1:
                print('No name was found.')


read_favorite_numbers(input('What is your name?  '))