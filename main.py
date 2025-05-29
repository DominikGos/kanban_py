from models.task import Task, TaskStatusError
from models.status import Status
from utils.display import display_tasks

tasks = []

def menu():
    while True:
        print("\n--- Kanban CLI ---")
        print("1. Dodaj zadanie")
        print("2. Wyświetl wszystkie zadania")
        print("3. Zmień status zadania")
        print("4. Filtruj zadania po statusie")
        print("0. Wyjdź")

        choice = input("Wybierz opcję: ")

        if choice == "1":
            title = input("Tytuł: ")
            desc = input("Opis: ")
            tasks.append(Task(title, desc))
        elif choice == "2":
            display_tasks(tasks)
        elif choice == "3":
            display_tasks(tasks)
            idx = int(input("Podaj ID zadania: "))
            print("Dostępne statusy: TODO, IN_PROGRESS, DONE")
            new_status = input("Nowy status: ").upper()
            try:
                tasks[idx].change_status(Status[new_status])
            except (IndexError, KeyError, TaskStatusError):
                print("Błąd przy zmianie statusu.")
        elif choice == "4":
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
