# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, start):
        self.name = name
        self.room = start

    def __str__(self):
        return self.room.__str__()

    def move(self, dir):
        if hasattr(self.room, dir):
            self.room = getattr(self.room, dir)
            return self.room
        else:
            return "I can't move there"
