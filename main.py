import tkinter as tk
from tkinter import messagebox

#This is the class for User, which will be the core of the program, organizing buttons on the Home screen
class User:
    def __init__(self):
        self.interest = []
        self.strength = []
    
    def add_interest(self, interest):
        if interest:
            self.interest.append(interest.lower())
            return True
    
    def add_strength(self, strength):
        if strength:
            self.strength.append(strength.lower())
            return True

class CareerPlanner:
    def __init__(self, user):
        self.user = user
        self.career_map = { #The basic database that will store some possible career suggestions
            "physics": ["Engineering", "Aerospace"],
            "math": ["Data Science", "Finance"],
            "biology": ["Medicine", "Biotechnology",],
            "chemistry": ["Pharmacology", "Chemical Engineering"],
            "english": ["Law", "Teaching"],
            "history": ["Politics","Education"],
            "computer science": ["Software Development", "Cybersecurity"]
        }
    
    def career_suggestion(self):
        if not self.user.interest and not self.user.strength:
            return False #Return false if neither interest or strength is found in the user inputs
        
        user_input = self.user.interest + self.user.strength
        suggestion = [""]
        
        for subject in user_input:
            if subject in self.career_map:
                suggestion.extend(self.career_map[subject])
        
        if suggestion:
            special_suggestions = list(set(suggestion))
            return f"Based on your the subjects that you chose, possible careers include: {', '.join(special_suggestions)}."
        else:
            return "No career matches could be found. Try adding subjects like Physics, Math, Biology." #Suggesting user career pathways

class CareerPlannerApp: #This will be the UI development for the Career Planner
    def __init__(self, root):
        self.root = root
        self.root.title("Welcome to Career Planner! This is a core module for the Gradus app, and is an imcomplete version. Version: 2") #Title at top left of the app
        
        self.user = User()
        self.planner = CareerPlanner(self.user)
        self.label = tk.Label(root, text="Enter an NCEA subject as an interest or strength:")
        self.label.pack(pady=10)
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=5)
        self.btn_interest = tk.Button(root, text="Add Interest", command=self.add_interest)
        self.btn_interest.pack(pady=5)
        self.btn_strength = tk.Button(root, text="Add Strength", command=self.add_strength)
        self.btn_strength.pack(pady=5)
        self.btn_suggest = tk.Button(root, text="Suggest Career", command=self.suggestion)
        self.btn_suggest.pack(pady=20)
    
    def add_interest(self): #Function for adding interest into the database
        interest = self.entry.get()
        if self.user.add_interest(interest):
            messagebox.showinfo("Added", f"Interest '{interest}' added.")
            self.entry.delete(0, tk.END)
        else:
            messagebox.showinfo("Empty", "Please type a interest.")
    
    def add_strength(self): #Function for adding strength into the database
        strength = self.entry.get()
        if self.user.add_strength(strength):
            messagebox.showinfo("Added", f"Strength '{strength}' added.")
            self.entry.delete(0, tk.END)
        else:
            messagebox.showinfo("Empty", "Please type a strength before adding.")
    
    def suggestion(self): #Function for suggesting the careers based on user inputs
        suggestion = self.planner.career_suggestion()
        if suggestion:
            messagebox.showinfo("Career Suggestion", suggestion)
        else:
            messagebox.showinfo("Incomplete", "Please add some interests or strengths.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CareerPlannerApp(root)
    root.mainloop()
