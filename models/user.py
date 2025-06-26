class User:
    def __init__(self, username: str):
        self.username = username

    def __repr__(self):
        return self.username
