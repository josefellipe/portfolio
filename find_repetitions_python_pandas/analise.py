import pandas as pd

database = pd.read_excel("Livro1.xlsx")
heading = list(database.columns)

def transform_DataFrame_into_array(data):
    data_array = []
    for i in range(len(data)):
        data_array.append(list(data.loc[i]))
    return data_array


def count_repetitions(data):
    for name1 in data:
        count = 0
        for name2 in data:
            if name1[1] == name2[1]:
                count += 1
        name1[5] = count
    return data


def remove_repetitions(data):
    aux = []
    aux.append(data[0])
    for name in data:
        count = 0
        for name_aux in aux:
            if name[1] == name_aux[1]:
                count += 1
        if count == 0:
            aux.append(name)
    return aux


def transform_data_into_DataFrame(data):
    table = pd.DataFrame(data, columns = heading)
    return table


def show_quantity_by_repetition(data):
    highest_repetition = 0
    for name in data:
        if name[5] > highest_repetition:
            highest_repetition = name[5]
    print(f'\nThe highest number of guns per person is: {highest_repetition}\n')
    i = 1
    while i <= highest_repetition:
        count = 0
        for name in data:
            if int(name[5]) == i:
                count += 1
        print(f'The quantity of people with {i} guns is: {count}')
        i += 1
    print("\n")


def show_people_per_quantity_of_guns(data,quantity):
    data_aux = []
    for name in data:
        if int(name[5]) == quantity:
            data_aux.append(name)
    data_aux = transform_data_into_DataFrame(data_aux)
    print(data_aux)


def filter_per_quantity_of_guns(data):
    new_search = "YES"
    while new_search == "YES":
        value = input("\n\n\nFor what quantity of guns do you want to visualize people's information?\n")
        if value.isnumeric():
            quantity_of_guns = int(value)
            if quantity_of_guns >= 0 and quantity_of_guns <= len(data):
                show_people_per_quantity_of_guns(data,quantity_of_guns)
                new_search = input("\n\nDo you want to do one more research?\n1 - Yes\n2 - No\n")
                if new_search == "1":
                    new_search = "YES"
                elif new_search == "2":
                    new_search = "NO"
            else:
                print("\nThis number is out of the range")
        else:
            print("\nInvalid Key\nTry again.\n")


def show_full_list(data):
    choice = "Invalid Key"
    while choice == "Invalid Key":
        choice = input("\n\nDo you want to see the full list?\n1 - Yes\n2 - No\n")
        if choice == "1":
            data_aux = transform_data_into_DataFrame(data)
        elif choice == "2":
            data_aux = "Thanks for researching with us!"
        else:
            choice = "Invalid Key"
            data_aux = "Invalid Key\nTry Again\n"
        print(f'\n\n'
        f'{data_aux}'
        f'\n\n')


data_in_matriz = transform_DataFrame_into_array(database)
data_in_matriz = count_repetitions(data_in_matriz)
data_formated = remove_repetitions(data_in_matriz)

show_quantity_by_repetition(data_formated)
filter_per_quantity_of_guns(data_formated)
show_full_list(data_formated)