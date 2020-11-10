try :
   x = '2' + 6
   print(x)
except TypeError as error:
    print(error)
    print("Error: Conversion not possible")
else :
   print("Conversion successful")