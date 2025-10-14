import tkinter as tk
from tkinter import messagebox

class User: #Create the class for user information
    def __init__(self):
        self.interests = []
        self.strengths = []
    
    #Buttons and functions for adding and removing interests and strengths
    def add_interest(self, interest):
        if interest and interest not in self.interests:
            self.interests.append(interest)

    def add_strength(self, strength):
        if strength and strength not in self.strengths:
            self.strengths.append(strength)

    def remove_interest(self, interest):
        if interest in self.interests:
            self.interests.remove(interest)

    def remove_strength(self, strength):
        if strength in self.strengths:
            self.strengths.remove(strength)

    def get_profile(self):
        return f"Interests: {', '.join(self.interests) or 'None'}\nStrengths: {', '.join(self.strengths) or 'None'}"

class CareerPlanner:
    def __init__(self, user_profile):
        self.user_profile = user_profile
        self.career_database = { #Really simple database, but extended compared to previous one
            "physics": ["Engineering", "Aviation", "Architecture"],
            "math": ["Engineering", "Data Science", "Finance"],
            "biology": ["Medicine", "Biotechnology", "Environmental Science"],
            "english": ["Communications", "Teaching", "Law"],
            "chemistry": ["Pharmacy", "Food Science", "Chemical Engineering"],
            "computer science": ["Software Development", "Cybersecurity", "AI Research"]
        }

    def suggest_career(self): #Create the core function of the program that suggests careers based on previous user inputs
        suggest = set()
        for item in self.user_profile.interests + self.user_profile.strengths:
            stuff = item.lower()
            if stuff in self.career_database:
                suggest.update(self.career_database[stuff])
        if suggest:
            return f"Suggested Careers:\n- " + "\n- ".join(suggest)
        else:
            return "No suggestions available."

class CareerPlannerApp: #Create the class for the app itself, which is also the UI
    def __init__(self, root):
        self.root = root
        self.root.title("Gradus - Career Planner - Version 3")
        self.user = User()
        self.planner = CareerPlanner(self.user)
        self.create_home_screen()

    def frame_clearing(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def create_home_screen(self): #Create the home screen in forms of UI
        self.frame_clearing()
        tk.Label(self.root, text="Welcome to Gradus Career Planner", font=("Arial", 18, "bold")).pack(pady=10) #Creates and labels the buttons. Same as below
        tk.Label(self.root, text="Select an option below:", font=("Arial", 12)).pack(pady=5)
        tk.Button(self.root, text="Add Interest", width=20, command=self.show_add_interest).pack(pady=5)
        tk.Button(self.root, text="Add Strength", width=20, command=self.show_add_strength).pack(pady=5)
        tk.Button(self.root, text="View Profile", width=20, command=self.show_profile).pack(pady=5)
        tk.Button(self.root, text="Remove Interest", width=20, command=self.show_remove_interest).pack(pady=5)
        tk.Button(self.root, text="Remove Strength", width=20, command=self.show_remove_strength).pack(pady=5)
        tk.Button(self.root, text="Suggest Career", width=20, command=self.show_suggestions).pack(pady=5)
        tk.Button(self.root, text="Exit", width=20, command=self.root.quit).pack(pady=5)

    def show_add_interest(self): #The function to show the UI of adding interest. Same as below
        self.frame_clearing()
        tk.Label(self.root, text="Add Interest", font=("Arial", 12)).pack(pady=5)
        tk.Label(self.root, text="Possible subjects: Physics, Maths, Biology, English, Chemistry and Computer Science.", font=("Arial", 8)).pack(pady=10) #Display a text to show users possible options
        entry = tk.Entry(self.root, width=30)
        entry.pack(pady=5)
        tk.Button(self.root, text="Add", command=lambda: self.add_interest(entry.get())).pack(pady=5)
        tk.Button(self.root, text="Back", command=self.create_home_screen).pack(pady=10)

    def add_interest(self, interest): #Function of adding interest itself. Same as below
        self.user.add_interest(interest)
        messagebox.showinfo("Success", f"Added interest: {interest}") #Tell the user that the typed interest is successfully added
        self.create_home_screen()

    def show_add_strength(self):
        self.frame_clearing()
        tk.Label(self.root, text="Add Strength", font=("Arial", 12)).pack(pady=5)
        tk.Label(self.root, text="Possible subjects: Physics, Maths, Biology, English, Chemistry and Computer Science.", font=("Arial", 8)).pack(pady=10)
        entry = tk.Entry(self.root, width=30)
        entry.pack(pady=5)
        tk.Button(self.root, text="Add", command=lambda: self.add_strength(entry.get())).pack(pady=5)
        tk.Button(self.root, text="Back", command=self.create_home_screen).pack(pady=10)

    def add_strength(self, strength):
        self.user.add_strength(strength)
        messagebox.showinfo("Success", f"Added strength: {strength}")
        self.create_home_screen()

    def show_remove_interest(self):
        self.frame_clearing()
        tk.Label(self.root, text="Enter Interest to Remove:", font=("Arial", 12)).pack(pady=5)
        entry = tk.Entry(self.root, width=30)
        entry.pack(pady=5)
        tk.Button(self.root, text="Remove", command=lambda: self.remove_interest(entry.get())).pack(pady=5)
        tk.Button(self.root, text="Back", command=self.create_home_screen).pack(pady=10)

    def remove_interest(self, interest):
        self.user.remove_interest(interest)
        messagebox.showinfo("Removed", f"Removed interest: {interest}")
        self.create_home_screen()

    def show_remove_strength(self):
        self.frame_clearing()
        tk.Label(self.root, text="Enter Strength to Remove:", font=("Arial", 12)).pack(pady=5)
        entry = tk.Entry(self.root, width=30)
        entry.pack(pady=5)
        tk.Button(self.root, text="Remove", command=lambda: self.remove_strength(entry.get())).pack(pady=5)
        tk.Button(self.root, text="Back", command=self.create_home_screen).pack(pady=10)

    def remove_strength(self, strength):
        self.user.remove_strength(strength)
        messagebox.showinfo("Removed", f"Removed strength: {strength}")
        self.create_home_screen()

    def show_profile(self): #Creates the function to show profiles
        self.frame_clearing()
        tk.Label(self.root, text="User Profile", font=("Arial", 16, "bold")).pack(pady=10)
        tk.Label(self.root, text=self.user.get_profile(), font=("Arial", 12), justify="left").pack(pady=10)
        tk.Button(self.root, text="Back", command=self.create_home_screen).pack(pady=10)

    def show_suggestions(self): #Creates the function to show suggestions
        self.frame_clearing()
        tk.Label(self.root, text="Career Suggestions", font=("Arial", 14, "bold")).pack(pady=10)
        tk.Label(self.root, text=self.planner.suggest_career(), font=("Arial", 12), justify="left").pack(pady=10)
        tk.Button(self.root, text="Back", command=self.create_home_screen).pack(pady=10)

#Runs the app
if __name__ == "__main__":
    root = tk.Tk()
    app = CareerPlannerApp(root)
    root.geometry("600x700")
    root.mainloop()
