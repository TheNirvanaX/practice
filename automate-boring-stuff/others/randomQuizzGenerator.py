# randomQuizzGenerator -  creates quizzes with questions and answers 
# in random order, alomg with the answer key.
#  
import random

# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 
    'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver', 
    'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 
    'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 
    'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 
    'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 
    'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 
    'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 
    'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 
    'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 
    'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 
    'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 
    'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 
    'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 
    'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 
    'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 
    'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# file path
import os

try:
    os.makedirs("F:\\programming\\code\\quiz")
except:
    pass
os.chdir("F:\\programming\\code\\quiz")
# Genertae 35 random quiz files.
for quizNum in range(35):

    # create quiz and answer files.
    quizfile=open(f'quiz_question{quizNum+1}.txt',"w")
    quizAns=open(f'quiz_answer{quizNum+1}.txt',"w")

    # write header for quiz.
    quizfile.write("Name:\n\nDate:\n\nPeriod:\n\n")
    quizfile.write(" "*20+f"State Capitals Quiz {quizNum+1}")
    quizfile.write("\n\n")

    # Shuffle the order of the states.
    states=list(capitals.keys())
    random.shuffle(states)

    # making 50 questions for each quiz.
    for num,question in enumerate(states):
        num+=1
        quizfile.write(f"{num}. What is the capital of {question}?\n")    # write question
        quizAns.write(f"{num}. {capitals[question]}\n")                   # write answer in Solution file.
        # create options
        options = [capitals[question],]
        for choice in list(capitals.values()):
            if choice in options:
                continue
            options.append(choice)
            if len(options)==4:
                break
        random.shuffle(options)
        quizfile.write(f"  A.{options[0]}\n")
        quizfile.write(f"  B.{options[1]}\n")
        quizfile.write(f"  C.{options[2]}\n")
        quizfile.write(f"  D.{options[3]}\n\n")
    
    quizfile.close()
    quizAns.close()
print("quiz sucessfully created!")