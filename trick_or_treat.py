#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# A fun trick or treat game for PfGWC
import random
from candy import candy_list

# The cool writing can be done at http://patorjk.com/software/taag/
print("""
██████╗ ███████╗ ██████╗ ██╗    ██╗ ██████╗
██╔══██╗██╔════╝██╔════╝ ██║    ██║██╔════╝
██████╔╝█████╗  ██║  ███╗██║ █╗ ██║██║     
██╔═══╝ ██╔══╝  ██║   ██║██║███╗██║██║     
██║     ██║     ╚██████╔╝╚███╔███╔╝╚██████╗
╚═╝     ╚═╝      ╚═════╝  ╚══╝╚══╝  ╚═════╝


▄▄▄█████▓ ██▀███   ██▓ ▄████▄   ██ ▄█▀    ▒█████   ██▀███     ▄▄▄█████▓ ██▀███  ▓█████ ▄▄▄     ▄▄▄█████▓
▓  ██▒ ▓▒▓██ ▒ ██▒▓██▒▒██▀ ▀█   ██▄█▒    ▒██▒  ██▒▓██ ▒ ██▒   ▓  ██▒ ▓▒▓██ ▒ ██▒▓█   ▀▒████▄   ▓  ██▒ ▓▒
▒ ▓██░ ▒░▓██ ░▄█ ▒▒██▒▒▓█    ▄ ▓███▄░    ▒██░  ██▒▓██ ░▄█ ▒   ▒ ▓██░ ▒░▓██ ░▄█ ▒▒███  ▒██  ▀█▄ ▒ ▓██░ ▒░
░ ▓██▓ ░ ▒██▀▀█▄  ░██░▒▓▓▄ ▄██▒▓██ █▄    ▒██   ██░▒██▀▀█▄     ░ ▓██▓ ░ ▒██▀▀█▄  ▒▓█  ▄░██▄▄▄▄██░ ▓██▓ ░ 
  ▒██▒ ░ ░██▓ ▒██▒░██░▒ ▓███▀ ░▒██▒ █▄   ░ ████▓▒░░██▓ ▒██▒     ▒██▒ ░ ░██▓ ▒██▒░▒████▒▓█   ▓██▒ ▒██▒ ░ 
  ▒ ░░   ░ ▒▓ ░▒▓░░▓  ░ ░▒ ▒  ░▒ ▒▒ ▓▒   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░     ▒ ░░   ░ ▒▓ ░▒▓░░░ ▒░ ░▒▒   ▓▒█░ ▒ ░░   
    ░      ░▒ ░ ▒░ ▒ ░  ░  ▒   ░ ░▒ ▒░     ░ ▒ ▒░   ░▒ ░ ▒░       ░      ░▒ ░ ▒░ ░ ░  ░ ▒   ▒▒ ░   ░    
  ░        ░░   ░  ▒ ░░        ░ ░░ ░    ░ ░ ░ ▒    ░░   ░      ░        ░░   ░    ░    ░   ▒    ░      
            ░      ░  ░ ░      ░  ░          ░ ░     ░                    ░        ░  ░     ░  ░        
                      ░                                                                                 

""")
# Remember that triple quote strings like """Hello""" let you add mulitple lines like above.

print("To play the game of PfGWC Trick or Treat, start by entering your name and costume.")
name = input("What is your name? ")
costume = input("What are you dressed up as? ")
# The input function prints text and then waits for the user to type something
# It then puts that something into any variable you give it, like the name and costume
# variables above.

print("Hi " + name + "!", "You look great as a " + costume + "!")
print()
do_not_care = input("Would you like to start trick or treating? ")
print("""
Great, let's get started!

At each house you can either take a treat or play a trick on the nice person handing out candy.
Type 'treat' to take a treat. If you take a treat, a candy will be added to your candy bag.
Type 'trick' to play a trick. If you play a trick, a candy will be removed from your candy bag.
Type 'goodnight' to end the game.
""")
do_not_care = input("Understand? ")
print("Great! Let's go!")
print()

candy_bag = []
game_over = False
# Here we are setting some variables to their initial values.
# They will be changed later based on what the user does.

# Below are functions we have defined ahead of time so that we can use them in our program.
# Each function does something small and repeatable, which makes it easier for us to reuse them ;)

# This function uses the random.choice function to get a random item from our candy_list
# variable (hint: You can find candy_list in the candy.py file).
# The function then uses the return keyword to send that candy item to whoever called the function.
# Each time the function is called, a new candy is returned.
def handout_candy():
    return random.choice(candy_list)

# This function will remove the last candy in our candy_bag using the list.pop() function
# If our candy_bag is empty (i.e. 'len(candy_bag) > 0' is not True), then we will not call the
# list.pop() function.
def take_candy():
    print("Nice person: Hey! I'm taking a candy from you!")
    if len(candy_bag) > 0:
        candy = candy_bag.pop()
        print("You lost a " + candy + "!")
    else:
        print("You have no candy!!")

# This function will add a candy we get from the handout_candy() function to our candy_bag
# list using the function list.append().
def give_candy():
    candy = handout_candy()
    print("Nice person: Aw, here's a " + candy + " for you!")
    candy_bag.append(candy)

# Now we come to the main part of our program.  This is actually called the game loop in
# gaming.  It is a while loop that keeps going forever until the game is "over".
# Our game is over when the variable game_over is given the value True.
print("You've come to your first house!")
while game_over == False:
    print("Nice person: Well hello there little " + costume + "!")
    # tot is short for Trick or Treat
    tot = input(name + ": Trick or Treat! ")
    if tot == 'trick':
        take_candy()
    elif tot == 'treat':
        give_candy()
    elif tot == 'goodnight':
        game_over = True
    else:
        print("Nice person: Umm okay... bye")
    print()
    if game_over == True:
        print("Time to go home.")
    else:
        print("Next house!")

# When our game loop is over, the program comes down here to print all the candy in our
# candy_bag and count the number of candy pieces we got.
print("What a fun night!")
print("You got:")
count = 0
for candy in candy_bag:
    count = count + 1
    print(candy)
print("That's " + str(count) + " pieces of candy!")
# Note, you have to change the count variable from a number to a string with the str()
# function, otherwise the program does not know how to concat (aka add) a string and a number
# together.
# (BTW, you could get the number of candy pieces by using 'len(candy_bag)' too)
