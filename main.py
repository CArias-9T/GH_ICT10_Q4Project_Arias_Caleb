from pyscript import display, document
import numpy as np
import logging
logging.getLogger('matplotlib').setLevel(logging.ERROR)
import matplotlib.pyplot as plt

plt.figure()
plt.plot([0, 1],[0, 1])
plt.close()


class Classmate: # class for all attributes
    def __init__(self, name, section, favorite_subject):
        self.name = name
        self.section = section
        self.favorite_subject = favorite_subject

classmate_list = [ # global list, has initially added classmates in it
    Classmate('Jalainie Abdullah', '10-Topaz', 'English'), 
    Classmate('Leona Abeleda', '10-Topaz', 'Filipino'),
    Classmate('Renzo Arce', '10-Topaz', 'CAT'),
    Classmate('Caleb Arias', '10-Topaz', 'Science'),
    Classmate('Cedric Bonzon', '10-Topaz', ''),
    Classmate('Martina Cajucom', '10-Topaz', 'Science'),
    Classmate('Pheobe Catimbang', '10-Topaz', 'Math'),
    Classmate('Sang-heon Choi', '10-Topaz', 'English'),
    Classmate('Sean Cotioco', '10-Topaz', 'Math'),
    Classmate('Allen Daradal', '10-Topaz', 'Math'),
    Classmate('Alejandro Enriquez', '10-Topaz', 'Math'),
    Classmate('Skyler Escobar', '10-Topaz', 'Math'),
    Classmate('Khloe Espina', '10-Topaz', 'Math'),
    Classmate('Prince Gano', '10-Topaz', 'Filipino'),
    Classmate('Calvin Garcia', '10-Topaz', 'TLE'),
    Classmate('Simrandip Kaur', '10-Topaz', 'Math'),
    Classmate('Miguel Sanchez', '10-Topaz', 'ICT'),

]


def show_classmates(e): # function for adding students and displaying

    document.getElementById('listoutput').innerHTML = ''

    name = document.getElementById('input1').value
    section = document.getElementById('input2').value
    favorite_subject = document.getElementById('input3').value

    classmate = Classmate(name, section, favorite_subject) # adding student section
    classmate_list.append(classmate)
    


    for classmate in classmate_list: # display loop
        display(f"Hi! I am {classmate.name} from {classmate.section}. My favorite subject is {classmate.favorite_subject}.", target="listoutput")

def graph(e):
    document.getElementById('output').innerHTML = ' ' # resets value

    absences = np.array([ # input absences
        int(document.getElementById('absence').value)
])
    months = np.array([ # input months
        str(document.getElementById('monthselect').value)
])

    topaz_absences_graph = plt.bar(months, absences) # display graph
    plt.show(topaz_absences_graph)
    plt.title("Topaz's Absence's Per Month")
    plt.xlabel("Months")
    plt.ylabel("Absences")
    
 