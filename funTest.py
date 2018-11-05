
def area(width, height=0):
    return width * height

def printinfo1( arg1, *vartuple ):
   "打印任何传入的参数"
   print ("输出: ")
   for var in vartuple:
      print (var)
   return

def printinfo( arg1, **vardict ):
   "打印任何传入的参数"
   print ("输出: ")
   print (vardict)
