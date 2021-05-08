# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, dscr):
        self.name = name
        self.dscr = dscr
        self.__items__ = []

    def __str__(self):
        output = self.name + "\n" + self.dscr
        if len(self.__items__):
            output += "\nIn this room, you can see: "
            for item in self.__items__:
                output += item.name + ", "
            output = output[:-2]
        return output

    def removeItem(self, name):
        new_items = []
        for i, item in enumerate(self.__items__):
            if not str.lower(item.name) == name:
                new_items.append(item)
            else:
                new_items = new_items + self.__items__[i+1:]
                self.__items__ = new_items
                return item
        self.__items__ = new_items
        return None

    def addItem(self, item):
        self.__items__.append(item)
