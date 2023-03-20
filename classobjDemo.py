class Animal:
    animal="dog"
    def __init__(self,breed):
        self.breed=breed

    def setcolor(self,color):
        self.color=color

    def getcolor(self):
        return self.color

d=Animal("German Shepherd")
d.setcolor("brown and black")
print(d.getcolor())
