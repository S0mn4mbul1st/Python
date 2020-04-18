class Soldier:

    health = 100
    attach_power = 50

    def taken_damage(self):
        self.health -= 1

    def isAlive(self):

        if(self.health > 0):
            return True
        elif(self.health == 0):
            return False
        else:
            return(str(self.health) + "Amina Koydu")

guy = Soldier()

guy.health = 0

guy.taken_damage()

#print(guy.isAlive())

print("*************************\n")


class Student:

    def __init__(self):
        ID = "000000"
        print(ID)


    def full_name(self):
        print("Name Surname")


#james = Student()
#james.full_name()

print("*************************\n")

class Enemy:

    def __init__(self, var):
        self.energy = var

    def attack(self):
        self.energy /= 2

    def getEnergy(self):
        print(self.energy)

adam = Enemy(60)

#adam.getEnergy()
adam.attack()
#adam.getEnergy()

print("*************************\n")


class Woman:

    sex = "female"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def changeName(self, name):
        self.name = name

    def changeAge(self, age):
        self.age = age

    def showCast(self):
        print("\nName: " + self.name + "\nAge:" + str(self.age) + "\nSex:" + self.sex)


fatma = Woman("fatma", 30)

#fatma.showCast()
fatma.changeName("Ilknur")
fatma.changeAge(25)
#fatma.showCast()

print("*************************\n")


class teacher:

    name = "None"

    def __init__(self, name):
        self.name = name
    def show(self):
        print("Main")

class mathTeacher(teacher):

    knowledge = "Math"
   # name = "string"
    def show(self):
       print("\nknowledge:" + self.knowledge + "\nName:" + self.name)

class deli(mathTeacher,teacher):
    pass

human = deli("Kutay")

#deli.show()

print("*************************\n")

#TupleDataUnpacking

ddl,ddl2,ddl3 = ['1 October 2019', 'Aristotales', 25]

#print(ddl)
#print(ddl2)

print("*************************\n")

def calc(*args):

    first, *second, third = args

    avg = sum(second) / len(second)

    print(avg)

calc(0,30,30,40,0)
