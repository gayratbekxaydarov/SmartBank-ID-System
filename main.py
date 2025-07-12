
from registration import UserManager, run_gui  

class Bank:
    def __init__(self, money, code):
        self.money = money
        self.code = code

class Account(Bank):
    def __init__(self, money, code):
        super().__init__(money, code)

    def add_money_code(self, money, code):
        self.money = money
        self.code = code
        return self.money, self.code

    def its_you(self, name):
        registered = UserManager("dummy", "dummy")  
        users = registered.get_users()

        if name in users:
            return f"{name.title()} is a registered user."
        else:
            return f"{name.title()} is NOT registered."

    def its_you_full_check(self, name):
        checker = UserManager("dummy", "dummy")
        if name in checker.data:
            _, real_id = list(checker.data[name].items())[0]
            if self.code == real_id:
                return f"{name.title()} verified by ID."
            else:
                return f"{name.title()} exists but code does not match."
        else:
            return f"{name.title()} is NOT registered."


# ========== Run section ==========
if __name__ == "__main__":
    # run_gui(UserManager("default", "user"))
    user = UserManager("naruto", "uzumaki")
    user.add_user()
    print(user.see_user("naruto"))
    account = Account(5000, user.user_id)

    print(account.its_you("naruto"))            # Ism 
    print(account.its_you_full_check("naruto")) # ID 
    print("Updated:", account.add_money_code(10000, user.user_id))
