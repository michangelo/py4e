# def createAnimal(name):
#     newAnimal = {'name':name, 'x':1}
#     return newAnimal

# def party(animal)
#     animal['x'] = animal['x'] + 1 

# animal = []

# for i in range(3):
#     animals.append(createAnimal())
#     print(animals[-1]) 

# fruit = 'apple'
# print(reversed(fruit) for frui in fruit)

class PartyAnimal:
   x = 0
   name = ''
   def __init__(self, nam):
     self.name = nam
     #print(self.name,'constructed')

   def party(self) :
     self.x = self.x + 1
     #print(self.name,'party count',self.x)


from party import PartyAnimal

class CricketFan(PartyAnimal):
   points = 0
   def six(self):
      self.points = self.points + 6
      self.party()
      print(self.name,"points",self.points)

s = PartyAnimal("Sally")
s.party()
j = CricketFan("Jim")
j.party()
j.six()
print(dir(j))

# Code: http://www.py4e.com/code3/party6.py