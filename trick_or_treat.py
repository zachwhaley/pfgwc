#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# A fun trick or treat game for PfGWC

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
    return 'Snickers'

candy_bag = []
game_over = False
while game_over == False:
    print("Nice person: Well hello there little " + costume + "!")
    trick_or_treat = input(name + ": Trick or Treat! ")
    candy = handout_candy()
    if trick_or_treat == 'trick':
        print("Nice person: Hey! I'm taking a candy from you!")
        if candy in candy_bag:
            candy_bag.remove(candy)
            print("You lost a " + candy + "!")
        else:
            print("You ran away. No candy lost!")
    elif trick_or_treat == 'treat':
        print("Nice person: Aw, here's a " + candy + " for you!")
        candy_bag.append(candy)
    elif trick_or_treat == 'goodnight':
        print("Time to go home.")
        game_over = True
    else:
        print("Nice person: Umm okay... bye")
    print()
    if game_over == False:
        print("Next house!")

print("What a fun night!")
print("You got:")
print(candy_bag)
