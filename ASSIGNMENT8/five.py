try :
   import test.h
except NameError:
    print("We are here")
except ImportError:
   print("Error: Import not possible")
else :
   print("Import successful")