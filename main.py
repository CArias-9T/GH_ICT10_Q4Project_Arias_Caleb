from pyscript import display, document
import numpy as np
import logging
logging.getLogger('matplotlib').setLevel(logging.ERROR)
import matplotlib.pyplot as plt

plt.figure()
plt.plot([0, 1],[0, 1])
plt.close()

class Classmate:
    def __init__(self, name, section, favorite_subject):
        self.name = name
        self.section = section
        self.favorite_subject = favorite_subject

classmate_list = [
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
    Classmate('Miguel Sanchez', '10-Topaz', 'ICT')
]

def show_classmates(e):
    document.getElementById('listoutput').innerHTML = ''

    name = document.getElementById('input1').value
    section = document.getElementById('input2').value
    subject = document.getElementById('input3').value

    if name:
        classmate_list.append(Classmate(name, section, subject))

    for c in classmate_list:
        display(
            f"Hi! I am {c.name} from {c.section}. My favorite subject is {c.favorite_subject}.",
            target="listoutput"
        )


def graph(e):
    document.getElementById('output').innerHTML = ''

    try:
        absence = int(document.getElementById('absence').value)
    except:
        return

    month = document.getElementById('monthselect').value

    plt.clf()
    plt.bar([month], [absence])
    plt.title("Topaz Absences Per Month")
    plt.xlabel("Months")
    plt.ylabel("Absences")
    plt.show()


def show_imgs(e):
    carousel = document.getElementById("carouselExampleIndicators")
    
    if carousel.style.display == "none":
        carousel.style.display = "block"
    else:
        carousel.style.display = "none"
