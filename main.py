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
    
    def __init__(self, name=None, hp=None):
        super().__init__(name, hp)
        if name is not None and hp is not None:
            self.__hp = hp
            self.__name = "Zombie " + name
        else:
            self.__hp = 100
            self.__name = "Zombie"
            self.__isDead = False
            
    # def __init__(self):
    #     super().__init__(name, hp)
    #     if name is not None:
    #         self.__name = name + " Zombie"
    #     else:
    #         self.__name = "Zombie"

    def attack(self):
        return super().getHP() * 0.5



class Vampire(Undead):
    def __init__(self, name=None, hp=None):
        super().__init__(name, hp)

    vampire_list = []

    @classmethod
    def add(cls, name=None, hp=None):
        new_vampire = cls(name=name, hp=hp)
        cls.vampire_list.append(new_vampire)
        return new_vampire


class Skeleton(Undead):
    def __init__(self, name=None, hp=None):
        super().__init__(name, hp)

    skeleton_list = []

    @classmethod
    def add(cls, name=None, hp=None):
        new_skeleton = cls(name=name, hp=hp)
        cls.skeleton_list.append(new_skeleton)
        return new_skeleton



class Ghost(Undead):
    def __init__(self, name=None, hp=None):
        super().__init__(name, hp)

    ghost_list = []

    @classmethod
    def add(cls, name=None, hp=None):
        new_ghost = cls(name=name, hp=hp)
        cls.ghost_list.append(new_ghost)
        return new_ghost


class Lich(Undead):
    def __init__(self, name=None, hp=None):
        super().__init__(name, hp)

    lich_list = []

    @classmethod
    def add(cls, name=None, hp=None):
        new_lich = cls(name=name, hp=hp)
        cls.lich_list.append(new_lich)
        return new_lich


class Mummy(Undead):
    def __init__(self, name=None, hp=None):
        super().__init__(name, hp)

    mummy_list = []

    @classmethod
    def add(cls, name=None, hp=None):
        new_mummy = cls(name=name, hp=hp)
        cls.mummy_list.append(new_mummy)
        return new_mummy


def main_menu():  # main menu
    print("""          
U N D E A D

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
            return "Display"
        case _:
            return 0


def choose_command():
    undead_counter = int(1)
    print("\n\n C H O O S E  U N D E A D\n\n")
    if not len(Zombie.zombie_list):
        print("-= Z O M B I E S =-")
        print("[No Zombies Created]")
    else:
        print("-= Z O M B I E S =-")
        for show_zombies in Zombie.zombie_list:
            print("[", undead_counter, "]", Zombie.getName(show_zombies))
            undead_counter += 1


def choose_undead():
    print("\n\n C R E A T E  U N D E A D")
    print("[A] - Zombie")
    print("[B] - Vampire")
    print("[C] - Skeleton")
    print("[D] - Ghost")
    print("[E] - Lich")
    print("[F] - Mummy")
    print("\n[0] <-- Go back")

    match choice():
        case 'a':  # Zombie
            zombie = Zombie()
            zombie_name = input("Name of the Zombie (press enter for default name): ")
            zombie.setName(zombie_name)

            Zombie.zombie_list.append(zombie)   # add to zombie_list list
            print(zombie.getName(), zombie.getHP())
            return main_menu()

        case 'b':  # Vampire
            vampire_name = input("Name of the Vampire (press enter for default name): ")
            if len(vampire_name) == 0:
                Vampire.add("Vampire", int(120))
            else:
                Vampire.add(vampire_name + " Vampire", int(120))

            for vampire in Vampire.vampire_list:
                print(Vampire.getHP(vampire), Vampire.getName(vampire))
            return main_menu()

        case 'c':  # Skeleton
            skeleton_name = input("Name of the Skeleton (press enter for default name): ")
            if len(skeleton_name) == 0:
                Skeleton.add("Skeleton", int(80))
            else:
                Skeleton.add(skeleton_name + " Skeleton", int(80))
            return main_menu()

        case 'd':  # Ghost
            ghost_name = input("Name of the Ghost (press enter for default name): ")
            if len(ghost_name) == 0:
                Ghost.add("Ghost", (100 / 2))
            else:
                Ghost.add(ghost_name + " Ghost", int(80))
            return main_menu()

        case 'e':  # Lich
            lich_name = input("Name of the Lich (press enter for default name): ")
            if len(lich_name) == 0:
                Lich.add("Lich", int(80))
            else:
                Lich.add(lich_name + " Lich", int(80))
            return main_menu()

        case 'f':  # Mummy
            mummy_name = input("Name of the Mummy (press enter for default name): ")
            if len(mummy_name) == 0:
                Mummy.add("Mummy", int(100))
            else:
                Mummy.add(mummy_name + " Mummy", int(100))
            return main_menu()

        case _:
            print("Invalid Input!!!\n\n")
            return choose_undead()


def choice():
    c = input("Please select your choice: ").lower()  # convert to higher case
    return c


print(main_menu())
