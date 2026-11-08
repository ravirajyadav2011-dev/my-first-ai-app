# ========================================================
# MY FIRST AI QUIZ MAKER
# Built by a 14-year-old student in India
# ========================================================

import os

# 1. Ask the user for a topic
topic = input("Enter the topic you want a summary and quiz for: ")
print(f"\nCreating a precise summary and 5-question quiz for '{topic}'...")

# 2. Craft instructions for the AI
system_instructions = (
    f"Act as a precise academic tutor. For the topic '{topic}', provide two things:\n"
    "1. A bulleted, exact, and highly precise summary of the core facts (maximum 5 bullet points).\n"
    "2. A 5-question multiple-choice quiz based strictly on that summary, complete with options A, B, C, D."
)

# 3. Display a simulated placeholder output so the file structure is correct
print("\n========================= RESULTS =========================")
print(f"Summary of {topic}:")
print(f"- Fact 1 about {topic}")
print(f"- Fact 2 about {topic}")
print("\nQuiz Questions:")
print("1. What is the main component of this topic?\n   A) Option 1  B) Option 2")
