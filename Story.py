# Main Story File

from hero_class import *

# Create player
player = Hero(input("\nHello there, adventurer!\nWhat is your name?\n\nYou: "))
print("\nWelcome, " + player.name + ", to the adventure.\n")
print("You begin the adventure with " + str(player.health) + " health.")
print("You don't have any weapons yet, so you inflict " + str(player.damage_stat) + " damage.")
print("You are holding " + str(len(player.inventory)) + " items and your inventory limit is " +
      str(player.p_Inv_size) + ".\n")

# Initial Room
print("You are inside a small room.\nIn front of you is a table.\nBeyond the table is a door.\n")

# Define 4 Questions:
# Approach the table?
# Pick up the bag?
# Pick up the knife?
# Pick up the apple?

def table_approach_question():

    table_approach = input("Approach the table?\n" + player.name + ": ").lower()

    if table_approach in yes:
        print("\nOn the table is a bag, a knife and an apple.\n")
        bag_choice_question()

    elif table_approach in no:
        print("\nYou move past the table and leave through the door.")

    else:
        print("\nSorry, " + player.name + ". Please respond with 'yes' or 'no'.\n\n")
        table_approach_question()

def bag_choice_question():

    bag_choice = input("Pick the bag up?\n" + player.name + ": ").lower()

    if bag_choice in yes:
        print("\nYou got the bag.")
        player.give("bag")
        print("You can now hold " + str(player.p_Inv_size) + " items.\n")
        knife_choice_q()

    elif bag_choice in no:
        print("\nYou left the bag behind.\n")
        knife_choice_q()

    else:
        print("\nSorry, " + player.name + ". Please respond with 'yes' or 'no'.\n\n")
        bag_choice_question()

def knife_choice_q():

    knife_choice = input("Grab the knife?\n" + player.name + ": ").lower()

    if knife_choice in yes:
        print("\nYou got the knife.")
        player.give("knife")
        print("You now inflict " + str(player.damage_stat) + " damage.\n")
        apple_p_choice_q()

    elif knife_choice in no:
        print("\nYou left the knife behind.\n")
        apple_p_choice_q()

    else:
        print("\nSorry, " + player.name + ". Please respond with 'yes' or 'no'.\n\n")
        knife_choice_q()

def apple_p_choice_q():
    apple_p_choice = input("Take the apple?\n" + player.name + ": ").lower()

    if apple_p_choice in yes:
        print("\nYou got the apple.")
        print("The apple has an unnatural glow.")
        player.give("apple")
        print("\nYou move past the table and leave through the door.")

    elif apple_p_choice in no:
        print("\nYou left the apple behind.")
        print("\nYou move past the table and leave through the door.")

    else:
        print("\nSorry, " + player.name + ". Please respond with 'yes' or 'no'.\n\n")
        apple_p_choice_q()

# Execute the question tree
table_approach_question()

player.printstats()
