from os import path

zero = 0
file_base = "base.txt"
last_id = int(zero)
all_data = []

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass

def read_records():
    global last_id, all_data

    if last_id:
        with open(file_base, encoding="utf-8") as f:
            all_data = [i.strip() for i in f]
            last_id = all_data[-1][0]
        return all_data
    return []

def show_all():
    global all_data
    if all_data:
        print(*all_data, sep="\n")
    else:
        print("Empty data!")

def delete():
    global last_id, all_data
    question = input("Do you know contact ID? Y/N - ")
    if question == 'Y':
        show_all
    else:
        con_id = int(input("Enter id: "))
        for i in range(len(all_data)):
            if con_id == all_data[i][0]:
                del_id = True
        if del_id:
            all_data.pop(i)


def exist_contact(rec_id, data):

    if rec_id:
        candidates = [i for i in all_data if rec_id in i.split()[0]]
    else:
        candidates = [i for i in all_data if data in i]
    return candidates

    
# def add_new_contact():
#     global last_id, all_data

#     array = ["surname", "name", "patronymic", "phone_number", "description"]
#     string = ""
#     for i in array:
#         string += input(f"Enter {i} ") + "   "
#     all_data.append(string)
#     last_id += 1

#     with open(file_base, "a", encoding="utf-8") as f:
#         f.write(f"{last_id} {string}\n")

def add_new_contact():

    global last_id

    array = ['surname', 'name', 'patronymic', 'phone number']
    answers = []
    for i in array:
        answers.append(data_collection(i))

    if not exist_contact(0, " ".join(answers)):
        last_id += 1
        answers.insert(0, str(last_id))

        with open(file_base, "a", encoding="utf-8") as f:
            f.write(f'{" ".join(answers)}\n')
        print("The entry has been successfully added to the phone book!\n")

    else:
        print("The data already exists!")


def change_contact(data_tuple):

    global all_data
    symbol = "\n"

    record_id, num_data, data = data_tuple

    for i, v in enumerate(all_data):
        if v.split()[0] == record_id:
            v = v.split()
            v[int(num_data)] = data
            if exist_contact(0, " ".join(v[1:])):
                print("The data already exists!")
                return
            all_data[i] = " ".join(v)
            break

    with open(file_base, 'w', encoding="utf-8") as f:
        f.write(f'{symbol.join(all_data)}\n')
    print("Record changed!\n")


def data_collection(num):

    answer = input(f"Enter a {num}: ")
    while True:
        if num in "surname name patronymic":
            if answer.isalpha():
                break
        if num == "phone number":
            if answer.isdigit() and len(answer) == 11:
                break
        answer = input(f"Data is incorrect!\n"
                       f"Use only use only the letters"
                       f" of the alphabet, the length"
                       f" of the number is 11 digits\n"
                       f"Enter a {num}: ")
    return answer


def edit_menu():

    add_dict = {"1": "surname", "2": "name", "3": "patronymic", "4": "phone number"}

    show_all()
    record_id = input("Enter the record id: ")

    if exist_contact(record_id, ""):
        while True:
            print("\nChanging:")
            change = input("1. surname\n"
                           "2. name\n"
                           "3. patronymic\n"
                           "4. phone number\n"
                           "5. exit\n")
            
            match change:
                case "1" | "2" | "3" | "4":
                    return record_id, change, data_collection(add_dict[change])
                case "5":
                    return 0
                case _:
                    print("The data is not recognized, repeat the input.")

    else:
        print("The data is not correct!")

def exp_bd(name):

    symbol = "\n"
    change_name = f"{name}.txt"
    if not path.exists(change_name):
        with open(change_name, "w", encoding="utf-8") as f:
            f.write(f'{symbol.join(all_data)}\n')

def imp_bd(name):
    global file_base

    if path.exists(name):
        file_base = name
        read_records()

def exp_imp_menu():

    while True:
        print("\nExp/Imp menu:")
        move = input("1. Import\n"
                     "2. Export\n"
                     "3. exit\n")

        match move:
            case "1":
                imp_bd(input("Enter the name of the file: "))
            case "2":
                exp_bd(input("Enter the name of the file: "))
            case "3":
                return 0
            case _:
                print("The data is not recognized, repeat the input.")

def main_menu():
    global all_data, last_id
    play = True
    while play:
        read_records()
        answer = input("Phone book:\n"
                       "1. Show all records\n"
                       "2. Add a record\n"
                       "3. Search a record\n"
                       "4. Delete\n"
                       "5. Exit\n\n")
        match answer:
            case "1":
                show_all()
                con = input("\nFor contuning press any button..")
            case "2":
                add_new_contact()
            case "3":
                pass
            case "4":
                delete()
                con
            case "5":
                play = False
            case _:
                print("Try again!!! You can do it!!! \n")
                con

main_menu()