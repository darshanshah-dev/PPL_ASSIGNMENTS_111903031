try :
   x = 1 / 0
   print(x)
except ZeroDivisionError:
   print("Error: Divide by zero")
else :
   print("Division successful")