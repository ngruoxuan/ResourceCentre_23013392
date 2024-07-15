class Laptop():
    # Refactor (E): Extract duplicate attributes and methods.
    # There are several common attributes and methods in
    # Camera.py and Laptop.py. Extract these common attributes
    # and methods into a super class, named item.py
    def __init__(self, assetTag, description, os):
        self._assetTag = assetTag
        self._description = description
        self._dueDate = ""
        self._isAvailable = True
        self._os = os

    def getAssetTag(self):
        return self._assetTag

    def getDescription(self):
        return self._description

    def getDueDate(self):
        return self._dueDate

    def getIsAvailable(self):
        if self._isAvailable:
            return "Yes"
        else:
            return "No"

    def getOS(self):
        return self._os

    def setDueDate(self, dueDate):
        self._dueDate = dueDate

    def setIsAvailable(self, isAvailable):
        self._isAvailable = isAvailable

    def getAvailableLaptop(self):
        output = ""
        output += "{:<10}{:<30}{:<10}{:<12}{:<10}\n".format("AssetTag", 
                    "Description", "Available", "Due Date", "OS")
        if len(self.laptopList) == 0:
            output += "There is no laptop to display."
        else:
            for i in self.laptopList:
                if i.getIsAvailable() == "Yes":
                    # Refactor (D): Extract duplicate code as __str__()
                    # If __str__() already created, use it.
                    output += "{:<10}{:<30}{:<10}{:<12}{:<10}\n".format(
                        i.getAssetTag(), i.getDescription() , 
                        i.getIsAvailable(), i.getDueDate(), 
                        i.getOS() )
        return output
