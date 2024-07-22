from inventory.item import Item

class Laptop(Item):
    def __init__(self, assetTag, description, os):
        super().__init__(assetTag, description)
        self._os = os

    def getOS(self):
        return self._os

    def __str__(self):
        return super().__str__() + "{:<10}".format(self.getOS())

    def getAvailableLaptop(self):
        output = "{:<10}{:<30}{:<10}{:<12}{:<10}\n".format(
            "AssetTag", "Description", "Available", "Due Date", "OS")
        if not hasattr(self, 'laptopList') or len(self.laptopList) == 0:
            output += "There is no laptop to display."
        else:
            for laptop in self.laptopList:
                if laptop.getIsAvailable() == "Yes":
                    output += str(laptop) + "\n"
        return output

# Example usage
if __name__ == "__main__":
    laptop1 = Laptop("L123", "Dell XPS", "Windows 10")
    laptop2 = Laptop("L124", "MacBook Pro", "macOS")
    laptop1.setIsAvailable(True)
    laptop2.setIsAvailable(False)

    # Simulating a list of laptops
    laptop1.laptopList = [laptop1, laptop2]

    print(laptop1.getAvailableLaptop())
