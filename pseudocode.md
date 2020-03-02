Main Overlook Pseudo Code:

BEGIN Dungeon Desertion
    BEGIN MENU
    END MENU


While Health > 0:
BEGIN movement
If Health < 0:
    END WHILE

INPUT: "GAME OVER, PLAY AGAIN?"
IF input is "yes"
    BEGIN Menu
Else:
    End Dungeon Desertion


Menu Code:

BEGIN Menu:
    PRINT logo
    INPUT: "What do you wish to choose?"
    CASEWHERE:
        1 : "start", BEGIN movement
        2 : "instructions", BEGIN HelpMe
        3 : "exit", END Menu
    END CASEWHERE
END Menu


Movement Code:
    WHILE Health > 0:
        BEGIN Show Status

        INPUT: "What will you do?"
        Go North: Move Forward
        Go South: Move Backward
        Go East : Move Right
        Go West : Move Left
        Get     : BEGIN Get
        Talk    : BEGIN Talk
        help me : BEGIN HelpMe
        Use     : BEGIN Use
        Inv     : BEGIN Inv  
        END CASEWHERE
    IF Health < 0
    END WHILE
END Movement


HelpMe Code:
BEGIN HelpMe
    PRINT the game commands
    INPUT "Continue?"
END HelpMe


Get Code:
BEGIN Get
    INPUT the item you want to get
        IF item is in chest:
            Add the item to your inventory
            Delete the item from room
        ELSE:
        PRINT "Item not in chest"
END Get


Use Code:

BEGIN Use:
    INPUT the item you want to use
    IF item is in inventory
        use the item if it can be used

    ELSE:
     Print "Item is not in inventory"

END USE


Inv Code:
BEGIN Inv:
    PRINT the inventory
END Inv


Show Status Code:

BEGIN Show Status:
    PRINT Health
    PRINT the room you are in
    PRINT information about the room

    IF boss is in the room:
        BEGIN Battle

    ELSE:
    PRINT "What shall you do?"
END Show Status


Battle Code:
BEGIN Battle:
    PRINT "You are under attack by the boss, what shall you do?"
        Make a random number

    IF you use a sword make a random number between 50 and 100 which shall be your
    attack, and remove your attack damage from enemy's health
    PRINT "You did (attack) damage to boss"
ELSE:
    PRINT "You missed"

    ELIF you use a bow make a random number between 50 and 75 which shall be your
    attack, and remove your attack damage from enemy's health
    PRINT "You did (attack) damage to boss"
ELSE:
    PRINT "You missed"

    ELIF you use an axe make a random number between 30 and 60 which shall be your
    attack, and remove your attack damage from enemy's health
    PRINT "You did (attack) damage to boss"
ELSE:
    PRINT "You missed"

IF INPUT is Health Potion:
    generate a random number between 50 and 100 which shall be heal
    Add heal to your health

IF INPUT is Strength Potion:
    Increase damage by 25%

IF INPUT is Invincibility Potion:
    Add an infinite amount of heal to your health for 5 attacks

IF INPUT is Poison Potion:
    Generate a random between 70 and 80 which shall be your
    attack, and remove your attack damage from enemy's health
    PRINT "You did (attack) damage to boss"
ELSE:
    PRINT "You missed"

After you use a potion or use a weapon the boss will attack you for a random
amount of damage

ELIF: Your Health < 0
    INPUT: "GAME OVER, PLAY AGAIN?"
        IF input is "yes"
    BEGIN Menu
    Else:
        END Battle

ELIF: Boss' Health < 0
    INPUT: "You've defeated the boss."

ELSE:
    PRINT "Invalid Input"

    Make a random number (to find out if the boss hits or not)
        IF you get a number which allows you to hit
        Make another random number which shall be the boss' attack
        Remove the boss' attack from your health
END Battle
