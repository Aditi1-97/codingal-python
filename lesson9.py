class Fruits:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def fruitsName(self):
        print(f"My name is {self.name}")

    def fruitsColor(self):
        print(f"My color is {self.color}")    



Apple = Fruits("Apple", "Green")      
Banana = Fruits("Banana", "Yellow")  


Apple.fruitsName()
Apple.fruitsColor()

Banana.fruitsName()
Banana.fruitsColor()
