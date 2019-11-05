from datetime import datetime

odds = [ 1,  3,  5,  7,  9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59 ]

right_this_time = datetime

if right_this_time in odds:

    print("This minute seems a little odd. ")

else:

    print("Not an odd minute")


print("\n*******************************\n")


for i in [1,2,3]:

    print (i," ")

print("\n*******************************\n")

for j in "Spelling":

    print(j)

print("\n*******************************\n")

for i in range(5):

    print("Hello World!")


print("\n*******************************\n")

import random
import time

for i in range( random.randint(1, 5) ):

    right_this_time = datetime.today().minute

    if right_this_time in odds:

        print("This minute seems a little odd. ", i)

    else:

        print("Not an odd minute ", i)

    time.sleep(5)


print("\n*******************************\n")

