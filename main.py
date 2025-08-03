import tkinter as tk
import time
from tkinter import messagebox

#List some sample courses that are available
courses = {
    "Bachelor of Science (Majored in Biomed)": {
        "rank_score_required": 280,
        "subject_requirement": ["None"]
    },
    "Bachelor of Engineering (Honours)": {
        "rank_score_required": 260,
        "subject_requirement": ["Calculus", "Physics"]
    }
}

#List some career options that are available
career_options = {
    "Science": ["Biomedical Scientist", "Pharmacist", "Geneticist"],
    "Technology": ["Software Engineer", "Data Analyst", "Urban Planning"],
    "Health": ["Nurse", "Public Health Advisor", "Surgeon"]
}

#List some possible career questions and answers for FROST module
frostQA = {
    "What is NCEA?": "NCEA stands for the National Certificate of Educational Achievement, and is the main secondary qualification in NZ. ",
    "What is a rank score?": "A rank score is a calculated score used by University of Auckland (and some majors in Auckland University of Technology) based on a student's NCEA results. ",
    "What is the University Entrance?": "University Entrance is the minimum requirement needed for a secondary student to have tertiary study in NZ with NCEA. It includes NCEA Level 3, 14 credits at Level 3 in each of three approved subjects, 10 Literacy credits at Level 2 or above made up of 5 reading and 5 writing, along with 0 Literacy credits at Level 2 or above. "
}

#Develop the class for my UI and home page
class GradusApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gradus(V1) - Alec Pan")
        self.root.geometry("400x600")

        button_frame = tk.Frame(root)
        button_frame.pack(side="top", fill="x")

        self.frames = {}
        for name in ["Home", "Grade Checker", "Career Planner", "FROST"]:
            frame = tk.Frame(root)
            frame.place(x=0, y=50, relwidth=1, relheight=1)
            self.frames[name] = frame

        self.home = Home(self.frames["Home"])
        self.grade_checker = GradeChecker(self.frames["Grade Checker"])
        self.career_planner = CareerPlanner(self.frames["Career Planner"])
        self.frost = FROST(self.frames["FROST"])

        self.home.build()
        self.grade_checker.build()
        self.career_planner.build()
        self.frost.build()

        tk.Button(button_frame, text="Home", command=lambda: self.show_frame("Home")).pack(side="left", expand=True)
        tk.Button(button_frame, text="Grade Checker", command=lambda: self.show_frame("Grade Checker")).pack(side="left", expand=True)
        tk.Button(button_frame, text="Cereer Planner", command=lambda: self.show_frame("Career Planner")).pack(side="left", expand=True)
        tk.Button(button_frame, text="FROST", command=lambda: self.show_frame("FROST")).pack(side="left", expand=True)
        tk.Button(button_frame, text="Exit", command=lambda: self.show_frame("Exit")).pack(side="left")
        self.show_frame("Home")

    def show_frame(self, name):
        for frame in self.frames.values():
            frame.lower()
        self.frames[name].lift()
    
class Home:
    def __init__(self, frame):
        self.frame = frame

    def build(self):
        tk.Label(self.frame, text="Thank you for using Gradus:", font=("Arial", 16, "bold")).pack(pady=20)
        tk.Label(self.frame, text="We are aiming to help students to plan their university and career pathways.", wraplength=360, justify="center").pack(pady=10)
        tk.Label(self.frame, text="Use the top buttons to explore some modules to help you out! \nVersion 1", font=("Arial", 10), fg="Gray").pack(pady=10)

#Develop the class for the Grader Checker
class GradeChecker:
    def __init__(self, frame):
        self.frame = frame
        self.rank_score_entry = tk.Entry(frame)
        self.course_var = tk.StringVar(frame)
        self.course_var.set(list(courses.keys())[0])

    def build(self):
        tk.Label(self.frame, text="Grade Checker", font=("Arial", 14)).pack(pady=5)
        tk.Label(self.frame, text="Enter your rank score: ").pack()
        self.rank_score_entry.pack()
        course_menu = tk.OptionMenu(self.frame, self.course_var, *courses.keys())
        course_menu.pack(pady=5)
        tk.Button(self.frame, text="Check Entry", command=self.grade_check).pack(pady=10)

    def grade_check(self):
        try:
            rank_score = int(self.rank_score_entry.get())
            course_selected = self.course_var.get()
            rank_score_required = courses[course_selected]["rank_score_required"]

            if rank_score >= rank_score_required and rank_score <= 320:
                messagebox.showinfo("Result:", f"Congradulations! You have met the rank score entry requirement for {course_selected}")
            elif rank_score < rank_score_required:
                messagebox.showinfo("Result:", f"Sorry, but you do NOT meet the entry requirement for {course_selected}")
            elif rank_score > 320 or rank_score < 0:
                messagebox.showerror("Error", f"Please enter a smaller but valid rank score.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid rank score.")

#Develop the class for the Career Planner
class CareerPlanner:
    def __init__(self, frame):
        self.frame = frame
        self.user_interest_var = tk.StringVar(frame)
        self.user_interest_var.set(list(career_options.keys())[0])
    
    def build(self):
        tk.Label(self.frame, text="Career Planner", font=("Arial", 14)).pack(pady=10)
        tk.Label(self.frame, text="Select your area of interest!").pack()
        user_interest_menu = tk.OptionMenu(self.frame, self.user_interest_var, career_options.keys())
        user_interest_menu.pack(pady=5)
        tk.Button(self.frame, text="Suggest Careers", command=self.career_suggestion).pack(pady=10)

    def career_suggestion(self):
        selected_field_of_interest = self.user_interest_var.get()
        careers = career_options.get(selected_field_of_interest, {})
        if careers:
            messagebox.showinfo("Suggested Careers:", f"Some careers that you might be interested include: {', '.join(careers)}")
        else:
            messagebox.showerror("Error", "No careers can be suggested for this field of interest.")

#Develop the class for the FROST
class FROST:

    def __init__(self, frame):
        self.frame = frame
        global frostQA
    
    def build(self):
        tk.Label(self.frame, text="FROST", font=("Arial", 14)).pack(pady=10)
        for question, answer in frostQA.items():
            tk.Label(self.frame, text=f"Q: {question}", font=("Arial", 14, "bold")).pack(anchor="w", padx=10)
            tk.Label(self.frame, text=f"A: {answer}", wraplength=400, justify="right").pack(anchor="w", padx=20, pady=2)

#Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = GradusApp(root)
    root.mainloop()