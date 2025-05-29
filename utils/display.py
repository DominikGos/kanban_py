def display_tasks(tasks):
    if not tasks:
        print("Brak zadań.")
        return

    print(f"{'ID':<4}{'Tytuł':<20}{'Status':<15}")
    print("-" * 40)
    for i, task in enumerate(tasks):
        print(f"{i:<4}{task.title:<20}{task.status.value:<15}")
