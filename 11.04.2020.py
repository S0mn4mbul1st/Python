'''

value = input()
print(value)
'''

print("***********************\n")

def sentence (main = "Ben" , Sec = "Eats" , Last = "Burger"):

    print (main, Sec, Last)

sentence()
sentence("He")
sentence("He", "Drinks", "Cola")
sentence(Sec = "Changes")

print("***********************\n")

def add(*args):

    sum = 0;

    for adder in args:

        sum += adder

    print(sum)

add(5)
add(5,10,15)

values = [1,2,3,4]

add(values[0], values[1], values[2], values[3])
add(*values)

print("***********************\n")

numbersA = {"one","one", "two", "three", "four"}
numbersB = ["one","one", "two", "three", "four"]

print(numbersA)
print(numbersB)

print("***********************\n")

