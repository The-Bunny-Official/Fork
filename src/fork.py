import time

class Fork():
    def __init__(self, prongs: int = 4, autowashing: bool = False, length: int = 5):
        self.prongs = prongs
        self.auto = autowashing
        self.length = length
        self.dirty = 0

    def wash(self, quick: bool = False):
        if quick == True:
            if self.dirty >= 10:
                print("Beginning Wash")
                time.sleep(5)
                print("Washed")
                self.dirty -= 10
            else:
                print("Not dirty enough")
                return
            return
        else:
            if self.dirty >= 50:
                print("Beginning wash")
                time.sleep(25)
                print("Washed")
                self.dirty -= 50
            else:
                print("Not dirty enough")
                return
        print(f"Fork is now {self.dirty}% dirty")

    def use(self, food: str):
        print("Using fork")
        self.dirty += ((len(food) + self.prongs) * self.length)
        print(f"Your fork is now {self.dirty}% dirty")