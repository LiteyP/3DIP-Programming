accounts = { #Database for user information
    "ADMIN": "2025",
    "1": "1"
}

career_database = { #Database for career suggestions related with interests and strengths
    "English": ["Journalism", "Public Relations", "Teaching", "Editing", "Law"],
    "Health Education": ["Nursing", "Public Health Advisor", "Physiotherapy", "Health Promotion Specialist"],
    "Outdoor Education": ["Outdoor Instructor", "Park Ranger", "Adventure Tourism Guide", "Physical Education Teacher"],
    "Physical Education": ["Sports Coach", "Physiotherapist", "Exercise Scientist", "PE Teacher", "Sports Management"],
    "Language Studies": ["Translator", "Interpreter", "Diplomat", "Tourism Consultant", "International Relations Specialist"],
    "Calculus": ["Engineering", "Mathematician", "Data Analyst", "Software Developer"],
    "Statistics and Probability": ["Statistician", "Data Scientist", "Economist", "Financial Analyst"],
    "Biology": ["Doctor", "Biotechnologist", "Environmental Scientist", "Research Scientist"],
    "Chemistry": ["Pharmacist", "Chemical Engineer", "Forensic Scientist", "Materials Scientist"],
    "Physics": ["Engineer", "Astronomer", "Aerospace Engineer", "Data Scientist"],
    "Accounting": ["Accountant", "Auditor", "Financial Analyst", "Tax Consultant"],
    "Business Studies": ["Business Analyst", "Entrepreneur", "Marketing Manager", "Human Resources Officer"],
    "Economics": ["Economist", "Financial Planner", "Policy Analyst", "Investment Banker"],
    "Geography": ["Urban Planner", "Environmental Consultant", "Geospatial Analyst", "Climatologist"],
    "History": ["Historian", "Archivist", "Museum Curator", "Teacher"],
    "Psychology": ["Psychologist", "Counsellor", "Human Resources Specialist", "Social Worker"],
    "Design and Visual Communication": ["Graphic Designer", "Architect", "Product Designer", "UX/UI Designer"],
    "Digital Technology": ["Software Developer", "Web Designer", "Cybersecurity Analyst", "IT Consultant"],
    "Fashion and Design Technology": ["Fashion Designer", "Textile Technologist", "Stylist", "Fashion Marketing Specialist"],
    "Food Technology": ["Food Scientist", "Nutritionist", "Quality Assurance Officer", "Product Developer"],
    "Multi Materials Technology": ["Mechanical Engineer", "Product Designer", "Construction Manager", "Technician"],
    "Art and Painting": ["Artist", "Art Teacher", "Gallery Curator", "Illustrator"],
    "Dance": ["Professional Dancer", "Choreographer", "Dance Instructor", "Fitness Trainer"],
    "Design": ["Graphic Designer", "Interior Designer", "Architect", "Creative Director"],
    "Drama": ["Actor", "Theatre Director", "Drama Teacher", "Scriptwriter"],
    "Music Studies": ["Musician", "Music Producer", "Composer", "Music Teacher"],
    "Photography": ["Photographer", "Photojournalist", "Graphic Designer", "Content Creator"]
}

strength_database = {
    "Problem Solving": ["Engineer", "Software Developer", "Data Scientist", "Research Scientist", "Statistician"],
    "Creativity": ["Graphic Designer", "Fashion Designer", "Architect", "Artist", "Product Designer"],
    "Communication": ["Teacher", "Journalist", "Public Relations Officer", "Counsellor", "Marketing Manager"],
    "Teamwork": ["Sports Coach", "Project Manager", "Engineer", "Teacher", "Healthcare Worker"],
    "Leadership": ["Manager", "Entrepreneur", "Team Leader", "Coach", "Marketing Director"],
    "Critical Thinking": ["Economist", "Policy Analyst", "Lawyer", "Research Scientist", "Engineer"],
    "Attention to Details": ["Accountant", "Pharmacist", "Forensic Scientist", "Software Tester", "Quality Assurance Officer"],
    "Adaptability": ["Consultant", "Tourism Manager", "IT Specialist", "Marketing Strategist"],
    "Empathy": ["Counsellor", "Social Worker", "Nurse", "Psychologist", "Teacher"],
    "Organization": ["Event Planner", "Business Analyst", "Project Manager", "Administrator"],
    "Analytical Thinking": ["Data Scientist", "Financial Analyst", "Engineer", "Statistician", "Research Scientist"],
    "Innovation": ["Entrepreneur", "Software Developer", "Product Designer", "Engineer"],
    "Technical Skills": ["Software Developer", "Cybersecurity Analyst", "IT Technician", "Engineer"],
    "Resilience": ["Healthcare Worker", "Police Officer", "Teacher", "Paramedic"],
    "Time Management": ["Accountant", "Engineer", "Project Manager", "Research Scientist"],
    "Collaboration": ["Teacher", "Software Developer", "Healthcare Worker", "Research Scientist"],
    "Patience": ["Teacher", "Therapist", "Research Scientist", "Healthcare Worker"],
    "Leadership and Motivation": ["Coach", "Entrepreneur", "Project Leader", "Manager"],
    "Logical Reasoning": ["Engineer", "Mathematician", "Programmer", "Data Analyst"],
    "Artistic Vision": ["Artist", "Fashion Designer", "Architect", "Graphic Designer"]
}

def get_suggested_careers(interests, strengths): #Create the function for getting top three related careers from interests and strengths
    career_scores = {}
    for interest in interests:
        if interest in career_database:
            for career in career_database[interest]:
                career_scores[career] = career_scores.get(career, 0) + 1
    for strength in strengths:
        if strength in strength_database:
            for career in strength_database[strength]:
                career_scores[career] = career_scores.get(career, 0) + 1 
                #If in interest or strength, +1 on the score for that career
    sorted_careers = sorted(career_scores.items(), key=lambda x: x[1], reverse=True) #Sort them by score and list the top three
    return [career for career, _ in sorted_careers[:3]]