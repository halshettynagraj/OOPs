from msilib import init_database


class team:
    name = ""
    captn = ""

    def winteamfansreview(self):
        if self.name == "India":
            return "we won"
        elif self.name == "Austrailia":
            return "we loss"


t1 = team()
t1.name = "India" 
t1.captn = "Msd"

t2 = team()
t2.name = "Austrailia"
t2.captn = "KV"

print(t1.winteamfansreview())