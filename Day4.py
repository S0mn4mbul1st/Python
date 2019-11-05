vowels = ['a', 'e', 'i' ,'o', 'u']

word = "Milliways"

for letter in word:

    if letter in vowels:

        print(letter)

print ("****************************\n")

vowels = ['a', 'e', 'i' ,'o', 'u']

word = "Provide a word to search for vowels"

found = []

for letter in word:

    if letter in vowels:

     if letter not in found:

      found.append(letter)

print(found)



print ("****************************\n")



//119