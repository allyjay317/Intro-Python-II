# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, dscr):
        self.name = name
        self.dscr = dscr

    def __str__(self):
        return self.name + "\n" + self.dscr
