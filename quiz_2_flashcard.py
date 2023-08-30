import re
import csv

# Read the content of the uploaded file
with open('Quiz1.txt', 'r') as file:
    content = file.read()

# Parsing logic
questions_raw = re.split(r"UnansweredQuestion \d+", content)
questions_raw = [q.strip() for q in questions_raw if q.strip()]
questions_answers = []

for q in questions_raw:
    lines = q.split("\n")
    question = lines[0].strip()
    correct_answer_index = lines.index("Correct Answer")
    options = lines[1:correct_answer_index]
    correct_answer = lines[correct_answer_index + 1].strip()
    
    questions_answers.append({
        "question": question,
        "options": options,
        "correct_answer": correct_answer
    })

for entry in questions_answers:
    if entry['question'] == '0 / 1 pts':
        entry['question'] = entry['options'][0]
        entry['options'] = entry['options'][1:]

# Path to save the CSV file
csv_path = r'.../quiz1_flashcards.csv"

# Writing the extracted questions and answers to the CSV
with open(csv_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    
    # Writing the header
    writer.writerow(["Term", "Definition"])
    
    # Writing the questions and answers
    for qa in questions_answers:
        writer.writerow([qa["question"], qa["correct_answer"]])

print(f"Flashcards saved to: {csv_path}")
