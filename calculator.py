from registration import Merge
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
        registered = Merge("dummy", "dummy")  # Create dummy Merge to access .data
        users = registered.get_users()

        if name in users:
            return f"{name.title()} is a registered user."
        else:
            return f"{name.title()} is NOT registered."
    def its_you_full_check(self, name):
        merge = Merge("dummy", "dummy")
        if name in merge.data:
            _, real_id = list(merge.data[name].items())[0]
            if self.code == real_id:
                return f"{name.title()} verified by ID."
            else:
                return f"{name.title()} exists but code does not match."
        else:
            return f"{name.title()} is NOT registered."


            