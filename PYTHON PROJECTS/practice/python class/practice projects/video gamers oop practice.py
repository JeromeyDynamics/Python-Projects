class video_gamers():
    def __init__(self,name,role,rank,damage,health):
        self.name = name
        self.role = role
        self.rank = rank
        self.damage = damage
        self.health = health
                    
    def shooting(self):
        print(f"{self.name} is shooting but, their health is only {self.health} and their rank is {self.rank}.")
    
    def hiding(self):
        print(f"{self.name} is hiding but, they only have {self.damage} damage!")
    
    def dead(self):
        print(f"{self.name} is dead even tough they are a {self.role} and they are even rank {self.rank}!")
    
gamer1 = video_gamers("deezle986", "damage", "diamond1", 1232, 22)
gamer2 = video_gamers("ur_mum60", "healer", "gold 3", 200, 200)
gamer3 = video_gamers(":()32", "tank", "platinum 1", 834, 500)

print(gamer1.shooting())
print(gamer2.dead())
print(gamer3.hiding())