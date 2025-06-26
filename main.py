from models.task import Task, TaskStatusError
from models.status import Status
from models.user import User
from utils.display import display_tasks

tasks = []
users = []

def find_user(username):
    return next((u for u in users if u.username == username), None)

def menu():
    while True:
        print("\n--- Kanban CLI ---")
        print("1. Dodaj użytkownika")
        print("2. Dodaj zadanie")
        print("3. Wyświetl wszystkie zadania")
        print("4. Zmień status zadania")
        print("5. Przypisz użytkownika do zadania")
        print("6. Filtruj zadania po statusie")
        print("0. Wyjdź")

        choice = input("Wybierz opcję: ")

        if choice == "1":
            username = input("Podaj nazwę użytkownika: ")
            if find_user(username):
                print("Taki użytkownik już istnieje.")
            else:
                users.append(User(username))
                print("Użytkownik dodany.")

        elif choice == "2":
            title = input("Tytuł zadania: ")
            desc = input("Opis: ")
            assigned = input("Przypisz użytkownika (opcjonalnie): ")
            user = find_user(assigned) if assigned else None
            tasks.append(Task(title, desc, assigned_to=user))

        elif choice == "3":
            display_tasks(tasks)

        elif choice == "4":
            display_tasks(tasks)
            idx = int(input("Podaj ID zadania: "))
            print("Dostępne statusy: TODO, IN_PROGRESS, DONE")
            new_status = input("Nowy status: ").upper()
            try:
                tasks[idx].change_status(Status[new_status])
            except (IndexError, KeyError, TaskStatusError):
                print("Błąd przy zmianie statusu.")

        elif choice == "5":
            display_tasks(tasks)
            idx = int(input("ID zadania do przypisania: "))
            username = input("Nazwa użytkownika: ")
            user = find_user(username)
            if user:
                tasks[idx].assign_user(user)
                print("Użytkownik przypisany.")
            else:
                print("Nie znaleziono użytkownika.")

        elif choice == "6":
            status_filter = input("Status (TODO, IN_PROGRESS, DONE): ").upper()
            try:
                filtered = list(filter(lambda t: t.status == Status[status_filter], tasks))
                display_tasks(filtered)
            except KeyError:
                print("Nieprawidłowy status.")

        elif choice == "0":
            break
        else:
            print("Nieznana opcja.")

if __name__ == "__main__":
    menu()
