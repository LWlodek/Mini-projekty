user_choice = -1
list_of_tasks = []

def load_tasks_from_file():
    try:
        file_name = input("Podaj nazwę listy zadań, z którą chcesz pracować.")
        file = open(file_name + '.txt')
        for lines in file.readlines():
            list_of_tasks.append(lines.strip())
        file.close()
        return file
    except FileNotFoundError:
        new_file = input("Nie znaleziono takiej listy. Tworzę nową, nadaj jej nazwę.")
        file = open(new_file + '.txt', "w")
        file.close()
        return

def show_tasks():
    task_indeks = 0
    for task in list_of_tasks:
        print(task + ' [' + str(task_indeks) + ']')
        task_indeks +=1

def add_task():
    new_task = input("Podaj treść nowego zadania")
    list_of_tasks.append(new_task)
    print("Zadanie dodane.")

def delete_task():
    try:
        print("Obecne zadania")
        show_tasks()
        task_to_delete = int(input("Podaj numer zadania do skasowania"))
        if task_to_delete < 0 or task_to_delete > len(list_of_tasks) - 1:
            print("Niewłaściwy numer zadania")
            return
        list_of_tasks.pop(task_to_delete)
        print("Zadanie skasowane.")
    except ValueError:
        print("Musisz podać numer!")

def save_changes():
    file_name = input("Do jakiego pliku zapiasc zadania")
    file = open(file_name + '.txt', "w")
    for task in list_of_tasks:
        file.write(task + "\n")
    file.close()

load_tasks_from_file()
while user_choice != 5:
    print()
    print("Podaj numer akcji:")
    print("1. Pokaż wszystkie zadania.")
    print("2. Dodaj nowe zadanie.")
    print("3. Usuń zadanie.")
    print("4. Zapisz zmiany.")
    print("5. Wyjdź.")
#weryfikacja wartości
    correct_value = False
    while correct_value == False:
        try:
            user_choice = int(input())
            correct_value = True
        except ValueError:
            print("Niewłaściwy format, podaj numer.")
    
    if user_choice == 1:
        show_tasks()
    if user_choice == 2:
        add_task()
    if user_choice == 3:
        delete_task()
    if user_choice == 4:
        save_changes()
    if user_choice < 1 or user_choice > 5:
        print("Niepoprawna wartość, wybierz z poniższej opcji.")