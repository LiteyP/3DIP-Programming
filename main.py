import tkinter as tk
from tkinter import messagebox, Toplevel, Listbox, Frame, Label, Entry, Button, Scrollbar, Text
from database import accounts, get_suggested_careers, career_categories, strength_database, frost_responses #Import the information stored in the database

class User: #This class creates the empty user profile
    def __init__(self, username): #Creates the function with parameter that has username included. This displays in the User Profile Module
        self.username = username #Store the username for personalization throughout the app
        self.interests = [] #Create an empty list that will store all the user's selected interests from Career Planner, same as below
        self.strengths = []
        self.standards = []
        self.target_rank_score = None

class Authorization: #Create a class for the authorization system, which has both login and create account within it
    def __init__(self):
        self.logged_in_user = None #Make sure that there are no user logged in upon launching the app for security

    def login(self, username, password):
        if username in accounts and accounts[username] == password: #Check if username exists and password matches
            self.logged_in_user = username
            return True #If the username and password are matching in the database, then return true and allow the user to log in
        return False #Return false if login fails due to wrong credentials
    
    def create_account(self, username, password):
        if username in accounts:
            return False #Return false if the user tried to create an account that is already in the system
        accounts[username] = password
        return True #Return true to indicate successful account creation
    
class GradusApp: #This is the application class that handles the UI and module functionalities
    def __init__(self, root):
        self.root = root
        self.root.title("Gradus - Career & Academic Planner") #Set the title of the application window that appears in the title bar
        self.root.geometry("800x600") #Set the default window size
        self.root.configure(bg="#E6F0FF") #Set the background color

        self.authorization = Authorization()
        self.user = None
        self.login_screen() #Start with the login screen as the first thing users see

    def login_screen(self): #Create the login screen interface where users can log in or create accounts
        for widget in self.root.winfo_children():
            widget.destroy() #Clear any existing widgets from the window to start fresh with login screen

        main_frame = Frame(self.root, bg="#E6F0FF")
        main_frame.pack(expand=True, fill="both", padx=50, pady=50) #Center the frame with padding for better appearance

        Label(main_frame, text="Gradus", bg="#E6F0FF", fg="#00B3FF", font=("Arial", 28, "bold")).pack(pady=30)
        Label(main_frame, text="Career & Academic Planner", bg="#E6F0FF", fg="#003366", font=("Arial", 14)).pack(pady=(0, 30))

        form_frame = Frame(main_frame, bg="#E6F0FF") #Create form frame to hold username and password inputs
        form_frame.pack(pady=20)

        #Positions the username
        Label(form_frame, text="Username:", bg="#E6F0FF", font=("Arial", 12)).grid(row=0, column=0, sticky="e", padx=5, pady=10)
        self.entered_username = Entry(form_frame, width=25, font=("Arial", 12))
        self.entered_username.grid(row=0, column=1, padx=5, pady=10)
        
        #Positions the password
        Label(form_frame, text="Password:", bg="#E6F0FF", font=("Arial", 12)).grid(row=1, column=0, sticky="e", padx=5, pady=10) 
        self.entered_password = Entry(form_frame, show="*", width=25, font=("Arial", 12)) 
        self.entered_password.grid(row=1, column=1, padx=5, pady=10)

        Button(main_frame, text="Login", command=self.login_user, bg="#00B3FF", fg="white", font=("Arial", 12), width=15).pack(pady=10) #Lables the button that triggers login process
        Button(main_frame, text="Create Account", command=self.create_account_window, bg="#00AA00", fg="white", font=("Arial", 12), width=15).pack(pady=10) #Lables the button for creating accounts

    def create_account_window(self): #Create a separate window for account creation to keep login screen clean
        window = Toplevel(self.root)
        window.title("Create Account - Gradus")
        window.geometry("400x400")
        window.configure(bg="#E6F0FF")
        window.transient(self.root)
        window.grab_set() #Make window modal so user must interact with it before returning to main window

        Label(window, text="Gradus", bg="#E6F0FF", fg="#00B3FF", font=("Arial", 20, "bold")).pack(pady=15) #Labels the app title
        Label(window, text="Create New Account", bg="#E6F0FF", fg="#003366", font=("Arial", 16, "bold")).pack(pady=10) #Labels the window's header

        form_frame = Frame(window, bg="#E6F0FF") #Create frame to hold account creation form elements
        form_frame.pack(pady=20)

        #Labels new username
        Label(form_frame, text="Username:", bg="#E6F0FF", font=("Arial", 12)).grid(row=0, column=0, sticky="e", padx=5, pady=10)
        new_username = Entry(form_frame, width=20, font=("Arial", 12))
        new_username.grid(row=0, column=1, padx=5, pady=10) 

        #Labels new password
        Label(form_frame, text="Password:", bg="#E6F0FF", font=("Arial", 12)).grid(row=1, column=0, sticky="e", padx=5, pady=10) 
        new_password = Entry(form_frame, show="*", width=20, font=("Arial", 12)) 
        new_password.grid(row=1, column=1, padx=5, pady=10) 

        #Labels the password confirmation
        Label(form_frame, text="Confirm Password:", bg="#E6F0FF", font=("Arial", 12)).grid(row=2, column=0, sticky="e", padx=5, pady=10) 
        confirm_password = Entry(form_frame, show="*", width=20, font=("Arial", 12))
        confirm_password.grid(row=2, column=1, padx=5, pady=10)

        def create_account(): #Creates the function to handle account creation process when user clicks create button
            username = new_username.get().strip() #Get username from entry field and remove any extra whitespace with strip
            password = new_password.get() #Get password from first password field
            confirm = confirm_password.get() #Get password from confirmation field

            if not username or not password: 
                messagebox.showwarning("Error", "Please fill in all fields!") #Show error message if fields are empty
                return #Exit function without creating account

            if password != confirm: 
                messagebox.showwarning("Error", "Passwords do not match!") #Show error if username and password do not match
                
            if len(password) < 3:
                messagebox.showwarning("Error", "Password must be at least 3 characters!") #Show error if password too short
                return #Exit function without creating account

            if self.authorization.create_account(username, password): #Account creation
                messagebox.showinfo("Success", "Account created successfully! Please login.") #Show success message
                window.destroy() #Close the account creation window after successful account creation
            else: 
                messagebox.showwarning("Error", "Username already exists. Please choose a different username.") #Show username taken error

        Button(window, text="Create Account", command=create_account, bg="#00AA00", fg="white", font=("Arial", 12), width=15).pack(pady=10) #Labels the green account creation button
        Button(window, text="Cancel", command=window.destroy, bg="#CC0000", fg="white", font=("Arial", 12), width=15).pack(pady=5) #Labels the red cancelling button

    def login_user(self): #Creates the function to handle user login when they click login button
        username = self.entered_username.get()
        password = self.entered_password.get()
        
        if self.authorization.login(username, password):
            self.user = User(username) #Create a new User object with the logged in username
            messagebox.showinfo("Welcome", f"Login successful! Welcome to Gradus, {username}.") #Welcomes the user
            self.show_main_dashboard() #Proceed to main dashboard after login
        else:
            messagebox.showerror("Error", "Login unsuccessful, please double check your username and password.") #Show error message that login has failed

    def show_main_dashboard(self): #Create the main dashboard with four modules
        for widget in self.root.winfo_children():
            widget.destroy() #Clear the login screen widgets to make space for dashboard

        #Labels the header on the main dashboard
        header_frame = Frame(self.root, bg="#E6F0FF")
        header_frame.pack(fill="x", pady=20)
        Label(header_frame, text=f"Welcome to Gradus, {self.user.username}!", bg="#E6F0FF", fg="#003366", font=("Arial", 20, "bold")).pack()

        #Centers the four main buttons
        center_frame = Frame(self.root, bg="#E6F0FF")
        center_frame.place(relx=0.5, rely=0.5, anchor="center") 

        modules_frame = Frame(center_frame, bg="#E6F0FF") #Holds the buttons in a grid
        modules_frame.pack(expand=True) #Allow frame to expand to fit content

        #Creates and labels the four module buttons with mini icons
        module1_btn = Button(modules_frame, text="📊 Grade Tracker", command=self.grade_tracker_module, bg="#00B3FF", fg="white", font=("Arial", 14, "bold"), width=20, height=3, compound="top")
        module1_btn.grid(row=0, column=0, padx=25, pady=25) #Position in top-left of grid, same as below
        module2_btn = Button(modules_frame, text="🎯 Career Planner", command=self.career_planner_module, bg="#00B3FF", fg="white", font=("Arial", 14, "bold"), width=20, height=3, compound="top")
        module2_btn.grid(row=0, column=1, padx=25, pady=25)
        module3_btn = Button(modules_frame, text="🤖 FROST", command=self.frost_module, bg="#00B3FF", fg="white", font=("Arial", 14, "bold"), width=20, height=3, compound="top")
        module3_btn.grid(row=1, column=0, padx=25, pady=25)
        module4_btn = Button(modules_frame, text="👤 Profile", command=self.profile_module, bg="#00B3FF", fg="white", font=("Arial", 14, "bold"), width=20, height=3, compound="top")
        module4_btn.grid(row=1, column=1, padx=25, pady=25)

        logout_btn = Button(self.root, text="Logout", command=self.login_screen, bg="#CC0000", fg="white", font=("Arial", 12), width=10) #Red logout button to return to login screen
        logout_btn.pack(side="bottom", anchor="se", padx=20, pady=20)

    def grade_tracker_module(self): #MODULE 1: Grade Tracker
        window = Toplevel(self.root) #Create new window
        window.title("Grade Tracker")
        window.geometry("650x650")
        window.configure(bg="#E6F0FF")

        Label(window, text="📊 Grade Tracker", bg="#E6F0FF", fg="#003366", font=("Arial", 18, "bold")).pack(pady=20) #Labels the module title with icon

        add_frame = Frame(window, bg="#E6F0FF") #Create frame for adding new standards
        add_frame.pack(pady=10)

        Label(add_frame, text="Add New Standard:", bg="#E6F0FF", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=4, pady=10) #Header for adding standards

        #Labels the standard input
        Label(add_frame, text="Standard Name:", bg="#E6F0FF").grid(row=1, column=0, padx=5, pady=5) 
        standard_name = Entry(add_frame, width=20) 
        standard_name.grid(row=1, column=1, padx=5, pady=5)

        #Labels the NCEA level selection
        Label(add_frame, text="NCEA Level:", bg="#E6F0FF").grid(row=2, column=0, padx=5, pady=5) 
        level_var = tk.StringVar(value="1")
        level_menu = tk.OptionMenu(add_frame, level_var, "1", "2", "3") #Dropdown menu for NCEA levels 1, 2, or 3
        level_menu.grid(row=2, column=1, padx=5, pady=5)
        
        #Labels the credit selection
        Label(add_frame, text="Credits:", bg="#E6F0FF").grid(row=3, column=0, padx=5, pady=5)
        credits_var = tk.StringVar(value="4")
        credits_menu = tk.OptionMenu(add_frame, credits_var, "2", "3", "4", "5", "6")
        credits_menu.grid(row=3, column=1, padx=5, pady=5)

        #Labels the grade selection
        Label(add_frame, text="Grade:", bg="#E6F0FF").grid(row=4, column=0, padx=5, pady=5)
        grade_var = tk.StringVar(value="Achieved")
        grade_menu = tk.OptionMenu(add_frame, grade_var, "Not Achieved", "Achieved", "Merit", "Excellence")
        grade_menu.grid(row=4, column=1, padx=5, pady=5)

        def add_standard(): #Creates the function to add a new standard to user's profile when they click add button
            name = standard_name.get().strip() #Get standard name from entry field and remove extra whitespace
            if not name:
                messagebox.showwarning("Error", "Please enter a standard name!") #Show error if name is empty
                return 
            
            grade_points = { #Dictionary to convert NCEA grades to point values for rank score calculation
                "Not Achieved": 0,
                "Achieved": 2,
                "Merit": 3,
                "Excellence": 4
            }
            
            standard = { #Create dictionary with all standard information
                "name": name,
                "level": level_var.get(),
                "credits": int(credits_var.get()),
                "grade": grade_var.get(),
                "points": grade_points[grade_var.get()]
            }
            self.user.standards.append(standard) #Add the new standard to user's standards list
            standard_name.delete(0, tk.END) #Clear the standard name entry field for next entry
            messagebox.showinfo("Success", f"Standard '{name}' added with grade: {grade_var.get()}!") #Show that the standard has been successfully added into the profile
            update_standards_list() #Refresh the standards display list

        Button(add_frame, text="Add Standard", command=add_standard, bg="#00B3FF", fg="white").grid(row=5, column=0, columnspan=2, pady=10) #Labels the blue button for adding standards

        rank_frame = Frame(window, bg="#E6F0FF") #Create frame for rank score calculation section
        rank_frame.pack(pady=10) 

        #Labels the rank score entry
        Label(rank_frame, text="Target Rank Score:", bg="#E6F0FF").grid(row=0, column=0, padx=5)
        target_entry = Entry(rank_frame, width=10)
        target_entry.grid(row=0, column=1, padx=5)

        def calculate_rank_score(): #Creates the function to calculate and compare rank score when user clicks check progress
            try:
                target = int(target_entry.get()) #Get target score from entry field and convert to integer
                #Check if the user input is within the range of possible rank scores
                if target < 0:
                    messagebox.showerror("Error", "Target rank score cannot be negative! Please enter a positive number.")
                    return #If not, return, same as below
                if target > 320:
                    messagebox.showerror("Error", "Target rank score cannot exceed 320! Please enter a smaller number.")
                    return
                rank_score = 0
                level_3_standards = [s for s in self.user.standards if s["level"] == "3"] #Filter only Level 3 standards for rank score calculation
                level_3_standards.sort(key=lambda x: x["points"], reverse=True) #Sort standards by points (highest first) to select best standards
                credits_count = 0
                for standard in level_3_standards: #Loop through each Level 3 standard
                    if credits_count + standard["credits"] <= 80: #Check if 80 credits is reached
                        rank_score += standard["credits"]*standard["points"]
                        credits_count += standard["credits"]
                    else: #If adding this standard exceeds 80 credits
                        remaining_credit_space = 80 - credits_count
                        if remaining_credit_space > 0: #If we have some credits remaining to allocate
                            rank_score += remaining_credit_space * standard["points"] #Add points for partial credits
                        break
                total_credits = sum(standard["credits"] for standard in self.user.standards) #Calculate total credits across all standards
                achieved_credits = sum(standard["credits"] for standard in self.user.standards if standard["grade"] != "Not Achieved") #Does not calculate not achieved credits
                if rank_score >= target: #Check if user has met their set rank score
                    messagebox.showinfo("Rank Score", f"🎉 Congratulations!\nYour rank score: {rank_score}\nTarget: {target}\nTotal Credits: {total_credits}\nAchieved Credits: {achieved_credits}") 
                else: #If user hasn't met target yet
                    messagebox.showinfo("Rank Score", f"📚 Keep Working! You are super close!!\nYour rank score: {rank_score}\nTarget: {target}\nYou need {target - rank_score} more points.\nTotal Credits: {total_credits}\nAchieved Credits: {achieved_credits}")
            except ValueError: #If user entered non-numeric value for target
                messagebox.showerror("Error", "Please enter a valid number for target rank score!") 

        Button(rank_frame, text="Check Progress", command=calculate_rank_score, bg="#00B3FF", fg="white").grid(row=0, column=2, padx=10) #Labels the blue button to calculate rank score

        list_frame = Frame(window, bg="#E6F0FF") #Create frame for displaying user's standards list
        list_frame.pack(pady=10, fill="both", expand=True)
        Label(list_frame, text="Your Standards:", bg="#E6F0FF", font=("Arial", 12, "bold")).pack()
        list_container = Frame(list_frame, bg="#E6F0FF") #Create container for listbox and scrollbar
        list_container.pack(fill="both", expand=True, padx=20, pady=5)
        
        #Create and labels the scroll bar and link it to the container
        standards_list = Listbox(list_container, height=8)
        scrollbar = Scrollbar(list_container, orient="vertical", command=standards_list.yview) 
        standards_list.configure(yscrollcommand=scrollbar.set)
        
        #Position listbox on left side and scroll bar on the right
        standards_list.pack(side="left", fill="both", expand=True) 
        scrollbar.pack(side="right", fill="y") 

        def update_standards_list(): #Creates the function to refresh the standards display list
            standards_list.delete(0, tk.END) #Clear current list contents
            for standard in self.user.standards: #Loop
                standards_list.insert(tk.END, f"{standard['name']} (Level {standard['level']}, {standard['credits']} credits) - {standard['grade']}") #Add standard info to list
        update_standards_list() #Initial standards list when module opens

        Button(window, text="Return to Dashboard", command=window.destroy, bg="#00B3FF", fg="white", width=20).pack(pady=20) #Labels the blue button to return to the main dashboard

    def career_planner_module(self): #MODULE 2: Career Planner
        window = Toplevel(self.root)
        window.title("Career Planner")
        window.geometry("500x400")
        window.configure(bg="#E6F0FF")

        Label(window, text="🎯 Career Planner", bg="#E6F0FF", fg="#003366", font=("Arial", 18, "bold")).pack(pady=20) #Labels the module title with icon

        #Creates the three buttons for three functions in Career Planner, and the button to close module and return to main dashboard
        Button(window, text="Add Interest", command=self.add_interest, bg="#00B3FF", fg="white", width=20).pack(pady=10)
        Button(window, text="Add Strength", command=self.add_strength, bg="#00B3FF", fg="white", width=20).pack(pady=10)
        Button(window, text="Suggest Careers", command=self.suggest_careers, bg="#00B3FF", fg="white", width=20).pack(pady=10)
        Button(window, text="Return to Dashboard", command=window.destroy, bg="#00B3FF", fg="white", width=20).pack(pady=20)

    def add_interest(self): #Creates the function to open interest selection window when user clicks Add Interest
        window = tk.Toplevel(self.root)
        window.title("Add Interest - Select Subject")
        window.geometry("800x500")
        window.configure(bg="#E6F0FF")
        
        Label(window, text="Select an NCEA Level 3 Subject", font=("Arial", 16, "bold"), bg="#E6F0FF", fg="#003366").pack(pady=15) #Labels the window title
        
        main_frame = Frame(window, bg="#E6F0FF") #Create main frame for scrollable content
        main_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        #Creates the scroll function of Interests
        canvas = tk.Canvas(main_frame, bg="#E6F0FF")
        scrollbar = tk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = Frame(canvas, bg="#E6F0FF")
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))) #Update scroll region when frame size changes
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set) #Connect canvas to scrollbar
        
        for category_name, subjects in career_categories.items(): #Loop through each subject category
            category_frame = Frame(scrollable_frame, bg="#E6F0FF")
            category_frame.pack(fill="x", pady=8)   
            
            Label(category_frame, text=category_name, bg="#E6F0FF", fg="#00B3FF", font=("Arial", 12, "bold")).pack(anchor="w") #Labels the catagory's name as header
            
            subject_frame = Frame(scrollable_frame, bg="#E6F0FF") #Create frame for subject buttons in this category
            subject_frame.pack(fill="x", pady=5)
            
            col = 0 #Initialize column counter for grid layout
            row = 0 #Initialize row counter for grid layout
            max_cols = 3 #Set maximum of 3 columns
            
            for subject in subjects: #Loop through each subject in current category
                subject_button = Button(subject_frame, text=subject, bg="#00B3FF", fg="white", font=("Arial", 9), width=30, height=1, command=lambda s=subject: self.select_interest(s, window)) #Create button for each subject
                subject_button.grid(row=row, column=col, padx=5, pady=3, sticky="w")
                col += 1 #Move to next column
                if col >= max_cols:
                    col = 0 #Reset to first column
                    row += 1 #Move to next row

        #Position canvas on left side and scrollbar on the right
        canvas.pack(side="left", fill="both", expand=True) 
        scrollbar.pack(side="right", fill="y") 

    def select_interest(self, subject, window): #Creates the function to handle interest selection when user clicks subject button
        if subject not in self.user.interests: #Check if subject is not already in user's interests
            self.user.interests.append(subject)
            messagebox.showinfo("Added", f"Interest '{subject}' successfully added!")
        else: #If subject is already in interests
            messagebox.showinfo("Info", f"'{subject}' is already in your interests.")
        window.destroy() #Close the interest selection window

    def add_strength(self): #Creates the function to open strength selection window when user clicks Add Strength
        window = tk.Toplevel(self.root)
        window.title("Add Strength")
        window.geometry("500x400")
        window.configure(bg="#E6F0FF")
        
        Label(window, text="Select a Strength", font=("Arial", 16, "bold"), bg="#E6F0FF", fg="#003366").pack(pady=15) #Labels the window title for strength selection

        strengths = list(strength_database.keys()) #Get list of all available strengths from database
        mid_point = len(strengths) // 2 #Find midpoint to split strengths into two columns
        columns_frame = Frame(window, bg="#E6F0FF") #Create frame for two columns layout
        columns_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        #Labels the left and right columns
        left_frame = Frame(columns_frame, bg="#E6F0FF")
        left_frame.pack(side="left", fill="both", expand=True)
        right_frame = Frame(columns_frame, bg="#E6F0FF")
        right_frame.pack(side="right", fill="both", expand=True)
        
        for i, strength in enumerate(strengths[:mid_point]): #Loop through first half of strengths
            Button(left_frame, text=strength, bg="#00B3FF", fg="white", width=22, command=lambda s=strength: self.select_strength(s, window)).pack(pady=3) #Create button for each strength in left column
        for i, strength in enumerate(strengths[mid_point:]):
            Button(right_frame, text=strength, bg="#00B3FF", fg="white", width=22, command=lambda s=strength: self.select_strength(s, window)).pack(pady=3)

    def select_strength(self, strength, window): #Creates the function to handle strength selection when user clicks strength button, mostly same as the interests part
        if strength not in self.user.strengths:
            self.user.strengths.append(strength) #Add strength to user's strengths list
            messagebox.showinfo("Added", f"Strength '{strength}' successfully added!")
        else: #If strength is already in strengths
            messagebox.showinfo("Info", f"'{strength}' is already in your strengths.")
        window.destroy() #Close the strength selection window after selection

    def suggest_careers(self): #Creates the function to generate career suggestions based on user's interests and strengths
        if not self.user.interests and not self.user.strengths:
            messagebox.showwarning("Error", "Please add at least one interest or strength first.") #Show error message
            return
        
        suggested_careers = get_suggested_careers(self.user.interests, self.user.strengths) #Get career suggestions from the function in database
        if suggested_careers:
            messagebox.showinfo("Career Suggestions", "Your top three career matches:\n" + "\n".join(suggested_careers))
        else: #If no matching careers found
            messagebox.showinfo("Career Suggestions", "No matching careers found. Try adding more interests or strengths.") #Show message about no matches

    def frost_module(self): #MODULE 3: FROST
        window = Toplevel(self.root) 
        window.title("FROST - Chatbot")
        window.geometry("800x600")
        window.configure(bg="#E6F0FF")

        Label(window, text="🤖 FROST Assistant", bg="#E6F0FF", fg="#003366", font=("Arial", 18, "bold")).pack(pady=10) #Creates and labels the title with robot icon

        #Create frame for chat display with white background
        chat_frame = Frame(window, bg="white")
        chat_frame.pack(padx=20, pady=10, fill="both", expand=True)

        #Create and positions the scrollbar
        scrollbar = Scrollbar(chat_frame)
        scrollbar.pack(side="right", fill="y")

        self.chat_display = Text(chat_frame, yscrollcommand=scrollbar.set, state="disabled", wrap="word", bg="white", fg="black") #Create text widget for chat history
        self.chat_display.pack(fill="both", expand=True)
        scrollbar.config(command=self.chat_display.yview) #Connect scrollbar to chat display

        self.add_to_chat("FROST", "Hello! I'm FROST, your Gradus assistant. How can I help you today?") #Add initial greeting
        
        #Create and positions frame for user input
        input_frame = Frame(window, bg="#E6F0FF")
        input_frame.pack(fill="x", padx=20, pady=10)

        self.user_input = Entry(input_frame, font=("Arial", 12)) #Create text entry for user messages
        self.user_input.pack(side="left", fill="x", expand=True, padx=(0, 10))
        self.user_input.bind("<Return>", lambda e: self.process_frost_input()) #Bind Enter key to send messages

        Button(input_frame, text="Send", command=self.process_frost_input, bg="#00B3FF", fg="white").pack(side="right") #Labels the blue send button for messages
        Button(window, text="Return to Dashboard", command=window.destroy, bg="#00B3FF", fg="white", width=20).pack(pady=10) #Labels the blue button to close module

    def add_to_chat(self, sender, message): #Creates the function to add messages to chat display
        self.chat_display.config(state="normal") #Enable editing
        self.chat_display.insert("end", f"{sender}: {message}\n\n") #Add message with sender name
        self.chat_display.config(state="disabled") #Disable editing
        self.chat_display.see("end") #Scroll to bottom to show the latest messages

    def process_frost_input(self): #Creates the function to process user input and generate FROST responses
        user_text = self.user_input.get().strip().lower() #Get user input and convert to lowercase
        if not user_text:
            return #Ignore empty messages and return
        
        self.add_to_chat("You", user_text) #Add user message to chat display
        self.user_input.delete(0, "end") #Clear input field after sending
        
        response = "I'm not sure how to answer that. Try asking about careers, grades, or NCEA." #Default response when keywords are not captured
        
        for keyword, bot_response in frost_responses.items(): #Loop through keyword responses
            if keyword in user_text:
                response = bot_response #Use response from the database for this keyword
                break

        self.add_to_chat("FROST", response) #Add FROST's response to chat display

    def profile_module(self): #MODULE 4: Profile
        window = Toplevel(self.root)
        window.title("Profile")
        window.geometry("500x700")
        window.configure(bg="#E6F0FF")

        Label(window, text=f"👤 {self.user.username}'s Profile", bg="#E6F0FF", fg="#003366", font=("Arial", 18, "bold")).pack(pady=20) #Labels the profile header with username

        self.create_interests_section(window) #Create interests section in profile. Same as below
        self.create_strengths_section(window)
        self.create_standards_section(window)

        Button(window, text="Return to Dashboard", command=window.destroy, bg="#00B3FF", fg="white", width=20).pack(pady=20) #Creates the blue button to close module

    def create_interests_section(self, parent): #Creates the function to create interests section in profile
        #Creates the frame and positions it
        frame = Frame(parent, bg="#E6F0FF") 
        frame.pack(fill="x", padx=20, pady=10)
        
        Label(frame, text="Your Interests:", bg="#E6F0FF", font=("Arial", 12, "bold")).pack(anchor="w") #Labels the section header for interests
        
        #Create and positions listbox for displaying interests
        interests_list = Listbox(frame, height=4, selectmode=tk.SINGLE) 
        interests_list.pack(fill="x", pady=5) 
        
        for interest in self.user.interests: #Loop through user's interests and add each interest to listbox
            interests_list.insert(tk.END, interest)

        Button(frame, text="Remove Selected Interest", bg="#CC0000", fg="white", command=lambda: self.remove_item(interests_list, self.user.interests, "interest")).pack(pady=5) #Creates and labels the red button to remove selected interest

    def create_strengths_section(self, parent): #Function to create strengths section in profile, basically same as create_interests_section
        #Creates and positions the frame for strengths selection
        frame = Frame(parent, bg="#E6F0FF") 
        frame.pack(fill="x", padx=20, pady=10) 
        
        Label(frame, text="Your Strengths:", bg="#E6F0FF", font=("Arial", 12, "bold")).pack(anchor="w") #Creates the section header for strengths
        
        #Creates and positions listbox for displaying strengths
        strengths_list = Listbox(frame, height=4, selectmode=tk.SINGLE)
        strengths_list.pack(fill="x", pady=5)
        
        for strength in self.user.strengths: #Loop through user's strengths
            strengths_list.insert(tk.END, strength) #Add each strength to listbox

        Button(frame, text="Remove Selected Strength", bg="#CC0000", fg="white", command=lambda: self.remove_item(strengths_list, self.user.strengths, "strength")).pack(pady=5) #Red button to remove selected strength

    def create_standards_section(self, parent): #Create the function to create standards section in profile, basically same as above too
        #Create and positions frame for standards section
        frame = Frame(parent, bg="#E6F0FF")
        frame.pack(fill="x", padx=20, pady=10)
        
        Label(frame, text="Your Standards:", bg="#E6F0FF", font=("Arial", 12, "bold")).pack(anchor="w") #Creates the section header for standards

        #Create and positions listbox for displaying standards
        standards_list = Listbox(frame, height=4, selectmode=tk.SINGLE)
        standards_list.pack(fill="x", pady=5)
        
        for standard in self.user.standards: #Loop through user's standards
            standards_list.insert(tk.END, f"{standard['name']} (Level {standard['level']}, {standard['credits']} credits) - {standard['grade']}") #Add formatted standard info to listbox

        Button(frame, text="Remove Selected Standard", bg="#CC0000", fg="white", command=lambda: self.remove_standard(standards_list)).pack(pady=5) #Creates and labels red button to remove selected standard

    def remove_item(self, listbox, data_list, item_type): #Creates the function to remove items from interests or strengths lists
        selection = listbox.curselection() #Get index of selected item in listbox
        if not selection: #If no item is selected
            messagebox.showinfo("Info", f"No {item_type} selected to remove.") #Show info message
            return
        
        selected = listbox.get(selection) #Get text of selected item
        data_list.remove(selected) #Remove item from database (interests or strengths)
        listbox.delete(selection) #Remove item from listbox display
        messagebox.showinfo("Removed", f"{item_type.title()} '{selected}' successfully removed!")

    def remove_standard(self, listbox): #Creates the function to remove standards
        selection = listbox.curselection() #Get index of selected standard in listbox
        if not selection: #If no standard is selected
            messagebox.showinfo("Info", "No standard selected to remove.")
            return
        
        selected_index = selection[0] #Get the index of selected standard
        removed_standard = self.user.standards.pop(selected_index) #Remove standard from standards list
        listbox.delete(selection) #Remove standard from listbox display
        messagebox.showinfo("Removed", f"Standard '{removed_standard['name']}' successfully removed!")

#Main Program
if __name__ == "__main__":
    root = tk.Tk() #Create main Tkinter window
    app = GradusApp(root) #Create Gradus application
    root.mainloop() #Start the Tkinter event loop