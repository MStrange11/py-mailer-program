import Mail as M

# recipients = [
#     'gta5andepic@gmail.com',
#     # 'suthara830@gmail.com'
#     # 'drtas2521@gmail.com'
#     ]

reci = {
    "meeting":['gta5andepic@gmail.com'],
    "old user":['gta5andepic@gmail.com', "EpicStrange0@gmail.com"],
    "new user":['gta5andepic@gmail.com','utsav.sehgal.123@gmail.com']
}

class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role
        self.status = "logout"

        if role == 'admin':
            self.pKey = 1245
        elif role == 'view':
            self.pKey = 3654
            print("view role don't have access to send mail.\n")
        else:
            return False
        
        if self.get_login():
            print(f"{username} logined Success")
            self.status = "login"
        else:
            print(f"{username} login fail")

    
    def get_login(self):
        trials = 2
        in_pin = input("Enter your login pin: ")
        while in_pin != str(self.pKey):
            print("\nYou entered wrong pin!")
            in_pin = input("Enter your login pin: ")

            if trials == 0 :
                return False
            trials -= 1
        
        return True

    # def verify_pass(self, pin):
    #     if len(str(pin)) != 4:
    #         for n in str(pin):
    #             if not n.isdigit():
    #                 return True
    #     return False
    
    # def change_pKey(self, trials = 2):
    #     old_pKey = int(input("Enter current pass key : "))
    #     if old_pKey == self.pKey:
    #         print("Only 4 digit pin allowed!")
    #         new_pKey = int(input("Enter new pass key : "))
    #         while self.verify_pass(new_pKey):
    #             new_pKey = int(input("Enter new pass key : "))
    #     else:
    #         if trials == 0 :
    #             return False
    #         self.change_pKey(trials - 1 )
                


class Userhandler:
    def __init__(self):
        self.users = []

    def add_user(self, username, role):
        user = User(username, role)
        if user.status == "logout":
            return False
        self.users.append(user)
        M.Logs().log("\n"+username + " login as "+role)
        return user

