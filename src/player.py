# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, start):
        self.name = name
        self.room = start
        self.items = []

    def __str__(self):
        return self.room.__str__()

    def move(self, dir):
        if hasattr(self.room, dir):
            self.room = getattr(self.room, dir)
            return self.room
        else:
            return "I can't do that"

    def get(self, item):
        recieved = self.room.removeItem(item)
        if recieved:
            self.items.append(recieved)
            return f"You successfully picked up {recieved.name}"
        else:
            return f"{item} is not in this room"

    def drop(self, name):
        new_items = []
        for i, item in enumerate(self.items):
            if not str.lower(item.name) == name:
                new_items.append(item)
            else:
                new_items = new_items + self.items[i+1:]
                self.items = new_items
                self.room.addItem(item)
                return f"You have dropped {item.name} in {self.room.name}\n\n{self.room}"
        self.items = new_items
        return f"You do not possess {name}\n\n{self.room}"

    def viewInventory(self):
        if not len(self.items):
            return "You sadly lack any items in your bag"
        output = "In you bag, you have: \n"
        for item in self.items:
            output += "" + item.__str__() + '\n'
        return output
