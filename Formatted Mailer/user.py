class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role

        if role == 'admin':
            self.pKey = 1245
        elif role == 'viewer':
            self.pKey = 3654
        
        print(f"{username} login password : {self.pKey}")

class Userhandler:
    def __init__(self):
        self.users = []

    def add_user(self, username, role):
        user = User(username, role)
        self.users.append(user)
