class Undead:  # Parent Class
    def __init__(self, name=None, hp=None):
        if name is not None and hp is not None:
            self.__hp = hp
            self.__name = "Undead " + name
        else:
            self.__hp = 100
            self.__name = "Undead"
            self.__isDead = False

    # dead is a boolean
    def isDead(self, dead=None):
        if dead is None:
            return self.__isDead
        else:
            self.__isDead = dead

    def getName(self):
        return self.__name

    def getHP(self):
        return self.__hp

    def setName(self, name):
        self.__name = name

    def setHP(self, hp=None, multiplier=None):
        if multiplier is None:
            self.__hp = hp
        else:
            self.__hp = self.__hp * multiplier


class Zombie(Undead):
    zombie_list = []

    def __init__(self):
        super().__init__()

    def attack(self):
        return super().getHP() * 0.5

    def eat(self, obj):
        if self.getHP() < 50:
            print(f"{self.getName()} cannot Attack {obj.getName()}")
        else:
            self.setHP(self.getHP() + (obj.getHP() / 2))
            obj.setHP(obj.getHP() / 2)
            print(f"[{self.getName()}:]")
            print("Health: ", self.getHP())

            if Zombie.isDead(self, True):
                print("Status: Dead")
            else:
                print("Status: Alive")



    @staticmethod
    def add():
        zombie = Zombie()
        zombie_name = input("Name of the Zombie (press enter for default name): ")
        if len(zombie_name) == 0:   # if zombie name is default
            zombie.setName("Zombie")
        else:                       # else not default
            zombie.setName(zombie_name + " Zombie")

        Zombie.zombie_list.append(zombie)  # add to zombie_list list
        print(zombie.getName(), zombie.getHP())


class Vampire(Undead):
    vampire_list = []

    def __init__(self):
        super().__init__()

    def attack(self):
        return super().getHP()

    @staticmethod
    def add():
        vampire = Vampire()
        vampire_name = input("Name of the Vampire (press enter for default name): ")
        if len(vampire_name) == 0:
            vampire.setName("Vampire")
            vampire.setHP(120)
        else:
            vampire.setName(vampire_name + " Vampire")
            vampire.setHP(120)

        vampire.vampire_list.append(vampire)  # add to zombie_list list
        print(vampire.getName(), vampire.getHP())


class Skeleton(Undead):
    def __init__(self, name=None, hp=None):
        super().__init__(name, hp)

    skeleton_list = []

    @staticmethod
    def add():
        skeleton = Skeleton()
        skeleton_name = input("Name of the Skeleton (press enter for default name): ")
        if len(skeleton_name) == 0:
            skeleton.setName("Skeleton")
        else:
            skeleton.setName(skeleton_name + " Skeleton")

        skeleton.skeleton_list.append(skeleton)  # add to skeleton_list list
        print(skeleton.getName(), skeleton.getHP())


class Ghost(Undead):
    def __init__(self, name=None, hp=None):
        super().__init__(name, hp)

    ghost_list = []

    @staticmethod
    def add():
        ghost = Ghost()
        ghost_name = input("Name of the Ghost (press enter for default name): ")
        if len(ghost_name) == 0:
            ghost.setName("Ghost")
        else:
            ghost.setName(ghost_name + " Ghost")

        Ghost.ghost_list.append(ghost)  # add to ghost_list list
        print(ghost.getName(), ghost.getHP())


class Lich(Undead):
    def __init__(self, name=None, hp=None):
        super().__init__(name, hp)

    lich_list = []
    print("hi")

    @staticmethod
    def add():
        lich = Lich()
        lich_name = input("Name of the Lich (press enter for default name): ")
        if len(lich_name) == 0:
            lich.setName("Lich")
        else:
            lich.setName(lich_name + " Lich")

        Lich.lich_list.append(lich)  # add to lich_list list
        print(lich.getName(), lich.getHP())


class Mummy(Undead):
    def __init__(self, name=None, hp=None):
        super().__init__(name, hp)

    mummy_list = []

    @staticmethod
    def add():
        mummy = Mummy()
        mummy_name = input("Name of the Mummy (press enter for default name): ")
        if len(mummy_name) == 0:
            mummy.setName("Mummy")
        else:
            mummy.setName(mummy_name + " Mummy")

        Mummy.mummy_list.append(mummy)  # add to mummy_list list
        print(mummy.getName(), mummy.getHP())


def main_menu():  # main menu
    print(""" 
  -=============-        
  + U N D E A D +
  -=============-

[1] - Create Undead
[2] - Command Undead
[3] - Display Undead
[4] - Exit 
    """)
    match int(choice()):
        case 1:
            return choose_undead()
        case 2:
            return choose_command()
        case 3:
            return display_all()
        case _:
            return 0


def choose_command():
    print("-=================================-")
    print("    C O M M A N D  U N D E A D     ")
    print("-=================================-")
    print("[A] - Zombie")
    print("[B] - Vampire")
    print("[C] - Skeleton")
    print("[D] - Ghost")
    print("[E] - Lich")
    print("[F] - Mummy")
    print("[0] <-- Go back")

    match choice():
        case 'a':
            return select_zombie()
        case 'b':
            return select_vampire()
        case _:
            return choose_command()


def select_zombie():
    counter = 1
    if len(Zombie.zombie_list) == 0:
        print("\nNo Zombies.\n\n")
        return choose_command()
    else:
        print("\n-=======================-")
        print("      Z O M B I E S      ")
        print("-=======================-")

        for i, zombie in enumerate(Zombie.zombie_list):
            print("[", counter, "]", zombie.getName())
            counter += 1

    x = int(input("Select a zombie: "))

    if 1 <= x <= len(Zombie.zombie_list):
        selected_zombie = Zombie.zombie_list[x - 1]
        print("You selected:", selected_zombie.getName())
        # Perform actions with the selected zombie

        print("                         [SKILLS]\n")
        print("[1] - Eat")
        print("Eat another undead as a result it will increase its HP by the")
        print("half of the HP of the undead being eaten\n")
        print("[2] - Normal Attack")
        print("Deals is half of its HP.\n")

        match int(choice()):
            case 1:
                print("Use Bite to who?\n\n")
                Zombie.eat(selected_zombie, attack_undead(selected_zombie))
                #attack_undead(selected_zombie.getName())



                return main_menu()
            case 2:
                print("YOu have used normal attack!!")
                return main_menu()

    else:
        print("Invalid selection. Please try again.")
        select_zombie()

    return choose_command()



def select_vampire():
    counter = 1
    if len(Vampire.vampire_list) == 0:
        print("\nThere are No Vampires. try again.")
        return choose_command()
    else:
        print("\n\n-=======================-")
        print("     V A M P I R E     ")
        print("-=======================-")
        for i, vampire in enumerate(Vampire.vampire_list):
            print("[", counter, "]", vampire.getName())
            counter += 1

    x = int(input("Select a vampire: "))

    if 1 <= x <= len(Zombie.zombie_list):
        selected_zombie = Zombie.zombie_list[x - 1]
        print("You selected:", selected_zombie.getName())
        # Perform actions with the selected zombie here
    else:
        print("Invalid selection. Please try again.")
        select_zombie()

    return choose_command()


def choose_undead():
    print("\n-=======================-")
    print(" C R E A T E  U N D E A D")
    print("-=======================-")

    print("[A] - Zombie")
    print("[B] - Vampire")
    print("[C] - Skeleton")
    print("[D] - Ghost")
    print("[E] - Lich")
    print("[F] - Mummy")
    print("\n[0] <-- Go back")

    match choice():
        case 'a':  # Zombie
            Zombie.add()
            return main_menu()

        case 'b':  # Vampire
            Vampire.add()
            return main_menu()

        case 'c':  # Skeleton
            Skeleton.add()
            return main_menu()

        case 'd':  # Ghost
            Ghost.add()
            return main_menu()

        case 'e':  # Lich
            Lich.add()
            return main_menu()

        case 'f':  # Mummy
            Mummy.add()
            return main_menu()

        case _:
            print("Invalid Input!!!\n\n")
            return choose_undead()


def display_all():
    undead_list = (Zombie.zombie_list + Vampire.vampire_list + Skeleton.skeleton_list + Ghost.ghost_list +
                   Lich.lich_list + Mummy.mummy_list)

    if len(undead_list) == 0:
        print("No Undead created.")
        return main_menu()

    for undead in undead_list:
        print("--------------------")
        print(undead.getName())
        print("HP: ", undead.getHP())
        print("State: ", undead.isDead())
    return main_menu()


def attack_undead(select_undead):
    print("-=================================-")
    print("    A T T A C K   U N D E A D     ")
    print("-=================================-")
    print("[A] - Zombie")
    print("[B] - Vampire")
    print("[3] - Skeleton")
    print("[4] - Ghost")
    print("[5] - Lich")
    print("[6] - Mummy")
    print("[0] <-- Go back")

    match choice():
        case 'a':
            counter = 1
            for z, zombie in enumerate(Zombie.zombie_list):
                print("[", counter, "]", zombie.getName())
                counter += 1

            x = int(input("Select a zombie: "))

            if 1 <= x <= len(Zombie.zombie_list):
                selected_zombie = Zombie.zombie_list[x - 1]
                print(select_undead.getName(), " will bite ", selected_zombie.getName())
                # Perform actions with the selected zombie here
            else:
                print("Invalid selection. Please try again.")
                select_zombie()
            return selected_zombie

        case 'b':
            counter = 1
            for v, vampire in enumerate(Vampire.vampire_list):
                print("[", counter, "]", vampire.getName())
                counter += 1

            x = int(input("Select a Vampire: "))

            if 1 <= x <= len(Vampire.vampire_list):
                selected_vampire = Vampire.vampire_list[x - 1]
                print(select_undead.getName(), " will bite ", selected_vampire.getName())
                # Perform actions with the selected zombie here
            else:
                print("Invalid selection. Please try again.")
                select_vampire()
            return selected_vampire



def choice():
    c = input("Please select your choice: ").lower()  # convert to higher case
    return c


print(main_menu())