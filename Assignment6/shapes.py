import turtle

s=turtle.getscreen()
t=turtle.Turtle()


class shape():

 def __init__(self):
  self.__sides
  self.__angles
  self.__dimensions
  self.__length
  
 def show(self):
  if(self.__length and self.__sides and self.__angles):
   for _ in range(self.__sides):
    t.forward(self.__length[_])
    t.right(self.__angles[_])
     
 def get_sides(self):
  return(self.__sides)
 def set_sides(self,s):
  self.__sides=s
  
 def get_angles(self):
  return(self.__angles)
 def set_angles(self,s):
  self.__angles=s
  
 def get_dimensions(self):
  return(self.__dimensions)
 def set_dimensions(self,s):
  self.__dimensions=s
   
 def get_length(self):
  return(self.__length)
 def set_length(self,s):
  self.__length=s 
 
   
class _2Dshape(shape):
 def __init__(self):
  self.set_dimensions(2)
   
 
class _3Dshape(shape):
 def __init__(self):
  self.__set_dimensions(3) 
 
class polygon(_2Dshape):
 pass


class square(polygon):
 def __init__(self): 
  self.set_sides(4)
  self.set_angles([90,90,90,90])


class rectangle(polygon):
 def __init__(self): 
  self.set_sides(4)
  self.set_angles([90,90,90,90])
 
 
class triangle(polygon):
 def __init__(self): 
  self.set_sides(3)
 
class eqitriangle(triangle):
 def __init__(self):
  self.set_angles([60,60,60])
 
class pentagone(shape):
 def __init__(self): 
  self.set_sides(5)
  self.set_angles([72,72,72,72,72])
 pass
 
class hexagone(shape):
 def __init__(self): 
  self.set_sides(6)
  self.set_angles([120,120,120,120,120,120])
 
 
class cube(_3Dshape):
 def __init__(self): 
  self.set_sides(12)
 
class cuboide(shape):
 def __init__(self): 
  self.set_sides(12)
 
 
s=square()
s.set_dimensions(2)
print("sides of square=",s.get_sides(),s.get_dimensions(),)
s.set_length([100,100,100,100])
s.show()

eq=eqitriangle()
print("Eqilateral triangle has angles=", eq.get_angles())

p=pentagone()
p.set_length([80,80,80,80,80])
p.show()



t1=triangle()
t1.set_length([100,100,100])
t1.set_angles([120,120,120])
t1.show()





