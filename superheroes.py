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
        
if __name__ == "__main__":
    # If you run this file from the terminal
    # this block of code is executed.
    ability = Ability("Great Debugging", 50)
    another_ability = Ability("Smarty Pants", 90)
    hero = Hero("Grace Hopper", 200)
    hero.add_ability(ability)
    hero.add_ability(another_ability)
    print(hero.attack())