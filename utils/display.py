def display_tasks(tasks):
    if not tasks:
        print("Brak zadań.")
        return

    print(f"{'ID':<4}{'Tytuł':<20}{'Status':<15}{'Użytkownik':<15}")
    print("-" * 60)
    for i, task in enumerate(tasks):
        user = task.assigned_to.username if task.assigned_to else "Brak"
        print(f"{i:<4}{task.title:<20}{task.status.value:<15}{user:<15}")
