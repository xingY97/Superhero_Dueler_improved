import random

class Ability:
    def __init__(self, name, max_damage):
        """Initialize the values passed into this methods as instance variables."""
        
        #Assign the "name" and "max_damage"
        #for a specific instance of the Ability class
        self.name = name
        self.max_damage = max_damage

    def attack(self):

        #Pick a random value between 0 and self.max_damage
        random_value = random.randint(0,self.max_damage)
        return random_value

class Armor:
    def __init__(self, name, max_block):
        """Instantiate instance properties.
            name:String
            max_block: Integer"""
        #TODO: Create instance variables fro the values to passed in.
        self.name = name
        self.max_block = max_block

    def block(self):
        """Return a  random value between 0 and the initialized max_block strength."""
        random_value = random.randint(0,self.max_block)
        return random_value

class Hero:
    #We want our hero to have a default "starting_health",
    #so we can set that in the function header.
    def __init__(self, name, starting_health=100):
        """Instance properties:
            abilities: List
            armors: List
            name: String
            starting_health:Integer
            current_health: Integer"""

        #abilities and armors don't have starting values,
        #and are set to empty lists on initialization
        self.abilities = list()
        self.armors = list()
        #We know the name of our hero, so we assign it here
        self.name = name
        #similarly, our starting health is passed in, just like name
        self.starting_health = starting_health
        #When a hero is created, their current health is 
        #a alwasy the same as their starting health (no damage taken yet!)
        self.current_health = starting_health

    def add_ability(self, ability):
        """Add ability to abilities list"""
        #We used the append method to add strings to a list
        #we are not adding strings, instead we'll add ability objejcts.
        self.abilities.append(ability)

    def attack(self):
        """Calculate the total damage from all ability attacks.
        return:total_damage:Int"""

        #start our total out at 0
        total_damage = 0
            #loop through all of our hero's abilities
        for ability in self.abilities:
                #add the damage of each attack to our running total
            total_damage += ability.attack()
            #return the total damage
        return total_damage

    def add_armor(self,armor):
        """add armor to self.armors
        Armor: Armor Object"""
        #TODO: Add armor object that is passed in to 'self.armors'
        self.armors.append(armor)
    
    def defend(self,damage_amt):
        """Calculate the total block amount from all armor blocks.
        return: total_block:Int"""
        #TODO: This method should run the block method on each armor in self.armors
        total_defend = 0
        for defend in self.armors:
            total_defend += defend.block()
        return total_defend

    def take_damage (self,damage):
        """Updates self.current_health to reflect the damage minus the defense"""
        #TODO: Create a method that updates self.current_health to the current 
        #Minus the amount returned from calling self.defend(damage).
        defense = self.defend(damage)
        self.current_health -= damage - defense
        
    def is_alive(self):
        """Return True or False depending on whether the hero is alive or not"""
        #TODO: check the current_health of the hero
        # if it is <=0, then return False. Otherwise, they still have health
        #and are therefore alive, so return True
        if self.current_health > 0:
            return True
        else:
            return False
    def fight(self, opponent):  
    
    # TODO: Fight each hero until a victor emerges.
    # Phases to implement:
    # 0) check if at least one hero has abilities. If no hero has abilities, print "Draw"
    # 1) else, start the fighting loop until a hero has won
    # 2) the hero (self) and their opponent must attack each other and each must take damage from the other's attack
    # 3) After each attack, check if either the hero (self) or the opponent is alive
    # 4) if one of them has died, print "HeroName won!" replacing HeroName with the name of the hero, and end the fight loop
    
        if len(self.abilities) == 0 and len(opponent.abilities) == 0:
            print("Draw")
        while self.is_alive() and opponent.is_alive():
            self_damage = self.attack()
            opponent.take_damage(self_damage)
            opponent_damage = opponent.attack()
            self.take_damage(opponent_damage)

        if opponent.is_alive():
            print("Dumbledore  won")
        
        else:
            print("Wonderwoman won")

    def add_weapon(self,weapon):
        """add weapon to self.abilities"""
        #TODO: This method will append the weapon object passed in as an
        #Argument to self.abilities.
        #This means that self.abilitites will be a list of 
        #abilitites and weapons
        self.abilities.append(weapon)

class Weapon(Ability):
    def attack(self):
        """This method returns a random value between one half to the full attack power of the weapon."""
        #TODO: Use integer division to find half of the max_damage value
        #Then return a random integer bwtween half of max_damage and max_damage
        return random.randint(self.max_damage//2,self.max_damage)

class Team:
    def __init__(self,name):
        """Initialize your team with its team name and an empty list of heroes"""
        self.name = name
        self.heroes = list()

    def remove_hero(self,name):
        """Remove hero from heroes list. if hero isn't found return 0."""
        foundHero = False
        #loop through each hero in our list
        for hero in self.heroes:
            # if we find them, remove them from the list
            if hero.name == name:
                self.heroes.remove(hero)
                #set our indicator to True
                foundHero = True
        # if we looped through our list and did not find our hero,
        # the indicator would have never changed, so return 0
        if not foundHero:
            return 0
    def view_all_heroes(self):
        """print out all heroes to the consle."""
        #TODO: loop over the list of heroes and print their names to the terminal one by one.
        for heroes in self.heroes:
            print(heroes.name)

    def add_hero(self, hero)
        """Add hero object to self.heroes."""
        #TODO: Add the hero object that is passed in to the list of heroes in
        #self.heroes
        self.heroes.append(hero)
        return

    
        

    

        
if __name__ == "__main__":
    # If you run this file from the terminal
    # this block of code is executed.
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())