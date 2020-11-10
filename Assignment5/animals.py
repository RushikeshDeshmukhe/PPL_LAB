class animal():
 def __init__(self):
  self.__legs
  self.__eyes
  self.__speaks
  self._tail
 def get_legs(self):
  return(self.__legs)
 def get_eyes(self):
  return(self.__eyes)
 def get_speaks(self):
  return(self.__speaks)
 def get_tail(self):
  return(self.__tail)
 def set_legs(self,n):
  self.__legs=n
 def set_eyes(self,n):
  self.__eyes=n
 def set_speaks(self,n):
  self.__speaks=n
 def set_tail(self,n):
  self.__tail=n
  
class wild(animal):
 pass
 
class domestic(animal):
 pass

class reptile(animal):   
 pass
    
class amphibian(animal):
 pass    
    
    
class cat(domestic):
 def __init__(self):
  self.set_legs(4)
  self.set_eyes(2)
  self.set_speaks("meow")
  self.set_tail(1)
 
class lizard(reptile):
 def __init__(self):
  self.set_legs(4)
  self.set_eyes(2)
  self.set_speaks("")
  self.set_tail(1)
 
class tortois(amphibian):
 def __init__(self):
  self.set_legs(4)
  self.set_eyes(2)
  self.set_speaks("")
  self.set_tail(1)
 
class kangaroo(wild):
 def __init__(self):
  self.set_legs(2)
  self.set_eyes(2)
  self.set_speaks("")
  self.set_tail(1)
 
class tiger(wild):
 def __init__(self):
  self.set_legs(4)
  self.set_eyes(2)
  self.set_speaks("")
  self.set_tail(1)
 
class elephant(wild):
 def __init__(self):
  self.set_legs(4)
  self.set_eyes(2)
  self.set_speaks("")
  self.set_tail(1)
 
class mouse(wild):
 def __init__(self):
  self.set_legs(4)
  self.set_eyes(2)
  self.set_speaks("")
  self.set_tail(1)
 
class panda(wild):
 def __init__(self):
  self.set_legs(4)
  self.set_eyes(2)
  self.set_speaks("")
  self.set_tail(0)
 
class snake(reptile):
 def __init__(self):
  self.set_legs(0)
  self.set_eyes(2)
  self.set_speaks("")
  self.set_tail(0)
 
class frog(amphibian):
 def __init__(self):
  self.set_legs(4)
  self.set_eyes(2)
  self.set_speaks("")
  self.set_tail(0)

tom=cat()

print("Tom is a cat and has legs =",tom.get_legs())

k=kangaroo()

print("k is a kangaroo and has legs =",k.get_legs())



