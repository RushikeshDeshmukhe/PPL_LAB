# import module sys to get the type of exception 


#Exceptions
# 1. Module imoprt error
# 2. zero dision error
# 3. value error
# 4. 








try :
 import sys
except :
 print("Module sys not found")

# module not found error
try :
 import numpy
 print("module succesfully imported")
except:
 print("Oops! Module is not found ") 


randomList = ['a', 'b', 0]
for entry in randomList: 
 try: 
  print("The entry is", entry) 
  r= 1/int(entry) 
  print("The reciprocal of", entry, "is", r)
  print()
  break 
 except: 
  print("Oops!", sys.exc_info()[0], "occurred.") 
  print("Next entry.") 
  print() 
