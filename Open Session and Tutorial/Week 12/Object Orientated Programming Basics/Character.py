class Character:

    def __init__(self,name="",health=0,defence=0,agility=0):

        self.name = name
        self.health = health
        self.defence = defence
        self.agility = agility

    def adjust_hp(self, new_val):

        self.health = new_val

    def adjust_def(self, new_val):

        self.defence = new_val

    def adjust_agi(self, new_val):

        self.agility = new_val

    def __str__(self):

        output = f"""
Character Name : {self.name}
Health Points  : {self.health}
Total Defence  : {self.defence}
Total Agility  : {self.agility}
"""
        return output