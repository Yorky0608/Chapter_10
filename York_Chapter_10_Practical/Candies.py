import openpyxl as op

path = "Candy_Request_Responses_1.xlsx"

wb = op.load_workbook(path)

sheet = wb.active
max_col = sheet.max_column
max_row = sheet.max_row

'''The way to write is by take the cell used below and setting cell.value = name/ candy.
Need a way to keep track where last current cell is and add new cells each new person is added.
Need to also keep track of adding new candies to the same row/column and a way to separate them to create lists.
Then wb.save(path) to keep the changes that were made.'''

fav_candies = {}

for a in range(2, max_row + 1):
    cell1 = sheet.cell(row=a, column=2)
    cell2 = sheet.cell(row=a, column=3)

    cell1 = cell1.value.title().strip()
    cell2 = cell2.value.lower().strip()

    fav_candies[cell1] = [cell2]


def arrange_by_candies(fav_candies):
    candy_list={}
    candy_dict={}
    for name, candy in fav_candies.items():
        for candie in candy:
            can = candie.replace(' ', '')
            if can not in candy_list:
                candy_list[can] = candie
                candy_dict[candie] = [name]
            else:
                candy_dict[candy_list[can]].append(name)
    return candy_dict


def add_candies(candy, name):
    fav_candies[name].append(candy)


def ask_for_candy():
    candy = input('What candy would you like to add? ')
    return candy.lower()


def add_new_person(name):
    fav_candies[name] = [ask_for_candy()]


def ask_add_candies(fav_candies):
    run = True
    while run:
        name = input('What is your name? ')
        try:
            int(name)
        except ValueError:
            run = False
        else:
            print('Please provide your name.')
        if name in fav_candies:
            while True:
                try:
                    y_n = input('Would you like to add a candy to your list? y/n ')
                    if y_n == 'y':
                        add_candies(ask_for_candy(), name)
                    else:
                        break
                except KeyError:
                    print('Please provide y for yes and n for no.')
        else:
            print('Your name is not in our database.')
            print('Adding you to our database.')
            add_new_person(name)


ask_add_candies(fav_candies)

print(fav_candies)

print(arrange_by_candies(fav_candies))