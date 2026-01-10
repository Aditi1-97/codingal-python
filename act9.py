
class Robot:
    def __init__(self, name, model, purpose):
        self.name = name
        self.model = model
        self.purpose = purpose

    def introduce(self):
        print("Hello! 🤖")
        print(f"My name is {self.name}.")
        print(f"My model number is {self.model}.")
        print(f"I am designed to {self.purpose}.")

    def greet(self, user_name):
        print(f"Nice to meet you, {user_name}! 😊")


my_robot = Robot("Astra", "AI-Nova-5", "help humans learn programming")

my_robot.introduce()
my_robot.greet("Aditi")
