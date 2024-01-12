from math import pi

def square_footage():

    while True:
        print("Getting square footage: ")
        user_length = input("What is the length of your house?: ")
        user_width = input("What is the width of your house?: ")

        area = int(user_length) * int(user_width)
    
        return area



def circumference():

    while True:
        print("Getting a circle's circumference:")
        user_input = input("Input the circle's radius: ")

        circ = 2 * pi * int(user_input)

        return circ
