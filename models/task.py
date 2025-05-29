from models.status import Status

class TaskStatusError(Exception):
    pass

class Task:
    def __init__(self, title: str, description: str, status: Status = Status.TODO):
        self.title = title
        self.description = description
        self.status = status

    def change_status(self, new_status: Status):
        if not isinstance(new_status, Status):
            raise TaskStatusError("Invalid status.")
        self.status = new_status

    def __repr__(self):
        return f"{self.title} - {self.status.value}"
