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

    def status(self, obj):
        print(f"\n[{self.getName()}]")
        print("Health: ", self.getHP())

        if self.getHP() <= 0:
            self.isDead(True)
        else:
            self.isDead(False)

        if self.isDead():
            if isinstance(self, Vampire):
                print("Status: Alive (cannot attack)")
            elif isinstance(self, Lich):
                print("Status: Alive (cannot attack)")
            else:
                print("Status: Dead")
        else:
            print("Status: Alive")

        print(f"\n[{obj.getName()}]")
        print("Health: ", obj.getHP())

        if obj.getHP() <= 0:
            obj.isDead(True)
        else:
            obj.isDead(False)

        if obj.isDead():
            if isinstance(obj, Vampire):
                print("Status: Alive (cannot attack)")
            elif isinstance(obj, Lich):
                print("Status: Alive (cannot attack)")
            else:
                print("Status: Dead")
        else:
            print("Status: Alive")


class Zombie(Undead):
    zombie_list = []

    def __init__(self):
        super().__init__()

    def attack(self, obj):
        if self.getHP() < 50:
            print(f"{self.getName()} cannot Attack {obj.getName()}")
        if isinstance(obj, Ghost):  # if attacking is a ghost
            obj.setHP(obj.getHP() - (self.getHP() / 2) * 0.10)
        elif isinstance(obj, Mummy):    # if attacking is a mummy
            obj.setHP(obj.getHP() - (self.getHP() / 2))
            if obj.getHP() <= 0:
                print("Hp reduced to 0. Reviving...")
                obj.setHP(100)
        else:
            obj.setHP(obj.getHP() - (self.getHP() / 2))
        Undead.status(self, obj)




    def eat(self, obj):
        if self.getHP() < 50:
            print(f"{self.getName()} cannot Attack {obj.getName()}")
        if isinstance(obj, Ghost):
            self.setHP(self.getHP() + (obj.getHP() / 2))
            obj.setHP(obj.getHP() / 2)
        else:
            self.setHP(self.getHP() + (obj.getHP() / 2))
            obj.setHP(obj.getHP() / 2)

        Undead.status(self, obj)
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
        self.setHP(multiplier=1.2)

    def attack(self, obj):
        if self.getHP() <= 0:
            print(f"{self.getName()} cannot attack {obj.getName()} anymore!")
        if isinstance(obj, Ghost):
            obj.setHP(obj.getHP() - self.getHP() * 0.10)
        elif isinstance(obj, Mummy):
            obj.setHP(obj.getHP() - self.getHP())
            Undead.status(self, obj)
            if obj.getHP() <= 0:
                print("Hp reduced to 0. Reviving...")
                obj.setHP(100)
        else:
            obj.setHP(obj.getHP() - self.getHP())
        Undead.status(self, obj)


    def bite(self, obj):
        self.setHP(self.getHP() + obj.getHP() * 0.8)
        Undead.status(self, obj)

    @staticmethod
    def add():
        vampire = Vampire()
        vampire_name = input("Name of the Vampire (press enter for default name): ")
        if len(vampire_name) == 0:
            vampire.setName("Vampire")
        else:
            vampire.setName(vampire_name + " Vampire")

        vampire.vampire_list.append(vampire)  # add to zombie_list list
        print(vampire.getName(), vampire.getHP())


class Skeleton(Undead):
    def __init__(self, name=None, hp=None):
        super().__init__(name, hp)
        self.setHP(multiplier=0.8)

    skeleton_list = []



    def attack(self, obj):
        if isinstance(obj, Ghost):
            obj.setHP(obj.getHP() - (self.getHP() * 0.7) * 0.10)
        else:
            obj.setHP(self.getHP() * 0.7)
        Undead.status(self, obj)

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
        self.setHP(multiplier=0.5)

    ghost_list = []

    def haunt(self, obj):
        self.setHP(self.getHP() + obj.getHP() * 0.10)
        Undead.status(self, obj)

    def attack(self, obj):
        if isinstance(obj, Ghost):
            obj.setHP(obj.getHP() - (self.getHP() * 0.2) * 0.10)
        else:
            obj.setHP(obj.getHP() - self.getHP() * 0.2)
        Undead.status(self, obj)

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
        self.setHP(multiplier=0.8)

    lich_list = []
    def leech(self, obj):
        self.setHP(self.getHP() + obj.getHP() * 0.10)
        Undead.status(self, obj)

    def attack(self, obj):
        if isinstance(obj, Ghost):
            obj.setHP(obj.getHP() - (self.getHP() * 0.7) * 0.10)
        else:
             obj.setHP(obj.getHP() - self.getHP() * 0.7)
        Undead.status(self, obj)

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

    def eat(self, obj):
        if self.getHP() < 50:
            print(f"{self.getName()} cannot Attack {obj.getName()}")
        else:
            self.setHP(self.getHP() + (obj.getHP() / 2))
            obj.setHP(obj.getHP() / 2)
        Undead.status(self, obj)

    def attack(self, obj):
        if self.getHP() < 50:
            print(f"{self.getName()} cannot Attack {obj.getName()}")
        if isinstance(obj, Ghost): # if ghost will be attacked
            obj.setHP(obj.getHP() - ((self.getHP() *  0.5) + (obj.getHP() * 0.10)) * 0.10 )
            Undead.status(self, obj)
        else:
            obj.setHP(obj.getHP() - ((self.getHP() *  0.5) + (obj.getHP() * 0.10)))
            Undead.status(self, obj)
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
        case 'c':
            return select_skeleton()
        case 'd':
            return select_ghost()
        case 'e':
            return select_lich()
        case 'f':
            return select_mummy()
        case _:
            return main_menu()


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
            case 2:
                print("YOu have used normal attack!!")
                Zombie.attack(selected_zombie, attack_undead(selected_zombie))
            case _:
                print("Invalid Input Please try again!")
                return select_zombie()
    else:
        print("Invalid selection. Please try again.")
        select_zombie()

    return main_menu()

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

    if 1 <= x <= len(Vampire.vampire_list):
        selected_vampire = Vampire.vampire_list [x - 1]
        print("You selected:", selected_vampire.getName())
        # Perform actions with the selected vampire here

        print("                         [SKILLS]\n")
        print("[1] - Bite")
        print("Bite which increases their HP by 80% of the undead HP being bitten.\n")
        print("[2] - Normal Attack")
        print("Deals equivalent of vampire's HP.\n")

        match int(choice()):
            case 1:
                print("Use Bite to who?\n\n")
                Vampire.bite(selected_vampire, attack_undead(selected_vampire))
            case 2:
                if selected_vampire.getHP() <= 0:
                    print("You Cannot attack without HP!")
                    selected_vampire.setHP(0)
                    return choose_command()
                print("You have used normal attack!!")
                Vampire.attack(selected_vampire, attack_undead(selected_vampire))
            case _:
                print("Invalid Input Please try again!")
                return select_vampire()
    else:
        print("Invalid selection. Please try again.")
        select_vampire()

    return main_menu()

def select_skeleton():
    counter = 1
    if len(Skeleton.skeleton_list) == 0:
        print("\nThere are No Vampires. try again.")
        return choose_command()
    else:
        print("\n\n-=======================-")
        print("     S K E L E T O N     ")
        print("-=======================-")
        for i, skeleton in enumerate(Skeleton.skeleton_list):
            print("[", counter, "]", skeleton.getName())
            counter += 1

    x = int(input("Select a Skeleton: "))

    if 1 <= x <= len(Skeleton.skeleton_list):
        selected_skeleton = Skeleton.skeleton_list[x - 1]
        print("You selected:", selected_skeleton.getName())
        # Perform actions with the selected skeleton here

        print("                         [SKILLS]\n")
        print("[1] - Normal Attack")
        print("Deals 70% of it's HP.\n")

        match int(choice()):
            case 1:
                print("Use Normal Attack to who?\n\n")
                Skeleton.attack(selected_skeleton, attack_undead(selected_skeleton))
                return main_menu()
            case _:
                print("Invalid Input Please try again!")
                return select_skeleton()
    else:
        print("Invalid selection. Please try again.")
        select_skeleton()

    return main_menu()

def select_ghost():
    counter = 1
    if len(Ghost.ghost_list) == 0:
        print("\nThere are No Ghost. try again.")
        return choose_command()
    else:
        print("\n\n-=======================-")
        print("     G H O S T     ")
        print("-=======================-")
        for i, ghost in enumerate(Ghost.ghost_list):
            print("[", counter, "]", ghost.getName())
            counter += 1

    x = int(input("Select a Ghost: "))

    if 1 <= x <= len(Ghost.ghost_list):
        selected_ghost = Ghost.ghost_list[x - 1]
        print("You selected:", selected_ghost.getName())
        # Perform actions with the selected ghost here

        print("                         [SKILLS]\n")
        print("[1] - Haunt")
        print("Increases its HP by the 10% of the undead being haunt.\n")
        print("[2] - Normal Attack")
        print("Deals 20% of the Ghost's HP")

        match int(choice()):
            case 1:
                print("Use Haunt to who?\n\n")
                Ghost.haunt(selected_ghost, attack_undead(selected_ghost))
                return main_menu()
            case 2:
                print("Use Normal Attack to who?\n\n")
                Ghost.attack(selected_ghost, attack_undead(selected_ghost))
            case _:
                print("Invalid Input Please try again!")
                return select_ghost()
    else:
        print("Invalid selection. Please try again.")
        select_ghost()

    return main_menu()

def select_lich():
    counter = 1
    if len(Lich.lich_list) == 0:
        print("\nThere are No Lich. try again.")
        return choose_command()
    else:
        print("\n\n-=======================-")
        print("     L I C H     ")
        print("-=======================-")
        for l, lich in enumerate(Lich.lich_list):
            print("[", counter, "]", lich.getName())
            counter += 1

    x = int(input("Select a Lich: "))

    if 1 <= x <= len(Lich.lich_list):
        selected_lich = Lich.lich_list[x - 1]
        print("You selected:", selected_lich.getName())
        # Perform actions with the selected lich here

        print("                         [SKILLS]\n")
        print("[1] - Leech")
        print("Cast a spell on undead which gets the 10% of their HP and add it to its HP.\n")
        print("[2] - Normal Attack")
        print("Deals 70% of the Lich's HP")

        match int(choice()):
            case 1:
                print("Use Leech to who?\n\n")
                Lich.leech(selected_lich, attack_undead(selected_lich))
                return main_menu()
            case 2:
                if selected_lich.getHP() <= 0:
                    print("You Cannot attack without HP!")
                    selected_lich.setHP(0)
                    return choose_command()
                else:
                    print("Use Normal Attack to who?\n\n")
                    Lich.attack(selected_lich, attack_undead(selected_lich))
            case _:
                print("Invalid Input Please try again!")
                return select_lich()

    else:
        print("Invalid selection. Please try again.")
        select_lich()

    return main_menu()

def select_mummy():
    counter = 1
    if len(Mummy.mummy_list) == 0:
        print("\nThere are No Mummy. try again.")
        return choose_command()
    else:
        print("\n\n-=======================-")
        print("     M U M M Y     ")
        print("-=======================-")
        for m, mummy in enumerate(Mummy.mummy_list):
            print("[", counter, "]", mummy.getName())
            counter += 1

    x = int(input("Select a Mummy: "))

    if 1 <= x <= len(Mummy.mummy_list):
        selected_mummy = Mummy.mummy_list[x - 1]
        print("You selected:", selected_mummy.getName())
        # Perform actions with the selected Mummy here

        print("                         [SKILLS]\n")
        print("[1] - Eat")
        print("Cast a spell on undead which gets the 10% of their HP and add it to its HP.\n")
        print("[2] - Normal Attack")
        print("Deals 70% of the Lich's HP")

        match int(choice()):
            case 1:
                print("Use Eat to who?\n\n")
                Mummy.eat(selected_mummy, attack_undead(selected_mummy))
                return main_menu()
            case 2:
                print("Use Normal Attack to who?\n\n")
                Mummy.attack(selected_mummy, attack_undead(selected_mummy))

                if selected_mummy.getHP() <= 0:
                    Undead.isDead(selected_mummy, None)
            case _:
                print("Invalid Input Please try again!")
                return select_mummy()

    else:
        print("Invalid selection. Please try again.")
        select_mummy()

    return main_menu()
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


        if undead.getHP() <= 0:
            undead.isDead(True)
        else:
            undead.isDead(False)

        if undead.isDead():
            if isinstance(undead, Vampire):
                print("Status: Alive (cannot attack)")
            elif isinstance(undead, Lich):
                print("Status: Alive (cannot attack)")
            else:
                print("Status: Dead")
        else:
            print("Status: Alive")
    return main_menu()


def attack_undead(select_undead):
    global selected_zombie, selected_vampire, selected_ghost, selected_skeleton, selected_lich, selected_mummy
    print("-=================================-")
    print("    A T T A C K   U N D E A D     ")
    print("-=================================-")
    print("[A] - Zombie")
    print("[B] - Vampire")
    print("[C] - Skeleton")
    print("[D] - Ghost")
    print("[E] - Lich")
    print("[F] - Mummy")
    print("[0] <-- Go back")
    counter = 1

    match choice():
        case 'a':
            for z, zombie in enumerate(Zombie.zombie_list):
                print("[", counter, "]", zombie.getName())
                counter += 1

            x = int(input("Select a zombie: "))

            if 1 <= x <= len(Zombie.zombie_list):
                selected_zombie = Zombie.zombie_list[x - 1]
                print(select_undead.getName(), " will attack ", selected_zombie.getName())
                # Perform actions with the selected zombie here
            else:
                print("Invalid selection. Please try again.")
                select_zombie()

            return selected_zombie

        case 'b':
            # counter = 1
            for v, vampire in enumerate(Vampire.vampire_list):
                print("[", counter, "]", vampire.getName())
                counter += 1

            x = int(input("Select a Vampire: "))

            if 1 <= x <= len(Vampire.vampire_list):
                selected_vampire = Vampire.vampire_list[x - 1]
                print(select_undead.getName(), " will attack ", selected_vampire.getName())
                # Perform actions with the selected zombie here
            else:
                print("Invalid selection. Please try again.")
                select_vampire()
            return selected_vampire
        case 'c':
            # counter = 1
            for s, skeleton in enumerate(Skeleton.skeleton_list):
                print("[", counter, "]", skeleton.getName())
                counter += 1

            x = int(input("Select a Skeleton: "))

            if 1 <= x <= len(Skeleton.skeleton_list):
                selected_skeleton = Skeleton.skeleton_list[x - 1]
                print(select_undead.getName(), " will attack ", selected_vampire.getName())
                # Perform actions with the selected zombie here
            else:
                print("Invalid selection. Please try again.")
                select_skeleton()
            return selected_skeleton
        case 'd':
            counter = 1
            for g, ghost in enumerate(Ghost.ghost_list):
                print("[", counter, "]", ghost.getName())
                counter += 1
            x = int(input("Select a Ghost: "))

            if 1 <= x <= len(Ghost.ghost_list):
                selected_ghost = Ghost.ghost_list[x - 1]
                print(select_undead.getName(), " will attack ", selected_ghost.getName())
                # Perform actions with the selected ghost here
            else:
                print("Invalid selection. Please try again.")
                select_ghost()
            return selected_ghost
        case 'e':
            for l, lich in enumerate(Lich.lich_list):
                print("[", counter, "]", lich.getName())
                counter += 1
            x = int(input("Select a Lich: "))

            if 1 <= x <= len(Lich.lich_list):
                selected_lich = Lich.lich_list[x - 1]
                print(select_undead.getName(), " will attack ", selected_lich.getName())
                # Perform actions with the selected lich here
            else:
                print("Invalid selection. Please try again.")
                select_lich()
            return selected_lich
        case 'f':
            for m, mummy in enumerate(Mummy.mummy_list):
                print("[", counter, "]", mummy.getName())
                counter += 1

            x = int(input("Select a Mummy: "))
            if 1 <= x <= len(Mummy.mummy_list):
                selected_mummy = Mummy.mummy_list[x - 1]
                print(select_undead.getName(), " will attack ", selected_mummy.getName())
                # Perform actions with the selected mummy here

            else:
                print("Invalid selection. Please try again.")
                select_mummy()
            return selected_mummy
        case '0':
            return choose_command()
        case _:
            return "Error" , choose_command()
def choice():
    c = input("Please select your choice: ").lower()  # convert to higher case
    return c

print(main_menu())
