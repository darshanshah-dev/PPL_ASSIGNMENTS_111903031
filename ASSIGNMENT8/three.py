try :
   x = 5 * test
   print(x)
except NameError:
   print("Error: Variable not defined")
except :
    print("Something went wrong")
else :
   print("Calculation successful")