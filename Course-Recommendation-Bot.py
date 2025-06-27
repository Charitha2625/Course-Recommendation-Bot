import tkinter as tk
from tkinter import scrolledtext

# Static course catalog
course_catalog = {
    "programming": ["Python for Beginners", "Advanced JavaScript"],
    "data science": ["Introduction to Data Science", "Machine Learning 101"],
    "web development": ["HTML & CSS Basics", "React Fundamentals"]
}

# Function to get recommendations
def get_recommendations(interests):
    interests = interests.lower()
    recommendations = []
    for category in course_catalog:
        if category in interests:
            recommendations.extend(course_catalog[category])
    return recommendations if recommendations else ["No specific courses found. Try 'programming', 'data science', or 'web development'."]

# Function to handle user input
def send_message():
    input_text = user_input.get().strip()
    if input_text:
        add_message(f"You: {input_text}")
        recommendations = get_recommendations(input_text)
        add_message("Bot: Recommended courses: " + ", ".join(recommendations))
        user_input.delete(0, tk.END)

# Function to add messages to chatbox
def add_message(message):
    chatbox.configure(state='normal')
    chatbox.insert(tk.END, message + '\n')
    chatbox.configure(state='disabled')
    chatbox.yview(tk.END)

# Create main window
root = tk.Tk()
root.title("Course Recommendation Bot")

# Chatbox
chatbox = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20, state='disabled', font=("Arial", 10))
chatbox.pack(padx=10, pady=10)

# Input field
user_input = tk.Entry(root, width=50, font=("Arial", 10))
user_input.pack(side=tk.LEFT, padx=10, pady=5)

# Send button
send_button = tk.Button(root, text="Send", command=send_message, font=("Arial", 10))
send_button.pack(side=tk.LEFT, padx=5)

# Bind Enter key to send
root.bind('<Return>', lambda event: send_message())

# Welcome message
add_message("Bot: Hi! Tell me your interests or background to get course recommendations.")

# Run the app
root.mainloop()

