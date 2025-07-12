import uuid
import datetime as dt
import json
import tkinter as tk
from tkinter import messagebox

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = str(uuid.uuid4())
        self.data = {
            'jinx': {"none": '58a9dcc5-8511-4fd7-800e-6a95a5d8fb95'},
            'gojo': {"satoru": "9243f43a-da7b-43b5-acf2-dddecb6afb88"},
            'tony': {"stark": "30ad41af-b0f0-4e22-ac65-2fe3220e6965"}
        }

class UserManager(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)

    def get_users(self):
        return list(self.data.keys())

    def add_user(self):
        self.data[self.first_name] = {self.last_name: self.user_id}
        return self.data

    def registration_time(self, name):
        if name == self.first_name:
            return f"You registered at: {dt.datetime.now()}"
        else:
            return "You are not this person."

    def see_user(self, name):
        if name in self.data:
            last_name, user_id = list(self.data[name].items())[0]
            return f"{name.title()}'s Info:\nLast Name - {last_name} --- ID - {user_id}"
        else:
            return "User not found."

    def delete_user(self, name):
        if name in self.data:
            del self.data[name]
            return f"{name} was successfully deleted."
        else:
            return "User not found. Cannot delete."

    def find_by_id(self, search_id):
        for fname, details in self.data.items():
            for lname, uid in details.items():
                if uid == search_id:
                    return f"Found: {fname.title()} {lname.title()}"
        return "No user found with that ID."

    def save_to_file(self, filename="data.json"):
        with open(filename, "w") as f:
            json.dump(self.data, f, indent=4)
        return "Data saved to file."

    def load_from_file(self, filename="data.json"):
        try:
            with open(filename, "r") as f:
                self.data = json.load(f)
            return "Data loaded from file."
        except FileNotFoundError:
            return "File not found."

def run_gui(manager):
    def add_user_gui():
        fname = entry_first.get()
        lname = entry_last.get()
        if fname and lname:
            manager.first_name = fname
            manager.last_name = lname
            manager.add_user()
            messagebox.showinfo("Success", f"{fname} {lname} has been added.")
        else:
            messagebox.showwarning("Warning", "Please enter both first and last names.")

    window = tk.Tk()
    window.title("User Registration")
    window.geometry("300x200")

    tk.Label(window, text="First Name:").pack()
    entry_first = tk.Entry(window)
    entry_first.pack()

    tk.Label(window, text="Last Name:").pack()
    entry_last = tk.Entry(window)
    entry_last.pack()

    tk.Button(window, text="Add User", command=add_user_gui).pack(pady=10)
    window.mainloop()
# for example
user_manager = UserManager("tony", "stark")

print(user_manager.see_user("gojo"))
print(user_manager.registration_time("tony"))
print(user_manager.get_users())
print(user_manager.find_by_id("30ad41af-b0f0-4e22-ac65-2fe3220e6965"))
print(user_manager.delete_user("jinx"))
print(user_manager.save_to_file())
print(user_manager.load_from_file())