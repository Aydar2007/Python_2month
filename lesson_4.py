import random
total_rounds=0
#RPG-Role Play Game

class GameEntity:
    def __init__(self,name,health,damage) -> None:
        self.__name=name
        self.__health=health
        self.__damage=damage
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        self.__name=value
    @property
    def health(self):
        return self.__health
    @health.setter
    def health(self,value):
        self.__health=value
        if value<=0:
            value=0
    @property
    def damage(self):
        return self.__damage
    @damage.setter
    def damage(self,value):
        self.__damage=value
    def __str__(self) -> str:
        return f"name:{self.name}  health:{self.health}  damage:{self.damage}"
    
class Boss(GameEntity):
    def __init__(self, name, health, damage) -> None:
        super().__init__(name, health, damage)

class Hero(GameEntity):
    def __init__(self, name, health, damage,super_ability_type) -> None:
        super().__init__(name, health, damage)
        self.__super_ability_type=super_ability_type

    @property
    def super_ability_type(self):
        return self.__super_ability_type
    @super_ability_type.setter
    def super_ability_type(self,value):
        self.__super_ability_type=value
    
    def apply_super_power(self,boss:Boss,heroes:list):
        pass

class Warrior(Hero):
    def __init__(self, name, health, damage) -> None:
        super().__init__(name, health, damage,"Critical_Damage")

    def apply_super_power(self,boss:Boss,heroes:list):
        coef=random(1,5)
        boss.health-=self.damage*coef
        print(f"Boss_Health:{boss.health},critical_damage:{self.damage*coef}")


class Medic(Hero):
    def __init__(self, name, health, damage,heal_point) -> None:
        super().__init__(name, health, damage, "heal")
        self.heal_point=heal_point

    def apply_super_power(self,boss:Boss,heroes:list):
        print(f"")
class Magic(Hero):
    def __init__(self, name, health, damage) -> None:
        super().__init__(name, health, damage, "Boost")

    def apply_super_power(self,boss:Boss,heroes:list):
        pass   

def is_game_finished(boss:Boss,heroes:list):
    if boss.health<=0:
        print("Heroes WON!!!")
        return True
    all_heroes_dead=True
    for hero in heroes:
        if hero.health>0:
            all_heroes_dead=False
    if all_heroes_dead:
        print("Boss WON")

    return all_heroes_dead

def print_info(boss:Boss,heroes):
    print(f"total round:{             total_rounds}     ")
    print(boss)
    for hero in heroes:
        print(hero)

def Boss_hit(boss:Boss,heroes:list):
    for hero in heroes:
        hero.health-=boss.damage

def heroes_hit(boss:Boss,heroes:list):
    for hero in heroes:
        boss.health-heroes.damage
def heroes_power(boss:Boss,heroes:list):
    for hero in heroes:
        hero.super_a(boss,heroes)

def play_round(boss,heroes):
    global total_rounds
    total_rounds+=1
    Boss_hit(boss,heroes)
    heroes_hit(boss,heroes)
    heroes_power(boss,heroes)


def start():
    boss=Boss("Antaras",2000,50)
    warrior=Warrior("Varvar",260,400)
    # medic=Medic("Medical_military",280,30)
    # magic=Magic("Fireman",250,45)
    heroes=[warrior]
    while not is_game_finished(boss,heroes):
        play_round(boss,heroes)
start()
