class pup:
    def __init__(self, name, surname, mark):
        self.name = name
        self.surame = surname
        self.mark = mark

    def pritn(self):
        print()

pupils = []

def printp(pupils):
    for pupil in pupils:
        print(pupil.name, pupil.surname, "-", pupil.mark)
    print("\n")

def printb(pupils):
    for pupil in pupils:
        if pupil.mark == "5":
            print(pupil.name, pupil.surname)
    print("\n")

def printa(pupils):
    average = 0
    for pupil in pupils:
        average+=pupil.mark
    res = average / len(pupils)
    print("Average -", res)

with open("pupils.txt", "r", encoding="utf-8") as file:
    for line in file:
        data = line.split(" ")
        pupil = pup(data[0], data[1], int(data[2]))
        pupils.append(pupil)

printb(pupils)
printa(pupils)