#This is main.py, the file that contains the classes and functions along with the UI
import tkinter as tk
from tkinter import messagebox, Toplevel, Listbox
from database import accounts, get_suggested_careers, career_database, strength_database #Import information stored in the database

class User: #Create the class for basic user, which has neither interest nor strength added
    def __init__(self, username):
        self.username = username
        self.interests = []
        self.strengths = []

class Authorization: #Create the class for authorization that has the function of login and creating account
    def __init__(self):
        self.logged_in_user = None

    def login(self, username, password):
        if username in accounts and accounts[username] == password:
            self.logged_in_user = username
            return True #Log in the user
        return False #Get rid of the authorization system as the user has already logged in

    def create_account(self, username, password):
        if username in accounts:
            return False
        accounts[username] = password
        return True
        #Does not return false as the user will return to the login page still

class CareerPlanner:
    def __init__(self, root):
        self.root = root
        self.root.title("Career Planner")
        self.root.geometry("700x500")
        self.root.configure(bg="#E6F0FF") #The basic colour of the app

        self.authorization = Authorization()
        self.user = None

        self.login_screen()

    def login_screen(self): #This is the development of the login screen which will mostly be UI development
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Career Planner", bg="#E6F0FF", fg="#007BFF", font=("Arial", 24, "bold")).pack(pady=30) #Chose the blue colour for our theme for Gradus
        tk.Label(self.root, text="Username:", bg="#E6F0FF", font=("Arial", 12)).pack()
        self.entered_username = tk.Entry(self.root, width=30)
        self.entered_username.pack(pady=5)

        tk.Label(self.root, text="Password:", bg="#E6F0FF", font=("Arial", 12)).pack()
        self.entered_password = tk.Entry(self.root, show="*", width=30)
        self.entered_password.pack(pady=5)

        tk.Button(self.root, text="Login", command=self.login_user, bg="#007BFF", fg="white", width=20).pack(pady=5)
        tk.Button(self.root, text="Create Account", command=self.create_account, bg="#00AA00", fg="white", width=20).pack(pady=5)

    def login_user(self): #Create the function to login existing users
        username = self.entered_username.get() #Get current values from what user have entered and process the information
        password = self.entered_password.get()
        if self.authorization.login(username, password):
            self.user = User(username)
            messagebox.showinfo("Welcome", f"Login successful! Welcome to Gradus, {username}.")
            self.show_main_menu() #Successfully login the user
        else:
            messagebox.showerror("Error", "Login unsuccessful, please double check your username and password.") #Warn the user if there is any error

    def create_account(self): #Create the function for users to create accounts when they do not have any
        username = self.entered_username.get()
        password = self.entered_password.get()

        if not username or not password:
            messagebox.showwarning("Error", "Please fill in both username and password!")
            return False #Return back to the authorization screen

        if self.authorization.create_account(username, password):
            messagebox.showinfo("Account Created", "Your have successfully created your account!")
        else:
            messagebox.showwarning("Error", "Account already exist. Please login or create a different account.")

    def show_main_menu(self): #Create the function for the main menu of the program
        for widget in self.root.winfo_children():
            widget.destroy()
        #Create the UI buttons for each core function
        tk.Label(self.root, text=f"Welcome to Gradus, {self.user.username}!", bg="#E6F0FF", fg="#003366", font=("Arial", 18, "bold")).pack(pady=20)
        tk.Button(self.root, text="Add Interest", command=self.add_interest, bg="#007BFF", fg="white", width=25).pack(pady=5)
        tk.Button(self.root, text="Add Strength", command=self.add_strength, bg="#007BFF", fg="white", width=25).pack(pady=5)
        tk.Button(self.root, text="View Profile", command=self.view_profile, bg="#007BFF", fg="white", width=25).pack(pady=5)
        tk.Button(self.root, text="Suggest Careers", command=self.suggest_careers, bg="#007BFF", fg="white", width=25).pack(pady=5)
        tk.Button(self.root, text="Logout", command=self.login_screen, bg="#CC0000", fg="white", width=25).pack(pady=10)

    def add_interest(self): #Create the function to add interests to user profile
        window = tk.Toplevel(self.root)
        window.title("Select an Interest to Add")
        tk.Label(window, text="Select an NCEA Level 3 Subject from below", font=("Arial", 14, "bold"), bg="#FFFFFF").pack(pady=10)
        for subject in career_database.keys():
            tk.Button(window, text=subject, font=("Arial", 8), bg="#007BFF", fg="white", width=25, command=lambda s=subject: self.select_interest(s, window)).pack(pady=3) #This dynamically create buttons for each subject from the database imported

    def select_interest(self, subject, window):
        if subject not in self.user.interests:
            self.user.interests.append(subject)
            messagebox.showinfo("Added", f"Interest '{subject}' successfully added!")
        else:
            messagebox.showinfo("Info", f"'{subject}' is already in your interests.")
        window.destroy() #Destroy the window that poped up

    def add_strength(self): #Create the function to add strength to user profile, it is basically the same as adding interest
        window = tk.Toplevel(self.root)
        window.title("Select a Strength")
        tk.Label(window, text="Select a Strength", font=("Arial", 14, "bold"), bg="#FFFFFF").pack(pady=10)
        for skill in strength_database.keys():
            tk.Button(window, text=skill, bg="#007BFF",fg="white", width=25, command=lambda s=skill: self.select_strength(s, window)).pack(pady=3)

    def select_strength(self, strength, window):
        if strength not in self.user.strengths:
            self.user.strengths.append(strength)
            messagebox.showinfo("Added", f"Strength '{strength}' successfully added!")
        else:
            messagebox.showinfo("Info", f"'{strength}' is already in your strengths.")
        window.destroy()

    def view_profile(self): #Create the function for the user profile
        window = Toplevel(self.root)
        window.title("Profile")
        window.geometry("500x450")
        window.configure(bg="#E6F0FF")
        tk.Label(window, text=f"{self.user.username}'s Profile", bg="#E6F0FF", fg="#003366", font=("Arial", 16, "bold")).pack(pady=10) #Displays the username of the user
        tk.Label(window, text="Your Interests:", bg="#E6F0FF", font=("Arial", 12, "bold")).pack()
        interest_list = Listbox(window, selectmode=tk.SINGLE, width=40, height=5)
        interest_list.pack(pady=5)
        for interest in self.user.interests:
            interest_list.insert(tk.END, interest) #Lists the interests of the user
        tk.Button(window, text="Remove Selected Interest", bg="#CC0000", fg="white", width=25, command=lambda: self.remove_item(interest_list, self.user.interests, "interest")).pack(pady=3) #Remove selected interest from the list so it gets removed in the system

        tk.Label(window, text="Your Strengths:", bg="#E6F0FF", font=("Arial", 12, "bold")).pack(pady=(15, 0))
        strength_list = Listbox(window, selectmode=tk.SINGLE, width=40, height=5)
        strength_list.pack(pady=5)
        for strength in self.user.strengths:
            strength_list.insert(tk.END, strength) #Lists the strengths of the user
        tk.Button(window, text="Remove Selected Strength", bg="#CC0000", fg="white", width=25, command=lambda: self.remove_item(strength_list, self.user.strengths, "strength")).pack(pady=3) #Remove selected strength from the list so it gets removed in the system

    def remove_item(self, listbox, data_list, item_type):
        selection = listbox.curselection()
        if not selection:
            messagebox.showinfo("Info", f"No {item_type} selected to remove.")
            return False #Return false if there is no items that is selected to be removed
        selected = listbox.get(selection)
        data_list.remove(selected)
        listbox.delete(selection)
        messagebox.showinfo("Removed", f"{item_type.title()} '{selected}' is successfully removed!")

    def suggest_careers(self): #Create the function for career suggestion
        if not self.user.interests and not self.user.strengths:
            messagebox.showwarning("Error", "Please add at least one interest or strength first.")
            return False #Return false value if there is no interests nor strengths added into the program, as suggestions are based on them
        suggested_careers = get_suggested_careers(self.user.interests, self.user.strengths)
        if suggested_careers:
            messagebox.showinfo("Career Suggestions", "Your top three career matches:\n" + "\n".join(suggested_careers))
        else:
            messagebox.showinfo("Career Suggestions", "No matching careers found. Try adding some more interests or/and strengths.")

if __name__ == "__main__": #Run the program
    root = tk.Tk()
    app = CareerPlanner(root)
    root.mainloop()