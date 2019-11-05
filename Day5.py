alien = { 'color' : 'green' , 'points' : 5 }

print ( alien['color'] , alien['points'] )


alien ['color'] = 'Yellow'

alien ['points'] = alien ['points'] + 1

print ( alien['color'] , alien['points'] )


print ("\n****************************\n")


fav_numbers = {'Aykhan': 17, 'Imanov': 4}

for name, number in fav_numbers.items():

    print(name + ' loves ' , number )


print ("\n****************************\n")


name = ("inputWhat is your name bro? : ")

print("Well, Fuck you dear" , name,'....')


print ("\n****************************\n")


current_value = 1

while current_value <= 5:

    print(current_value)

    current_value += 1

print("\n****************************\n")

"""
    msg = ''

    while msg == 'exit':

        msg = ('inputEnter your message please. ')

        print (msg)
"""

print("\n****************************\n")


def bfs():

    """Display a simple greeting"""

    print('Hello World ! ','\n')


bfs()


def dfs(username = 'ali '):

    print('Hello Dear',username)

dfs("Kamal")

def sum( a, b ):

    return a + b


print((sum ( 3,5 )))



print("\n****************************\n")



class Dog():

   def init(self, name):

       """Initialize dog object."""

       self.name = name


   def sit(self):

    """Simulate sitting."""

    print(self.name + " is sitting.")




my_dog = Dog()

print(my_dog.name + " is a great dog!")

my_dog.sit()


class SARDog(Dog):


  def __init__(self, name):


   super().__init__(name)


  def search(self):


   print(self.name + " is searching.")

my_dog = SARDog('Willie')

print(my_dog.name + " is a search dog.")

my_dog.sit()

my_dog.search()


print("\n****************************\n")


