class Animal:
    def __init__ (self):
        self.num_eyes = 2, "minor anomalies allowed."

    def breathe(self):
        print("inhale, exhale.")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("doing it under water.")

    def swim(self):
        print("moving in water.")

nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)