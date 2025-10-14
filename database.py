#User accounts database that stores username and password combinations for authentication
accounts = {
    "ADMIN": "2025",
    "1": "1" #Test account with simple credentials for demonstration purposes
}

#Career database
career_categories = {
    "Language": [ #Subjects related to languages
        "English", 
        "Language Studies" 
    ],
    "Health and Physical Education": [ #Subjects related to health, wellness, and physical activity
        "Health Education", 
        "Outdoor Education", 
        "Physical Education" 
    ],
    "Mathematics and Statistics": [ #Subjects focused on mathematical concepts and data analysis
        "Calculus", 
        "Statistics and Probability" 
    ],
    "Sciences": [ #Scientific subjects exploring natural phenomena and principles
        "Biology",
        "Chemistry", 
        "Physics" 
    ],
    "Social Sciences": [ #Subjects examining human society and social relationships
        "Accounting", 
        "Business Studies", 
        "Economics", 
        "Geography", 
        "History", 
        "Psychology" 
    ],
    "Technology": [ #Subjects focused on technological applications and design
        "Design and Visual Communication", 
        "Digital Technology", 
        "Fashion and Design Technology", 
        "Food Technology", 
        "Multi Materials Technology" 
    ],
    "Visual and Performing Arts": [ #Creative subjects involving artistic expression
        "Art and Painting", 
        "Dance", 
        "Design", 
        "Drama", 
        "Music Studies", 
        "Photography" 
    ]
}

#Career database for backward compatibility with existing career suggestion functions
career_database = {} #Initialize empty dictionary
for category, subjects in career_categories.items(): #Loop through each category and its subjects
    for subject in subjects: #Loop through each subject in current category
        if subject == "English":
            career_database[subject] = ["Journalism", "Public Relations", "Teaching", "Editing", "Law"] #Communication and language-based careers
        elif subject == "Language Studies":
            career_database[subject] = ["Translator", "Interpreter", "Diplomat", "Tourism Consultant", "International Relations Specialist"] #Language and international careers
        elif subject == "Health Education":
            career_database[subject] = ["Nursing", "Public Health Advisor", "Physiotherapy", "Health Promotion Specialist"] #Healthcare and wellness careers
        elif subject == "Outdoor Education":
            career_database[subject] = ["Outdoor Instructor", "Park Ranger", "Adventure Tourism Guide", "Physical Education Teacher"] #Outdoor and recreation careers
        elif subject == "Physical Education":
            career_database[subject] = ["Sports Coach", "Physiotherapist", "Exercise Scientist", "PE Teacher", "Sports Management"] #Sports and fitness careers
        elif subject == "Calculus":
            career_database[subject] = ["Engineering", "Mathematician", "Data Analyst", "Software Developer"] #Math-intensive technical careers
        elif subject == "Statistics and Probability":
            career_database[subject] = ["Statistician", "Data Scientist", "Economist", "Financial Analyst"] #Data analysis and statistics careers
        elif subject == "Biology":
            career_database[subject] = ["Doctor", "Biotechnologist", "Environmental Scientist", "Research Scientist"] #Biological and medical sciences careers
        elif subject == "Chemistry":
            career_database[subject] = ["Pharmacist", "Chemical Engineer", "Forensic Scientist", "Materials Scientist"] #Chemistry and materials science careers
        elif subject == "Physics":
            career_database[subject] = ["Engineer", "Astronomer", "Aerospace Engineer", "Data Scientist"] #Physics and engineering careers
        elif subject == "Accounting":
            career_database[subject] = ["Accountant", "Auditor", "Financial Analyst", "Tax Consultant"] #Accounting and finance careers
        elif subject == "Business Studies":
            career_database[subject] = ["Business Analyst", "Entrepreneur", "Marketing Manager", "Human Resources Officer"] #Business and management careers
        elif subject == "Economics":
            career_database[subject] = ["Economist", "Financial Planner", "Policy Analyst", "Investment Banker"] #Economics and finance careers
        elif subject == "Geography":
            career_database[subject] = ["Urban Planner", "Environmental Consultant", "Geospatial Analyst", "Climatologist"] #Geography and environmental careers
        elif subject == "History":
            career_database[subject] = ["Historian", "Archivist", "Museum Curator", "Teacher"] #History and education careers
        elif subject == "Psychology":
            career_database[subject] = ["Psychologist", "Counsellor", "Human Resources Specialist", "Social Worker"] #Psychology and human services careers
        elif subject == "Design and Visual Communication":
            career_database[subject] = ["Graphic Designer", "Architect", "Product Designer", "UX/UI Designer"] #Design and visual arts careers
        elif subject == "Digital Technology":
            career_database[subject] = ["Software Developer", "Web Designer", "Cybersecurity Analyst", "IT Consultant"] #Technology and computing careers
        elif subject == "Fashion and Design Technology":
            career_database[subject] = ["Fashion Designer", "Textile Technologist", "Stylist", "Fashion Marketing Specialist"] #Fashion and design careers
        elif subject == "Food Technology":
            career_database[subject] = ["Food Scientist", "Nutritionist", "Quality Assurance Officer", "Product Developer"] #Food science and nutrition careers
        elif subject == "Multi Materials Technology":
            career_database[subject] = ["Mechanical Engineer", "Product Designer", "Construction Manager", "Technician"] #Engineering and manufacturing careers
        elif subject == "Art and Painting":
            career_database[subject] = ["Artist", "Art Teacher", "Gallery Curator", "Illustrator"] #Fine arts and creative careers
        elif subject == "Dance":
            career_database[subject] = ["Professional Dancer", "Choreographer", "Dance Instructor", "Fitness Trainer"] #Dance and performance careers
        elif subject == "Design":
            career_database[subject] = ["Graphic Designer", "Interior Designer", "Architect", "Creative Director"] #Design and architecture careers
        elif subject == "Drama":
            career_database[subject] = ["Actor", "Theatre Director", "Drama Teacher", "Scriptwriter"] #Theatre and performance careers
        elif subject == "Music Studies":
            career_database[subject] = ["Musician", "Music Producer", "Composer", "Music Teacher"] #Music and audio careers
        elif subject == "Photography":
            career_database[subject] = ["Photographer", "Photojournalist", "Graphic Designer", "Content Creator"] #Photography and media careers
        else:
            career_database[subject] = ["Various Careers"] #Any unassigned subjects

#Strength database
strength_database = {
    "Problem Solving": ["Engineer", "Software Developer", "Data Scientist", "Research Scientist", "Statistician"], #Analytical and technical careers
    "Creativity": ["Graphic Designer", "Fashion Designer", "Architect", "Artist", "Product Designer"], #Creative and design-focused careers
    "Communication": ["Teacher", "Journalist", "Public Relations Officer", "Counsellor", "Marketing Manager"], #Communication and people-oriented careers
    "Teamwork": ["Sports Coach", "Project Manager", "Engineer", "Teacher", "Healthcare Worker"], #Collaborative and team-based careers
    "Leadership": ["Manager", "Entrepreneur", "Team Leader", "Coach", "Marketing Director"], #Leadership and management careers
    "Critical Thinking": ["Economist", "Policy Analyst", "Lawyer", "Research Scientist", "Engineer"], #Analytical and reasoning-based careers
    "Attention to Details": ["Accountant", "Pharmacist", "Forensic Scientist", "Software Tester", "Quality Assurance Officer"], #Precision and detail-oriented careers
    "Adaptability": ["Consultant", "Tourism Manager", "IT Specialist", "Marketing Strategist"], #Flexible and dynamic careers
    "Empathy": ["Counsellor", "Social Worker", "Nurse", "Psychologist", "Teacher"], #Caring and supportive careers
    "Organization": ["Event Planner", "Business Analyst", "Project Manager", "Administrator"], #Structured and planning-based careers
    "Analytical Thinking": ["Data Scientist", "Financial Analyst", "Engineer", "Statistician", "Research Scientist"], #Data and analysis careers
    "Innovation": ["Entrepreneur", "Software Developer", "Product Designer", "Engineer"], #Innovative and inventive careers
    "Technical Skills": ["Software Developer", "Cybersecurity Analyst", "IT Technician", "Engineer"], #Technical and specialized careers
    "Resilience": ["Healthcare Worker", "Police Officer", "Teacher", "Paramedic"], #High stress and demanding careers
    "Time Management": ["Accountant", "Engineer", "Project Manager", "Research Scientist"], #Efficiency and deadline-oriented careers
    "Collaboration": ["Teacher", "Software Developer", "Healthcare Worker", "Research Scientist"], #Team-based and cooperative careers
    "Patience": ["Teacher", "Therapist", "Research Scientist", "Healthcare Worker"], #Patient and methodical careers
    "Leadership and Motivation": ["Coach", "Entrepreneur", "Project Leader", "Manager"], #Motivational and guidance careers
    "Logical Reasoning": ["Engineer", "Mathematician", "Programmer", "Data Analyst"], #Logic and reasoning based careers
    "Artistic Vision": ["Artist", "Fashion Designer", "Architect", "Graphic Designer"] #Creative and aesthetic careers
}

#FROST chatbot responses
frost_responses = {
    #Greetings and basic interactions
    "hello": "Hello! I'm FROST, your Gradus assistant. I can help you with career advice, NCEA questions, and more!",
    "hi": "Hi there! How can I assist you with your career planning today?",
    "hey": "Hey! I'm FROST, ready to help you with your academic and career journey!",
    "good morning": "Good morning! Ready to make progress on your goals today?",
    "good afternoon": "Good afternoon! How can I help you with Gradus?",
    "good evening": "Good evening! I'm here to help with any questions you have.",
    
    #App functionality questions
    "what can you do": "I can help you with: career suggestions based on your interests, NCEA information, grade tracking explanations, and general academic guidance. What would you like to know?",
    "how does this work": "Gradus has four main modules: Grade Tracker for NCEA standards, Career Planner for career exploration, FROST (that's me!) for questions, and Profile to manage your data.",
    "help": "I can help with: career advice, NCEA information, grade tracking, and general guidance. What would you like to know?",
    "what is gradus": "Gradus is your career and academic planner! It helps you track NCEA progress, explore career options, and get personalized guidance for your future.",
    
    #NCEA detailed information
    "ncea": "NCEA (National Certificate of Educational Achievement) is New Zealand's main secondary school qualification. It has three levels over Years 11-13.",
    "level 1": "NCEA Level 1 is usually taken in Year 11. Students typically take 5-6 subjects and need 80 credits to achieve Level 1.",
    "level 2": "NCEA Level 2 is usually taken in Year 12. You need 80 credits total, with 60 at Level 2 or above.", 
    "level 3": "NCEA Level 3 is usually taken in Year 13. You need 80 credits total, with 60 at Level 3 or above and 20 from Level 2 or above.",
    "credits": "NCEA credits are earned when you achieve standards. Most standards are worth 3-5 credits. You need 80 credits to achieve each NCEA level.",
    "how many credits": "You need 80 credits to achieve each NCEA level. For Level 2, 60 must be at Level 2 or above; for Level 3, 60 must be at Level 3 or above.",
    "standard": "Standards are the individual assessments in NCEA. They can be internal (assessed in school) or external (exams).",
    "achieved": "Achieved is the passing grade for NCEA standards. It gives you 2 points per credit for Rank Score calculations.",
    "merit": "Merit is the second-highest grade in NCEA. It gives you 3 points per credit for Rank Score calculations.",
    "excellence": "Excellence is the highest grade in NCEA. It gives you 4 points per credit for Rank Score calculations.",
    "endorsement": "Course Endorsement: 14+ credits at Merit/Excellence in one subject. Certificate Endorsement: 50+ credits at Merit/Excellence across your subjects.",
    "literacy": "Literacy requirements: 10 credits from specific English or Te Reo Māori standards, plus 5 credits in reading and 5 in writing.",
    "numeracy": "Numeracy requirements: 10 credits from specific mathematics standards.",
    "university entrance": "For university entrance, you generally need NCEA Level 3 with 14 credits in three approved subjects, plus literacy and numeracy requirements.",
    
    #Rank score information
    "rank score": "Rank Score is used for university entrance. It's calculated from your best 80 credits at Level 3, with Excellence=4, Merit=3, Achieved=2 points per credit. Maximum is 320.",
    "calculate rank score": "Rank Score uses your best 80 Level 3 credits: Excellence=4pts/credit, Merit=3pts/credit, Achieved=2pts/credit. Not Achieved=0. The Grade Tracker module can calculate this for you!",
    "maximum rank score": "The maximum Rank Score is 320 points (80 credits × 4 points each for Excellence).",
    
    #Career guidance
    "career": "I can help you explore careers based on your interests and strengths. Try adding some interests in the Career Planner module!",
    "what career": "I can suggest careers based on your interests and strengths. Go to the Career Planner module to add your interests and get personalized suggestions!",
    "job": "I can help you explore different career paths. What subjects are you interested in? You can add them in the Career Planner module.",
    "future": "Thinking about your future? That's great! I can help you explore career options that match your interests and strengths.",
    "subject": "Your NCEA subjects can lead to many career paths. Add your favorite subjects as interests in the Career Planner to see related careers!",
    "interest": "Your interests are great indicators of potential careers. Add them in the Career Planner module to get personalized career suggestions!",
    "strength": "Your strengths can help determine which careers you might excel in. Add them in the Career Planner module for better career matches!",
    
    #Grade tracker specific
    "grade": "The Grade Tracker module helps you record NCEA standards, track your credits, and calculate your Rank Score. You can add standards with their levels, credits, and grades.",
    "track": "The Grade Tracker lets you monitor your NCEA progress. You can add standards you've completed and see how close you are to your goals.",
    "progress": "Check your academic progress in the Grade Tracker module. It shows all your standards and can calculate your current Rank Score.",

    # Encouragement and motivation
    "stressed": "It's normal to feel stressed about your future. Take it one step at a time! Focus on your interests and strengths - they'll guide you toward suitable career paths.",
    "worried": "Don't worry - exploring careers is about discovering possibilities, not making final decisions. Try adding different interests to see what careers might suit you!",
    "confused": "Feeling confused about your options is completely normal! Start by adding subjects you enjoy in the Career Planner - I'll help you see what careers might fit.",
    "motivation": "Remember: every step you take in exploring careers brings you closer to finding your path. You're doing great by using Gradus to plan your future!",
    
    # Appreciation and farewell
    "thank": "You're welcome! Feel free to ask if you have any other questions.",
    "thanks": "You're welcome! I'm here whenever you need help with your career or academic planning.",
    "bye": "Goodbye! Remember to check your Grade Tracker regularly and update your career interests!",
    "goodbye": "Goodbye! Come back anytime you have questions about your career path or NCEA progress.",
    "see you": "See you later! Don't hesitate to ask if you need any help with your academic planning.",
    
    # Default fallback responses
    "": "I'm not sure I understand. Try asking about careers, NCEA, grades, or how to use Gradus!",
    "default": "I'm here to help with career planning and NCEA questions. Try asking about specific subjects, careers, or how to use the different modules in Gradus!"
}

def get_suggested_careers(interests, strengths): #Create the function to generate career suggestions based on user's interests and strengths
    career_scores = {}
    #Add points for careers related to user's interests
    for interest in interests: #Loop through each user interest
        if interest in career_database: 
            for career in career_database[interest]: #Loop through careers associated with this interest
                career_scores[career] = career_scores.get(career, 0) + 1 
    #Add points for careers related to user's strengths  
    for strength in strengths: #Loop through each user strength
        if strength in strength_database: 
            for career in strength_database[strength]: #Loop through careers associated with this strength
                career_scores[career] = career_scores.get(career, 0) + 1 
    #Sort careers by score in descending order and return top 3
    sorted_careers = sorted(career_scores.items(), key=lambda x: x[1], reverse=True) #Sort careers by score (highest first)
    return [career for career, _ in sorted_careers[:3]] #Return only the career names from top 3 scored careers

def get_suggested_careers(interests, strengths): #Create the function to generate career suggestions based on user's interests and strengths
    career_scores = {}
    #Add points for careers related to user's interests
    for interest in interests: #Loop through each user interest
        if interest in career_database: 
            for career in career_database[interest]: #Loop through careers associated with this interest
                career_scores[career] = career_scores.get(career, 0) + 1 
    #Add points for careers related to user's strengths  
    for strength in strengths: #Loop through each user strength
        if strength in strength_database: 
            for career in strength_database[strength]: #Loop through careers associated with this strength
                career_scores[career] = career_scores.get(career, 0) + 1 
    #Sort careers by score in descending order and return top 3
    sorted_careers = sorted(career_scores.items(), key=lambda x: x[1], reverse=True) #Sort careers by score (highest first)
    return [career for career, _ in sorted_careers[:3]] #Return only the career names from top 3 scored careers