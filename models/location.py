class Location():

    def __init__(self, name, address, id = ""):
        if id != "":
            self.id = id
        self.name = name
        self.address = address