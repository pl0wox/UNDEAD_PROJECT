class Undead:   # parent class
    def __init__(self, name, health, damage, status):
        self.undead_name = name
        self.undead_health = health
        self.undead_damage = damage
        self.undead_status = status


def print_main_menu():  # main menu
    return """          U N D E A D
    
    [1] - Create Undead
    [2] - Command Undead
    [3] - Display Undead
    [4] - Exit 
    """


def navigate(x):    # switch case for the menu choices
    match x:
        case 1:
            return "Zombie"
        case 2:
            return "Tite"
        case _:
            return 0


def choice():   # function for getting choice input from user
    ch = (int(input("Please select your choice: ")))
    return ch


print(print_main_menu())  # print menu
print(navigate(choice()))  # user choice
