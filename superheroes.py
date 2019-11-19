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


if __name__ == "__main__":
    #If you run this file from the terminal
    #this block in executed.
    ability = Ability("Debugging Ability", 20)
    print(ability.name)
    print(ability.attack())