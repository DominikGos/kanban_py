from models.status import Status
from models.user import User

class TaskStatusError(Exception):
    pass

class Task:
    def __init__(self, title: str, description: str, assigned_to: User = None, status: Status = Status.TODO):
        self.title = title
        self.description = description
        self.status = status
        self.assigned_to = assigned_to

    def change_status(self, new_status: Status):
        if not isinstance(new_status, Status):
            raise TaskStatusError("Invalid status.")
        self.status = new_status

    def assign_user(self, user: User):
        self.assigned_to = user

    def __repr__(self):
        return f"{self.title} - {self.status.value} - {self.assigned_to.username if self.assigned_to else 'Brak przypisania'}"
