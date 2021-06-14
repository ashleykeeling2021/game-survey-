import itertools
from tkinter import *

from matplotlib import pyplot

import graphs

answers = []

window = Tk(className='Market Research')
window.geometry("400x750")

def question(question):
     
    questionTitle = Label(text = question)
    questionTitle.pack()

    topic = StringVar()

    entry = Entry(window, textvariable=topic)
    entry.pack()
    
    answers.append(topic)
    
def radioButtonQuestion(question, options):
    questionTitle = Label(text = question)
    questionTitle.pack()

    topic = StringVar()   

    index = 0
    while index < len(options):
        button=Radiobutton(window, text = options[index], variable=topic, value = options[index])
        button.pack()
        index += 1

    # adds the index of the option choson to the topic values list

    answers.append(topic)
    

def saveValues():
    txtFile = open("database.txt", "a+")

    index = 0
    while index < len(answers):
        txtFile.write(answers[index].get())
        
        if index <= len(answers)-1:
            txtFile.write(",")
        index += 1

    txtFile.write("\n")
    txtFile.close()

    window.destroy()

    displayGraphs()

# asks questions

question("whats your age?")

#asks radioButton questions
genresOptions = ["RPG", "Shooters", "Platformers", "Adventure", "Multiplayer", "Horror", "Other"]
radioButtonQuestion("what is your favourite Genre?", genresOptions)
radioButtonQuestion("what is your least favourite Genre?", genresOptions)

genderOptions = ["Male", "Female", "Other"]
radioButtonQuestion("whats your gender?", genderOptions)

platformOptions = ["Xbox", "PC", "Playstation", "Nintedo", "Saga"]
radioButtonQuestion("what is your favourite platform?", platformOptions)

submit = Button(window, text="Submit", command=saveValues)
submit.pack()

# creates graphs

def displayGraphs():

    window = Tk(className='thing')
    window.geometry("400x500")

    Button(window, text="Gender Pie Chart", command=graphs.pieChart).pack()
##    Button(window, text="Favourite Platformers", command=graphs.pieChart).pack()

window.mainloop()



