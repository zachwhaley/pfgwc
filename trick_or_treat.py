#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# A fun trick or treat game for PfGWC
import random
from candy import candy_list

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
print("To play the game of PfGWC Trick or Treat, start by entering your name and costume.")
name = input("What is your name? ")
costume = input("What are you dressed up as? ")
print("Hi " + name + "!", "You look great as a " + costume + "!")
print()
do_not_care = input("Would you like to start trick or treating? ")
print("Great, let's get started!")
print()
print("At each house you can either take a treat or trick the nice person handing out candy.")
print("If you take a treat, a candy will be added to your candy bag.")
print("If you trick the person, a candy will be removed from your candy bag.")
print("To end the game, type 'goodnight'")
do_no_care = input("Understand? ")
print("Great! let's go!")
print()
print("You've come to your first house!")

def handout_candy():
    return random.choice(candy_list)

candy_bag = []
game_over = False
while game_over == False:
    print("Nice person: Well hello there little " + costume + "!")
    trick_or_treat = input(name + ": Trick or Treat! ")
    if trick_or_treat == 'trick':
        print("Nice person: Hey! I'm taking a candy from you!")
        if len(candy_bag) > 0:
            candy = candy_bag.pop()
            print("You lost a " + candy + "!")
        else:
            print("You have no candy!!")
    elif trick_or_treat == 'treat':
        candy = handout_candy()
        print("Nice person: Aw, here's a " + candy + " for you!")
        candy_bag.append(candy)
    elif trick_or_treat == 'goodnight':
        print("Time to go home.")
        game_over = True
    else:
        print("Nice person: Umm okay... bye")
    if game_over == False:
        print("Next house!")
    print()

print("What a fun night!")
print("You got:")
print(candy_bag)
