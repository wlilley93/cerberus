# By Will Lilley
# Originally written in 2017
# Updated in 2020

import time

# Define game parameters

# Establish yes no question answers
yes = {'yes', 'y', 'ye'}
no = {'no', 'n'}

class Hero:

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.damage_stat = 0

        # Player Inventory Size shouldn't be exceeded. p_Inv_size defines the potential size of the inventory.

        self.p_Inv_size = 2

    ########################################
    #            User inventory            #
    #    Player begins with a single item  #
    #                                      #
        self.inventory = ["useless fluff"]
    ########################################

    # A tool to see how an event might have affected a self's stats

    def printstats(self):
        print("\nYour Name: " + self.name)
        print("Your Current Health: " + str(self.health))
        print("Inventory Listing " + str(self.inventory))
        print("Inventory Slots " + str(self.p_Inv_size))
        print("Items in your Inventory: " + str(len(self.inventory)))
        print("Damage Infliction: " + str(self.damage_stat) + "\n")

    # ITEM LIST - lists all items in the game and their associated attributes.
    # The give function performs an inventory check after each item is given
    # to ensure that selfs do not exceed their inventory limit.

    def give(self, item):

        # The bag does not sit in the inventory because once picked up it becomes
        # the inventory (and increases the potential inventory size limit by 2)

        if item == "bag":
            self.p_Inv_size += 2

        elif item == "apple":
            self.inventory.append("apple")
            self.invcheck()

        elif item == "p_apple":
            self.inventory.append("glowing apple")
            self.invcheck()

        elif item == "ham":
            self.inventory.append("ham")
            self.invcheck()

        elif item == "golden ham":
            self.inventory.append("golden ham")
            self.invcheck()

        elif item == "knife":
            self.damage_stat += 10
            self.inventory.append("knife")
            self.invcheck()

        elif item == "sword":
            self.damage_stat += 40
            self.inventory.append("sword")
            self.invcheck()

        elif item == "mace":
            self.damage_stat += 50
            self.inventory.append("mace")
            self.invcheck()

    # Defines the effect of eating food

    def eat(self, food):

        if food == "apple":
            self.health += 10

        elif food == "p_apple":
            self.health -= 20

        elif food == "ham":
            self.health += 20

        elif food == "golden Ham":
            self.health += 50

    # Defines the effect of inflicting damage upon an object with a weapon

    def inflict(self, weapon):

        if weapon == "knife":
            self.health -= 10

        elif weapon == "sword":
            self.health -= 50

        elif weapon == "mace":
            self.health -= 100

    # The next section deals with swapping out an item for a prospective item
    # when the inventory limit exceeds the potential inventory limit
    #
    # item_exchange exchanges a current inventory item with a prospective inventory item.

    def item_exchange(self):

        # When a new item causes the inventory limit to exceed the potential inventory
        # limit, the item  remains in the list until removed.
        #
        # It is not removed instantly because the offending item is relied upon later in item_exchange.
        # There is no need to remove the item as del_recent_item removes the final list element.
        # Here the inventory is printed with the last item sliced off instead of removing it
        # to make it appear as though the item has already been removed.

        item_exchange_prompt = "\nYour inventory currently contains \n" + str(self.inventory[:-1])
        print(item_exchange_prompt)

        # Calculate the length of inventory minus the index number of self's selected element to remove

        while True:

            try:

                global pos_reversal_int
                pos_reversal_int = (len(self.inventory) - (int(self.inventory.index(input("\nWhich item are "
                                    "you replacing?\n" + self.name + ""
                                                                                              ": ")))))
                break

            except ValueError:

                print("\nSorry, that item isn't in your inventory.")
                print(item_exchange_prompt)

        # Take pos_reversal_int away from itself twice to give its value as a negative number

        neg_reversal_int = (pos_reversal_int - (pos_reversal_int * 2))

        # Use the negative number to locate and replace the chosen outgoing item with the incoming item
        # The incoming item is currently located as the final item in the inventory list

        self.inventory[neg_reversal_int] = item_to_drop
        print("\nYour inventory now contains:")
        #
        # The incoming item is no longer relied upon so it can be deleted
        # (along with attributes) through del_recent_item.
        #
        self.del_recent_item()
        print(self.inventory)

    # del_recent_item drops the final element from the inventory list
    # (in this case the most recently added item)

    def del_recent_item(self):

        # First check that the inventory size exceeds the potential inventory size

        if len(self.inventory) > self.p_Inv_size:

            # If the item to be dropped matches the below strings, drop it
            # from the inventory and also remove any extra attributes assigned to that item

            if item_to_drop == "apple":
                self.inventory.pop()

            elif item_to_drop == "p_apple":
                self.inventory.pop()

            elif item_to_drop == "ham":
                self.inventory.pop()

            elif item_to_drop == "golden Ham":
                self.inventory.pop()

            elif item_to_drop == "knife":
                self.damage_stat -= 10
                self.inventory.pop()

            elif item_to_drop == "sword":
                self.damage_stat -= 40
                self.inventory.pop()

            elif item_to_drop == "mace":
                self.damage_stat -= 50
                self.inventory.pop()

    # The initial inventory check.
    # "Whilst it is true" that the inventory exceeds the maximum potential inventory size,
    # Ask whether the user wants to exchange or delete a prospective item.

    def invcheck(self):

        while len(self.inventory) > self.p_Inv_size:

            global item_to_drop
            item_to_drop = self.inventory[-1]
            time.sleep(0.6)

            # As the del_recent_item function has not run yet, the offending item is still
            # the final element in the list. This means it can be called to create the following
            # sentence:

            print("\nYour inventory is full.\nYou have no way to carry the " + (self.inventory[-1]) + ".\n")

            # Define the question that will be asked presently
            item_exchange_question = input("Do you want to exchange an item in your inventory for the " +
                                           (self.inventory[-1] + "?\n" + self.name + ": "))

            if item_exchange_question in yes:

                    # Initiate the item exchange function
                    self.item_exchange()

            elif item_exchange_question in no:

                    # Remove the item from the inventory
                    print("You leave the " + item_to_drop + " behind.")
                    self.del_recent_item()

            else:
                print("\nPlease respond with 'yes' or 'no'.\n")

                # Repeat the question

                self.invcheck()

pass
