from itertools import chain
from operator import inv
from time import sleep
from tkinter import END
import random

class Tools():
    money = 0

inventory = []


# WEAPONS

class Weapons(object):
    Torch = 3
    Sword = 5
    potion = 25


# Hero

class Berry(object):
    health = 150
    strength = 10
    defence = 10
    magic = 1

class Wizard(object):
    health = 125
    strength = 7
    defence = 7
    magic = 10

class Maggie(object):
    health = 100
    strength = 7
    defence = 10
    magic = 6


# Enemy Classes

class Bat(object):
    name = "Bat"
    health = 20
    strength = 1
    defence = 3
    loot = random.randint(0,2)

class Goblan(object):
    name = "Goblan"
    health = 30
    strength = 2
    defence = 2
    loot = random.randint(0,2)

class Troll(object):
    name = "Troll"
    health = 40
    strength = 5
    defence = 1.5
    loot = random.randint(0,2)


# hero select
def heroselect():
    print("Select your hero! ")
    hero_select = input("1. Berry \n2. Elf \n3. Maggie \n")
    if hero_select == "1":
        character = Berry
        print("You have selected Berry.... here is his stats")
        print("Health - ", character.health)
        print("Strength - ",character.strength)
        print("Defence - ",character.defence)
        print("Magic - ",character.magic)
        return character

    elif hero_select == "2":
        character = Wizard
        print("You have selected the wizard...here are the stats")
        print("Health - ", character.health)
        print("Strength - ",character.strength)
        print("Defence - ",character.defence)
        print("Magic - ",character.magic)
        return character

    elif hero_select == "3":
        character = Maggie
        print("You have selected Maggie...here are her stats")
        print("Health - ", character.health)
        print("Strength - ",character.strength)
        print("Defence - ",character.defence)
        print("Magic - ",character.magic)
        return character

    else:
        print("Only press 1, 2 or 3")
        heroselect()
    
def loot():
    loot = ["Sword", "Shield", "Health potion"]
    lootChance = random.randint(0,2)
    lootDrop = loot[lootChance]
    return lootDrop

def enemyselect(Goblin,Bat,Troll):
    enemyList = [Goblin,Bat,Troll]
    chance = random.randint(0,2)
    enemy = enemyList[chance]
    return enemy


# fighting
def DEAD():
    sleep(3)
    print("YOU HAVE DIED")
    print("DO YOU WANT TO GO BACK TO MENUE OR QUIT")
    print("inventory = ",inventory)
    print("money = ",Tools.money)
    DEAD_input = input("DEAD# ")
    if DEAD_input == "menue":
        inventory = []
        menue()
    
    elif DEAD_input == "quit":
        END

def World_1_enemys():

    # here we select the enemy that we willl battle
    enemy = enemyselect(Goblan,Bat,Troll)
    print("a wild", enemy.name, "has appeared!")

    while enemy.health > 0:
        print("inventory = ",inventory)
        choise = input("chose weapon # ").lower().strip()
        hitchance = random.randint(0,10)  

        # To see if the weapon is in our inventory and then use it
        if choise == "torch" and ("Torch") in inventory:
            weapon = Weapons.Torch    
            
            # Make a hit chance for your character
            if hitchance > 3:
                enemy.health = enemy.health - ((character.strength + weapon) / enemy.defence)
                print("")
                print("You landed a hit...")
                print("enemy health =",enemy.health)
                sleep(2)

            # Make the enemy take a swing and they hit if they are not dead
                if enemy.health > 0:
                    character.health = character.health - (enemy.strength / character.defence)
                    print("")
                    print("the enemy is attacking...")
                    sleep(3)
                    print("The ",enemy.name," takes a swing and hits")
                    print("character health = ",character.health)

            # Reset the health of the enemys
                else:
                    if enemy.name == "Goblin":
                        enemy.health = 30                       

                    elif enemy.name == "Bat":
                        enemy.health = 20

                    elif enemy.name == "Troll":
                        enemy.health = 40
            
            # The loot that you will get for killing it
                    print("You have defeated the",enemy.name)
                    lootDrop = loot()
                    print("You found a",lootDrop)
                    print(lootDrop,"STORED")
                    inventory.append(lootDrop)
                    Tools.money = Tools.money + 25
                    print("YOU GAINED 25 GOLD")
                    print("WORLD COMPLETED")
                    menue()
            
            # You miss the swing of the sword

            else:
                print("Your lost grip of the sword and missed")
                print("The",enemy.name," hits you for full damage")
                character.health = character.health - enemy.strength
                print("you have ",character.health,"remaining")

    # Make sure they have the weapon





        elif choise == "":
            if hitchance > 3:
                enemy.health = enemy.health - (character.strength / enemy.defence)
                print("")
                print("You landed a hit...")
                print("enemy health =",enemy.health)
                sleep(1)

            # Make the enemy take a swing and they hit if they are not dead
                if enemy.health > 0:
                    character.health = character.health - (enemy.strength / character.defence)
                    print("")
                    print("Enemy is attcking...")
                    sleep(2)
                    print("The ",enemy.name," takes a swing and hits")
                    print("character health = ",character.health)

            # Reset the health of the enemys
                else:
                    if enemy.name == "Goblin":
                        enemy.health = 30                       

                    elif enemy.name == "Bat":
                        enemy.health = 20

                    elif enemy.name == "Troll":
                        enemy.health = 40
            
            # The loot that you will get for killing it
                    print("You have defeated the",enemy.name)
                    lootDrop = loot()
                    print("You found a",lootDrop)
                    print(lootDrop,"STORED")
                    inventory.append(lootDrop)
                    Tools.money = Tools.money + 25
                    print("YOU GAINED 25 GOLD")
                    print("WORLD COMPLETED")
                    menue()          
            # You miss the swing of the sword

            else:
                print("Your lost grip of the sword and missed")
                print("The",enemy.name," hits you for full damage")
                character.health = character.health - enemy.strength
                print("you have ",character.health,"remaining")






        elif choise == "sword":
            weapon = Weapons.Sword
            if hitchance > 3:
                enemy.health = enemy.health - ((character.strength + weapon) / enemy.defence)
                print("")
                print("You landed a hit...")
                print("enemy health =",enemy.health)
                sleep(1)

            # Make the enemy take a swing and they hit if they are not dead
                if enemy.health > 0:
                    character.health = character.health - (enemy.strength / character.defence)
                    print("")
                    print("Enemy is attaching...")
                    sleep(2)
                    print("The ",enemy.name," takes a swing and hits")
                    print("character health = ",character.health)

            # Reset the health of the enemys
                else:
                    if enemy.name == "Goblin":
                        enemy.health = 30                       

                    elif enemy.name == "Bat":
                        enemy.health = 20

                    elif enemy.name == "Troll":
                        enemy.health = 40
            
            # The loot that you will get for killing it
                    print("You have defeated the",enemy.name)
                    lootDrop = loot()
                    print("You found a",lootDrop)
                    print(lootDrop,"STORED")
                    inventory.append(lootDrop)
                    Tools.money = Tools.money + 25
                    print("YOU GAINED 25 GOLD")
                    print("WORLD COMPLETED")
                    menue()
            
            # You miss the swing of the sword

            else:
                print("Your lost grip of the sword and missed")
                print("The",enemy.name," hits you for full damage")
                character.health = character.health - enemy.strength
                print("you have ",character.health,"remaining")


        elif choise == "health potion":
            inventory.remove("Health potion")
            character.health = character.health + 25
            print("Drinking health potion...")
            sleep(2)
            print("hero health = ",character.health)
            sleep(3)

            if enemy.health > 0:
                print("")
                character.health = character.health - (enemy.strength / character.defence)
                print("")
                print("Enemty attacking...")
                sleep(2)
                print("The ",enemy.name," takes a swing and hits")
                print("character health = ",character.health)

            # Reset the health of the enemys
            else:
                if enemy.name == "Goblin":
                    enemy.health = 30                       

                elif enemy.name == "Bat":
                    enemy.health = 20

                elif enemy.name == "Troll":
                    enemy.health = 40


        elif character.health < 0:
            DEAD()



        else:
            print("That is not a valid input")





def world_1():
    print("")
    print("########## WELCOME TO WORLD 1 ########")
    print("")
    sleep(1)
    print("You are in a dark cave")
    sleep(2)
    print("There is a door in from of you and black walls on your sides")
    sleep(2)
    print("You also see a Torch next to you")
    sleep(2)
    print("What do you do?")
    while True == True:
        torch_pick = 0
        pickuptorch = ["pick up torch", "pick up the torch", "take the torch"]
        opendoor = ["open the door", "open door", "unlock door", "unlock the door"]
        lookforkey = ["look for the key", "look for a key", "find a key", "find the key", "search for the key", "look for key", "look around"]
        tourch_input = input("# ").lower()
    # Picking up the tourch and the key for the door

        if tourch_input in pickuptorch and torch_pick < 1:
            torch_pick = torch_pick + 2
            inventory.append("Torch")
            print("TOURCH STORED")

        elif tourch_input in opendoor and ("Key") not in inventory:
            print("Door is locked")
            sleep(1.3)
            print("Type hint if you need help")

        elif tourch_input in opendoor and ("Key") in inventory:
            print("The door opens")
            inventory.remove("Key")
            sleep(2.4)
            break
            
        elif tourch_input == "hint":
            print("Try looking for Key")

        elif tourch_input in lookforkey:
            print("searching.....")
            sleep(3)
            print("You fond a key")
            inventory.append("Key")
            print("KEY STORED")

        else:
            print("Do not understand")
    
    print("")
    print("You have finaly escaped the cave")
    sleep(3)
    print("You are now standing in front of a rainforest")
    sleep(3)
    print("But not just any rain forest there apeares to be MAGICAL creatures")
    sleep(3)
    print("As you look around you see a one of those creatures")
    sleep(4)
    print("Do you want to fight it to fight?")
    fight_lion = input("# ").lower().strip()

    if fight_lion == "yes":
        World_1_enemys()


    elif fight_lion == "no":
        print("IT ATTACKS YOU FIRST AND YOU DIE")
        DEAD()

    else:
        print("not a valid input")

# Menue
def menue():
    #making the menue for the levels and the inventory

    print("")
    print("########### This is the menue ##########")
    print("If you want to see your inventory type inv and to see your money type money")
    print("To see the worlds type worlds")
    print("AND TYPE store TO SEE THE GREAT STORE")
    brick = True

    while brick == True:
        user = input("# ").lower().strip()

        if user == "inv":
            print(inventory)

        elif user == "money":
            print(Tools.money)

        elif user == "worlds":
            print("world 1, level 2, level 3")
            print("chose a level")

        elif user == "1":
            world_1()

        elif user == "level 2":
            print("not avalable")

        elif user == "level 3":
            print("not avalable")
        
        elif user == "store":
            Store()

        else:
            print("only enter the number")

def Store():
    print("")
    print("-----------Welcome to the Store-------------")
    print("YOU ARE NOW IN THE STORE SELECT THE ITEM THAT YOU WANT TO BUY")
    print("If you want to go back to menue type menue")
    print("1. Sword $75\n2. Torch $10\n3. health potion $25")

    while 1 == 1:
        store_input = input("MUN# ")
        buy = store_input

        if buy == "1" and (Tools.money >= 75):
            print("")
            Tools.money = Tools.money - 75
            inventory.append("Sword")
            print("SWORD PURCHASED")
            print("")
        
        elif buy == "money":
            print(Tools.money)

        elif buy == "stompie":
            Tools.money = Tools.money + 1000

        elif store_input == "menue":
            menue()

        elif buy == "2" and (Tools.money >= 50):
            print("")
            Tools.money = Tools.money - 50
            inventory.append("Torch")
            print("TORCH PURCHASED")
            print("")

        elif buy == "3" and (Tools.money >= 25):
            print("")
            Tools.money = Tools.money - 25
            inventory.append("Health potion")
            print("HEALTH POTION PURCHASED")
            print("")
    
        else:
            print("INSUFFICIENT FUNDS")


def RULES():
    print("HELLO")
    print("1. you can only pick up the torch on world 1, 1 time")
    print("2. if it does not understand then make sure that there are no spaces at the end of the word")
    print("")

# WORLDS


character = heroselect()
menue()